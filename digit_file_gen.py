from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean

def createEx():
	numberAr = open('num.txt','a')
	range1 = range(0,10)#nums we have
	versions = range(1,10)
	
	for i in range1:
		for j in versions:
			print(str(i)+'.'+str(j))
			imageFilePath = 'images/numbers/'+str(i)+'.'+str(j)+'.png'
			ei = Image.open(imageFilePath)
			eiar = np.array(ei)
			eiar1 = str(eiar.tolist())
			print(eiar1)
			lineToWrite = str(i)+'::'+eiar1+'\n'
			numberAr.write(lineToWrite)

			

def threshold(imageArray):
	balanceAr = []
	newAr = imageArray
	for i in imageArray:
		for j in i:
			avg = mean(j[:3])
			balanceAr.append(avg)
	balance = mean(balanceAr)	
	for i in newAr:
		for j in i:
			if mean(j[:3]) > balance:
				j[0] = 255
				j[1] = 255
				j[2] = 255
				j[3] = 255
			else:
				j[0] = 0
				j[1] = 0
				j[2] = 0
				j[3] = 255
	return newAr
			
		
		
		

im1 = Image.open('images/numbers/0.1.png')

iar1 = np.array(im1)

iar1 = threshold(iar1)

fig = plt.figure()
s = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
s1 = plt.subplot2grid((8,6),(5,0), rowspan=3, colspan=3)
#s.imshow(iar)
s1.imshow(iar1) 


createEx()
plt.show()




