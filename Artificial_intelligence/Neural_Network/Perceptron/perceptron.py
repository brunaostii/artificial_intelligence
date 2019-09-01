#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:43:39 2019

@author: brunaosti
"""
import pandas as pd
import numpy as np

class neural_network(object):
    
    def __init__(self, dataset1, dataset2, n):
        self.train_dataset = pd.read_csv(dataset1)
        self.test_dataset = pd.read_csv(dataset2)
        self.X_train = [] 
        self.X_test = []
        self.y_train = []
        self.n = n
        self.w = []
        self.output = []
        self.epochs = 0
        
    def pre_processing(self):
        self.X_train= np.hstack((-1*np.ones((len(self.train_dataset),1)), self.train_dataset.iloc[:,0:3].values))
        self.X_test = np.hstack((-1*np.ones((len(self.test_dataset),1)), self.test_dataset.iloc[:,:].values))
        self.y_train = self.train_dataset.iloc[:, 3].values
        
        self.X_train = self.X_train.transpose()
        self.y_train = self.y_train.transpose()
        self.X_test = self.X_test.transpose()

    def training(self):
        self.w = np.random.rand(1,len(self.X_train)).transpose()

        error = 1
        
        while(error):
            error = 0
            for i in range(len(self.y_train)):
                y = self.signal(np.dot(self.w.transpose(), self.X_train[:,i:i+1]))
                
                if y != self.y_train[i]:
                    self.w = self.w + (self.n*(self.y_train[i] - y) * self.X_train[:,i:i+1])
                    error = 1
            self.epochs += 1
            
    def output_final(self):
        
        for i in range(len(self.X_test[0])):
            self.output.append(self.signal(np.dot(self.w.transpose(), self.X_test[:,i:i+1])))
        
        return self.output
    
    def signal(self, num: float):
    
        if(num >= 0):
            return 1
    
        else:
            return -1
        
