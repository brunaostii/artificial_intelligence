#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:43:39 2019

@author: brunaosti
"""
import pandas as pd
import numpy as np

class neural_network(object):
    
    def __init__(self, dataset1, dataset2, n, e):
        self.train_dataset = pd.read_csv(dataset1)
        self.test_dataset = pd.read_csv(dataset2)
        self.X_train = [] 
        self.X_test = []
        self.y_train = []
        self.n = n
        self.e = e
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
        self.output = []
        eqm_atual = 1
        eqm_ant = 0
        
        while(np.abs(eqm_atual - eqm_ant) >= self.e):

            eqm_ant = self.calculation_eqm()
            
            for i in range(len(self.y_train)):
                u = np.dot(self.w.transpose(), self.X_train[:,i:i+1])
                self.w = self.w + self.n*(self.y_train[i] - u) * self.X_train[:, i:i+1]
                
            self.epochs += 1
            eqm_atual = self.calculation_eqm()

            
    def calculation_eqm(self):
        eqm = 0
        
        for i in range(len(self.X_train[0])):
            u = np.dot(self.w.transpose(),self.X_train[:, i:i+1])
            eqm = eqm + ((self.y_train[i] - u)*(self.y_train[i] - u))
            
        eqm = eqm/len(self.X_train)
        
        return eqm
        
    def output_final(self):
        
        for i in range(len(self.X_test[0])):
            self.output.append(self.signal(np.dot(self.w.transpose(), self.X_test[:,i:i+1])))
        
        return self.output
    
    def signal(self, num: float):
    
        if(num >= 0):
            return 1
    
        else:
            return -1
        