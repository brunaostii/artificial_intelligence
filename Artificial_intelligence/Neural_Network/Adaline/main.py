#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:40:43 2019

@author: brunaosti
"""
from adaline import neural_network

teste = neural_network('train_dataset.csv', 'test.csv', 0.01, 0.001)
teste.pre_processing()
teste.training()
print(teste.output_final())
print(teste.epochs)