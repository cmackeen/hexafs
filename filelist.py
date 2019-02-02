import pandas as pd
import numpy as np
import xraydb
import sklearn as skl
import matplotlib.pyplot as plt


'''
we're using  python3 for this . . 
'''

datain="043b2gg_pre.dat"
datainr="043b2gg.dat"
#path used for testing
path='./xxdmini/mapbr/es/'
class :
	def __init__(self, datain):
		self.datain= datain

	def reader(self):
		with open(path+str(datain)) as myfile:
			head = [next(myfile) for x in range(20)]
			hd_len=pd.Series(head).str.contains('#').sum()
		df=pd.read_csv(path+datain, skiprows=hd_len, sep='\s+')
		df.columns=['e','mu','blnk']
		return df

