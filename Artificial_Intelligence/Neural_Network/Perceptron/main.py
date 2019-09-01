#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 19:40:43 2019

@author: brunaosti
"""
from perceptron import neural_network

teste = neural_network('train_dataset.csv', 'test.csv', 0.01)
teste.pre_processing()
teste.training()
print('Saída', teste.output_final())
print('Número de iterações', teste.epochs)