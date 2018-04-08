# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:54:53 2016
@author: erik
"""

A = 9.8 #acceleration of gravity in meters per second squared

def velocity(t):
    V = A * t
    return V
    
def distance(t):
    X = (A * (t**2)) / 2
    return X

    
     

     