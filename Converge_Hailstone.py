#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:36:54 2019

@author: shrutirajani
"""

def available(p,q):
    if p in q:
        return 1
    else:
        return 2
    
for a in range(0,11):
    for b in range(0,11):
        holding=[]
        for x in range(1,1001):
            x1=x
            t=[]
            c=0
            breaker=0
            r=[]
            while available(x1,t)==2:
                if c>1000:
                    breaker=1
                    print(a,b,'bad')
                    break;
                else:
                    t.append(x1)
                    if x1%2==0:
                        x1//=2
                    else:
                        x1=a*x1+b
                    c=c+1
            if(breaker==0):
                ndx=t.index(x1)
                r=t[ndx:]
                r.sort()
                if r not in holding and r != []:
                    holding.append(r)
            else:
                break
        if(breaker==0):
            rcycle=len(holding)
            print(a,b,rcycle)

