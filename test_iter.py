import pandas as pd
import numpy as np
from xraydb import XrayDB
import sklearn as skl
import matplotlib.pyplot as plt
from readers import *
from filelist import *
from xas_character import *
'''
we're using  python3 for this . . 
'''

datain="043b2gg_pre.dat"
datainr="043b2gg.dat"
#path='./xxdmini/mapbr/es/'
import os
rootdir = './minixxdmini'


	
alledges=[]
edg=XAS_EStats
for jk in filels.index:
    if len(filels[jk].split('/')) ==5:
        statty=[]
        mm=edg.edgenom(filels,jk)
        if mm[1] != 'pre_unkn':
            statty=edg.signoise(filels,jk,mm[1])
        alledges.append([mm[1],statty])
alledge_df=pd.DataFrame(alledges)
pd.DataFrame(alledges).to_csv('alledges.cvs')


'''
iterator used to to experiment on new xas_chaarcter methods
'''
