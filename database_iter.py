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
	if len(filels[jk].split('/')) == 5:
		mm=edg.edgenom(filels,jk)
		alledges.append(mm[1])
alledge_df=pd.DataFrame(alledges)
pd.DataFrame(alledges).to_csv('alledges.cvs')


'''
current error due to 2 or 3 columns in the data, so naming the columsn from EData.reader() needs to be robust'd
'''
