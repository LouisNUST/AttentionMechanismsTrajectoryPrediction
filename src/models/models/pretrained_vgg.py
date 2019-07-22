import torch
import torch.nn as nn
import torch.nn.functional as f 
import random
import numpy as np 
import torchvision
import imp
import time

class Identity(nn.Module):
    def __init__(self):
        super(Identity, self).__init__()
        
    def forward(self, x):
        return x
# mobilenet pretrained on imagenet
class customCNN1(nn.Module):
    def __init__(self):

        
        super(customCNN1,self).__init__()

        # For mobilenet_v2 uncomment following
        self.cnn = torchvision.models.mobilenet_v2(pretrained=True).features #mobilenet
        # self.cnn = torchvision.models.vgg19(pretrained=True).features #vgg19

        # self.cnn = torchvision.models.segmentation.fcn_resnet101(pretrained=True).backbone #semantic segmentation
        # print(self.cnn)

        self.reduce_layer = nn.AdaptiveAvgPool2d((7,7))
        
        for param in self.cnn.parameters():
            param.requires_grad = False
        
 
    
    def forward(self,x):
        x = self.cnn(x)  
        # x = self.cnn(x)['out'][0] #semantic

        cnn_features = self.reduce_layer(x)
        return cnn_features