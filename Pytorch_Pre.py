import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
from torchvision import transforms
from torch.utils.data import DataLoader,Dataset
from sklearn.metrics import roc_curve, auc
import torch.nn.functional as F
import pandas as pd
def prs(path,test_loader,thre = 0,save_feature = False,Task = 'Unknow'):
    names = os.listdir(path)
    models = []
    for name in names:
        if(name[-3] == 'p' and name[-2] == 't' and name[-1] == 'h'):
            models.append(name)
    print(len(models))
    print(models)
    num = len(models)
    if(thre == 0):
        if(num % 2):
            thre = int(round(num/2,0)+1)
        else:
            thre = num/2
    correct = 0
    total = 0
    au = 0
    OI = 0
    IO = 0
    ZERO = 0
    ONES = 0
    la = []
    pre = []
    predicted = []
    WRONG = []
    FEATURE = []
    FNAME = []
    img = np.array(test_loader.dataset.img)
    imgname = []
    for i in range(len(img)):
        imgname.append(str.split(os.path.basename((img[i])),'.')[0])
    with torch.no_grad():
        for i, data in enumerate(test_loader, 0):
            images, labels = data[0].to(torch.float).to(device), data[1].to(torch.float).to(device)
            cou = 0
            for name in models:
                cou += 1
                model = path + '\\' + name
                net = CNN()
                net.load_state_dict(torch.load(model))
                net.to(device)
                print("MODEL" + str(cou) + ':',name)
                pr(net,test_loader)
                outputs,feature = net(images)
                feature = np.array(feature.cpu())
                LA = np.array(labels).reshape(-1,1)
                imgname = np.array(imgname).reshape(-1,1)
                if(len(FEATURE) == 0):
                    FEATURE = np.hstack((imgname,LA))
                else:
                    FEATURE = np.hstack((FEATURE,feature))
                fnum = feature.shape[1]
                fname = []
                for j in range(fnum):
                    fname.append('DL_' + name + '_' + str(j))
                if(len(FNAME) == 0):
                    FNAME.append('name')
                    FNAME.append('label')
                else:
                    FNAME = np.hstack((FNAME,fname))
                svp = path + '\\' + Task + '_FEATURE_' + name + '.csv'
                if(save_feature):
                    pd.DataFrame(columns=fname,data=feature).to_csv(svp,encoding='utf_8_sig',index=None,header = True)
                _, predictedx = torch.max(outputs.data, 1)
                wronglabel = np.array((predictedx != labels).cpu())
                for i in range(len(wronglabel)):
                    if(wronglabel[i]):
                        a = os.path.basename(os.path.split(img[i])[0]) + ' ' + os.path.basename(img[i])
                        WRONG.append(a)
                if(len(predicted) == 0):
                    predicted = predictedx
                else:
                    predicted += predictedx
            for i in range(predicted.size()[0]):
                if(predicted[i] >= thre):
                    predicted[i] = 1
                elif(predicted[i] <= thre):
                    predicted[i] = 0
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
    fpr, tpr, threshold = roc_curve(la, pre)
    au = auc(fpr, tpr)*100
    acc = correct/total*100
    OI = OI*100/ZERO
    IO = IO*100/ONES
    print("AUC:", au, "%")
    print("ACC:", acc, "%")
    print("0-1:", OI, "%")
    print("1-0:", IO, "%")
    svp = path + '\\' + Task + '_FEATURE_ALL'  + '.csv'
    if(save_feature):
        pd.DataFrame(columns=FNAME,data=FEATURE).to_csv(svp,encoding='utf_8_sig',index=None,header = True)
    return au, acc, OI, IO, predicted, WRONG

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
    with torch.no_grad():
        for i, data in enumerate(test_loader, 0):
            images, labels = data[0].to(torch.float).to(
                device), data[1].to(torch.float).to(device)
            outputs,FEATURE = netx(images)
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

    fpr, tpr, threshold = roc_curve(la, pre)
    au = auc(fpr, tpr)*100
    print("AUC:", au, "%")
    print("ACC:", correct/total*100, "%")
    print("0-1:", OI*100/ZERO, "%")
    print("1-0:", IO*100/ONES, "%")
    return au, correct/total*100, OI*100/ZERO, IO*100/ONES,FEATURE


def draw_train_process(title, iters, costs, accs, auc, OI, IO, label_cost, lable_acc, label_auc, label_oi, label_io):
    Wro = []
    for i in range(len(OI)):
        Wro.append((OI[i] + IO[i]) / 2)
    plt.title(title, fontsize=10)
    plt.xlabel("iter", fontsize=10)
    plt.ylabel("acc(\%)", fontsize=10)
    plt.plot(iters, OI, color='teal', label=label_oi)
    plt.plot(iters, IO, color='purple', label=label_io)
    plt.plot(iters, accs, color='green', label=lable_acc)
    plt.plot(iters, auc, color='blue', label=label_auc)
    plt.plot(iters, Wro, color='red', label='AveWroPre')
    plt.legend()
    plt.grid()
    plt.show()


class ImBLossFun(nn.Module):
    def init_(self):
        super(ImBLossFun, self)._init_()

    def forward(self, x, y, t):
        t = torch.tensor(t).to(device)
        x = F.softmax(x, dim=1)
        # print(x)
        # print(y)
        eps = 1e-7
        y = F.one_hot(y, num_classes=x.size(1))
        # print(y)
        ce = -1 * torch.log(x+eps) * y
        # print(ce)
        loss = torch.pow((1-x), 2) * ce
        # print(loss)
        loss = torch.mul(loss, t)
        # print(loss)
        loss = torch.sum(loss, dim=1)
        # print(loss)
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
            imgs.append(os.path.join(self.root, word[2], word[0]))
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
        return img, label


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
        self.logsoftmax = nn.LogSoftmax(dim = 1)

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


if __name__ == '__main__':

    path2 = r'' 

    transform = transforms.Compose([
        transforms.Resize([120, 120]),
        transforms.ToTensor() 
    ])

    if(not os.path.exists(path2 + '\\data.txt')):
        make_txt(path2, file_name='FUFA', label=1)
        make_txt(path2, file_name='WEIFUFA', label=0)
    testset = MyDataset(path2, transform=transform)
    test_loader = DataLoader(dataset=testset, batch_size=len(testset.label), shuffle=False)

    
    device = torch.device("cpu")

    di = r''
    _,_,_,_,pred,WRONG = prs(di,test_loader,5,save_feature = True,Task = 'train')
    
    