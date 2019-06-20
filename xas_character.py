import pandas as pd
import numpy as np
from xraydb import XrayDB
import sklearn as skl
import matplotlib.pyplot as plt
from readers import *
from xas_character import *
from filelist import *

'''
we're using  python3 for this . . 
'''

datain="043b2gg_pre.dat"
datainr="043b2gg.dat"
#path='./xxdmini/mapbr/es/'
import os
rootdir = './minixxdmini'


class XAS_EStats:
	def __init__(self, rootdir):
		self.datain= rootdir
		b=File_Compile(rootdir)
		filels=b.lister()
		return filels

	def signoise(filels, inter, edge):
		jj=inter
		data=EData(filels[jj])
		df=data.reader(data.datain)
		edgelib=XrayDB()
		edgenom=edgelib.xray_edge(edge,'K')[0]
		if len(df[df['e']>100+edgenom])<20:
			edgenom=edgelib.xray_edge(edge,'L3')[0]
		dftrim=df[df['e']>100+edgenom]
		xfsmean=dftrim[dftrim.columns[1]].mean()
		xfsstd=dftrim[dftrim.columns[1]].std()
		return xfsmean,xfsstd


                

	def edgenom(filels,inter):
		jj=inter
		data=EData(filels[jj])
		df=data.reader(data.datain)
		df['diff']=df[df.columns[1]].diff()
		edgelib=XrayDB()
		edgeid='pre_unkn'
		for z in np.linspace(15,77,63):
			if abs(edgelib.xray_edge(edgelib.symbol(int(z)),'K')[0]-df['e'][df['diff'].idxmax()])<15:
				edgeid=edgelib.symbol(int(z))
				print(edgelib.xray_edge(edgelib.symbol(int(z)),'K')[0]-df['e'][df['diff'].idxmax()])
				print(edgeid)
				print('K')
				print(jj)
			elif abs(edgelib.xray_edge(edgelib.symbol(int(z)),'L3')[0]-df['e'][df['diff'].idxmax()]) < 15:
				edgeid=edgelib.symbol(int(z))
				print(edgeid)
				print('L3')
				print(jj)
				print(edgelib.xray_edge(edgelib.symbol(int(z)),'K')[0]-df['e'][df['diff'].idxmax()])

		return df,edgeid,filels[jj]
	



'''
current error due to 2 or 3 columns in the data, so naming the columsn from EData.reader() needs to be robust'd
'''
