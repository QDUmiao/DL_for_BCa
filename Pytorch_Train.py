import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import roc_curve, auc
import torch.optim as optim
import torch.nn.functional as F

def pr(netx, test_loader):
    correct = 0
    total = 0
    au = 0
    OI = 0
    IO = 0
    ZERO = 0
    ONES = 0
    la = []
    pre = []
    prob = []
    with torch.no_grad():
        for i, data in enumerate(test_loader, 0):
            images, labels = data[0].to(torch.float).to(
                device), data[1].to(torch.float).to(device)
            outputs,_ = netx(images)
            preprob2 = torch.exp(outputs.data)
            for i in preprob2:
                prob.append(i[1].cpu())
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            ZERO += (torch.tensor(0) == labels).sum().item()
            ONES += (torch.tensor(1) == labels).sum().item()
            correct += (predicted == labels).sum().item()
            OI += (predicted > labels).sum().item()
            IO += (predicted < labels).sum().item()
            
            
            for k in np.array(labels.cpu()):
                la.append(k)
            for k in np.array(predicted.cpu()):
                pre.append(k)
                

    fpr, tpr, threshold = roc_curve(la, prob)
    au = auc(fpr, tpr)*100
    plt.figure(figsize=(5,5))
    plt.plot(fpr, tpr, color='darkorange',
              lw=2, label='ROC curve (area = %0.2f)' % au)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()
    print(au, "%")
    print(correct/total*100, "%")
    print(OI*100/ZERO, "%")
    print(IO*100/ONES, "%")
    return au, correct/total*100, OI*100/ZERO, IO*100/ONES

def draw_train_process(title,iters,costs,accs,auc,OI,IO,label_cost,lable_acc,label_auc,label_oi,label_io):
    Wro = []
    for i in range(len(OI)):
        Wro.append((OI[i] + IO[i]) / 2) 
    plt.title(title, fontsize=10)
    plt.xlabel("iter", fontsize=10)
    plt.ylabel("acc(\%)", fontsize=10)
    plt.plot(iters, OI,color='teal',label=label_oi) 
    plt.plot(iters, IO,color='purple',label=label_io) 
    plt.plot(iters, accs,color='green',label=lable_acc) 
    plt.plot(iters, auc,color='blue',label=label_auc) 
    plt.plot(iters, Wro,color='red',label='AveWroPre') 
    plt.legend()
    plt.grid()
    plt.show()
    
class ImBLossFun(nn.Module):
    def init_(self):
        super(ImBLossFun,self)._init_()


    def forward(self,x,y,t):
        t = torch.tensor(t).to(device)
        x = F.softmax(x,dim=1)
        # print(x)
        # print(y)
        eps = 1e-7
        y = F.one_hot(y,num_classes = x.size(1))
        #print(y)
        ce = -1 * torch.log(x+eps) * y
        #print(ce)
        loss = torch.pow((1-x), 2) * ce
        #print(loss)
        loss = torch.mul(loss, t)
        #print(loss)
        loss = torch.sum(loss, dim=1)
        #print(loss)
        return torch.mean(loss)

class MyDataset(Dataset):
    def __init__(self, img_path, transform=None):
        super(MyDataset, self).__init__()
        self.root = img_path
        self.txt_root = self.root + '\\' + 'data.txt'

        f = open(self.txt_root, 'r')
        data = f.readlines()
        imgs = []
        labels = []
        for line in data:
            line = line.rstrip()
            word = line.split()
            imgs.append(os.path.join(self.root,word[2], word[0]))
            labels.append(word[1])
        self.img = imgs
        self.label = labels
        self.transform = transform

    def __len__(self):
        return len(self.label)

    def __getitem__(self, item):
        img = self.img[item]
        label = self.label[item]
        img = Image.open(img).convert('RGB')
        if self.transform is not None:
            img = self.transform(img)
        label = np.array(label).astype(np.int64)
        label = torch.from_numpy(label)
        return img,label

class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()
        self.conv0 = nn.Conv2d(3, 3, kernel_size=12,padding=2,stride = 2)
        self.conv1 = nn.Conv2d(3, 6, kernel_size=5,padding=2)
        self.conv2 = nn.Conv2d(6,16,kernel_size=5)
        self.conv3 = nn.Conv2d(16,120,kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.relu = nn.LeakyReLU()
        self.fc1 = nn.Linear(120,60)
        self.bn = nn.BatchNorm1d(60)
        self.fc2 = nn.Linear(60,2)
        self.logsoftmax = nn.LogSoftmax()

    def forward(self,x):
        in_size = x.size(0)  
        out = self.relu(self.mp(self.conv0(x)))
        out = self.relu(self.mp(self.conv1(out)))
        out = self.relu(self.mp(self.conv2(out)))
        out = self.relu(self.conv3(out))
        out = out.view(in_size, -1)
        out = self.relu(self.fc1(out))
        out = self.relu(self.bn(out))
        feature = out
        out = self.fc2(out)
        return self.logsoftmax(out) , feature

    
def make_txt(root, file_name, label):
    path = os.path.join(root, file_name)  
    data = os.listdir(path)
    f = open(root + '\\' + 'data.txt', 'a')
    for line in data:
        f.write(line + ' ' + str(label) + ' ' + file_name + '\n')
    f.close()

def ModelTrain(net,times,saveauc,train_accs,train_loss,test_accs,train_auc,test_auc,OI,IO,bestauc,bestacc,t,tt,ttt,pth,SAVENAME):
    for epoch in range(times):
        running_loss = 0.0
        la = []
        pre = []
        tt += ttt
        t[1] = t[1] + tt
        for i,data in enumerate(train_loader,0):
            inputs,labels = data[0].to(device), data[1].to(device)
            optimizer.zero_grad()          
            outputs,_ = net(inputs)
            loss = loss_function(outputs,labels,t)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            if i%2 == 0:
                print('[%d,%5d] loss :%.3f' %
                      (epoch+1,i+1,running_loss/100))
                running_loss = 0.0
            train_loss.append(loss.item())

            correct = 0
            total = 0
            _, predicted = torch.max(outputs.data, 1)
            total = labels.size(0)
            correct = (predicted == labels).sum().item()
            for k in np.array(labels.cpu()):
                la.append(k)
            for k in np.array(predicted.cpu()):
                pre.append(k)
            train_accs.append(100*correct/total)
            testauc,testacc,oi,io = pr(net,test_loader)
            print("BestACC:",bestacc)
            print("BestAUC:",bestauc)
            if((testauc+testacc) > (bestauc+bestacc)):
                bestauc = testauc
                bestacc = testacc
                if(testauc > saveauc):
                    SAVEPATH = pth + '\\' + SAVENAME + '_' + str(round(bestacc,2)) + '_' + str(round(bestauc,2)) + '.pth'
                    if(not os.path.exists(SAVEPATH)):
                        torch.save(net.state_dict(), SAVEPATH)
            OI.append(oi)
            IO.append(io)
            test_auc.append(testauc)
            train_iters = range(len(train_accs))
            draw_train_process('Training',train_iters,train_loss,train_accs,test_auc,OI,IO,'training loss','training acc','test auc','O-I','I-O')
            
if __name__ == '__main__':
################################################################################
    pth = r'C:\Users\Miao\Desktop\PTH'
    SaveName = 'Test'
    path = r"C:\Users\Miao\Desktop\GTRAIN"
    path2 = r"C:\Users\Miao\Desktop\GTEST"
    trainbatch = 256
    t = [100,400]
    tt = 3.5
    ttt = 0
    SaveAuc = 60
    seed = 35331
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
################################################################################
    transform = transforms.Compose([
        transforms.Resize([120,120]),
        transforms.ToTensor()
    ]) 
    if(not os.path.exists(path + '\\data.txt')):
        make_txt(path, file_name='1', label=1)
        make_txt(path, file_name='0', label=0)
    dataset = MyDataset(path, transform=transform)
    train_loader = DataLoader(dataset=dataset, batch_size=trainbatch, shuffle=True)
    if(not os.path.exists(path2 + '\\data.txt')):
        make_txt(path2, file_name='1', label=1)
        make_txt(path2, file_name='0', label=0)
    testset = MyDataset(path2, transform=transform)
    test_loader = DataLoader(dataset=testset, batch_size=999, shuffle=False)
#########################################################################################
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
    net = CNN().to(device)
    net.to(device)
    print(net)
    net.load_state_dict(torch.load(r""))
    


    loss_function = ImBLossFun() 
    optimizer = optim.SGD(net.parameters(), lr=0.0003, momentum=0.9)
    # optimizer = torch.optim.Adam(net.parameters(),lr=0.0003)
    train_accs = []
    train_loss = []
    test_accs = []
    train_auc = []
    test_auc = []
    net = net.to(device)
    OI = []
    IO = []
    bestauc = 0
    bestacc = 0
##############################################################################################
    ModelTrain(net,150,SaveAuc,train_accs,train_loss,test_accs,train_auc,test_auc,OI,IO,bestauc,bestacc,t,tt,ttt,pth,SaveName)
    
    SAVEPATH = pth + '\\' + 'best2.pth'
    torch.save(net.state_dict(), SAVEPATH)
    
    PATH = pth + '\\' + 'test.pth'
    net2 = CNN()
    net2.load_state_dict(torch.load(PATH)).to(device)
    pr(net,test_loader)

    




