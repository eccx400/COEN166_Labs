# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html

import cv2
import numpy as np
import operator
import dot
import os.path
from collections import Counter
import numpy.matlib as ml
import numpy.linalg as la
import glob
import sys
import pprint


#Get file paths
s1 = ['att_faces_10/s1/1.pgm','att_faces_10/s1/2.pgm','att_faces_10/s1/3.pgm','att_faces_10/s1/4.pgm','att_faces_10/s1/5.pgm','att_faces_10/s1/6.pgm','att_faces_10/s1/7.pgm','att_faces_10/s1/8.pgm','att_faces_10/s1/9.pgm','att_faces_10/s1/10.pgm']
s2 = ['att_faces_10/s2/1.pgm','att_faces_10/s2/2.pgm','att_faces_10/s2/3.pgm','att_faces_10/s2/4.pgm','att_faces_10/s2/5.pgm','att_faces_10/s2/6.pgm','att_faces_10/s2/7.pgm','att_faces_10/s2/8.pgm','att_faces_10/s2/9.pgm','att_faces_10/s2/10.pgm']
s3 = ['att_faces_10/s3/1.pgm','att_faces_10/s3/2.pgm','att_faces_10/s3/3.pgm','att_faces_10/s3/4.pgm','att_faces_10/s3/5.pgm','att_faces_10/s3/6.pgm','att_faces_10/s3/7.pgm','att_faces_10/s3/8.pgm','att_faces_10/s3/9.pgm','att_faces_10/s3/10.pgm']
s4 = ['att_faces_10/s4/1.pgm','att_faces_10/s4/2.pgm','att_faces_10/s4/3.pgm','att_faces_10/s4/4.pgm','att_faces_10/s4/5.pgm','att_faces_10/s4/6.pgm','att_faces_10/s4/7.pgm','att_faces_10/s4/8.pgm','att_faces_10/s4/9.pgm','att_faces_10/s4/10.pgm']
s5 = ['att_faces_10/s5/1.pgm','att_faces_10/s5/2.pgm','att_faces_10/s5/3.pgm','att_faces_10/s5/4.pgm','att_faces_10/s5/5.pgm','att_faces_10/s5/6.pgm','att_faces_10/s5/7.pgm','att_faces_10/s5/8.pgm','att_faces_10/s5/9.pgm','att_faces_10/s5/10.pgm']
s6 = ['att_faces_10/s6/1.pgm','att_faces_10/s6/2.pgm','att_faces_10/s6/3.pgm','att_faces_10/s6/4.pgm','att_faces_10/s6/5.pgm','att_faces_10/s6/6.pgm','att_faces_10/s6/7.pgm','att_faces_10/s6/8.pgm','att_faces_10/s6/9.pgm','att_faces_10/s6/10.pgm']
s7 = ['att_faces_10/s7/1.pgm','att_faces_10/s7/2.pgm','att_faces_10/s7/3.pgm','att_faces_10/s7/4.pgm','att_faces_10/s7/5.pgm','att_faces_10/s7/6.pgm','att_faces_10/s7/7.pgm','att_faces_10/s7/8.pgm','att_faces_10/s7/9.pgm','att_faces_10/s7/10.pgm']
s8 = ['att_faces_10/s8/1.pgm','att_faces_10/s8/2.pgm','att_faces_10/s8/3.pgm','att_faces_10/s8/4.pgm','att_faces_10/s8/5.pgm','att_faces_10/s8/6.pgm','att_faces_10/s8/7.pgm','att_faces_10/s8/8.pgm','att_faces_10/s8/9.pgm','att_faces_10/s8/10.pgm']
s9 = ['att_faces_10/s9/1.pgm','att_faces_10/s9/2.pgm','att_faces_10/s9/3.pgm','att_faces_10/s9/4.pgm','att_faces_10/s9/5.pgm','att_faces_10/s9/6.pgm','att_faces_10/s9/7.pgm','att_faces_10/s9/8.pgm','att_faces_10/s9/9.pgm','att_faces_10/s9/10.pgm']
s10 = ['att_faces_10/s10/1.pgm','att_faces_10/s10/2.pgm','att_faces_10/s10/3.pgm','att_faces_10/s10/4.pgm','att_faces_10/s10/5.pgm','att_faces_10/s10/6.pgm','att_faces_10/s10/7.pgm','att_faces_10/s10/8.pgm','att_faces_10/s10/9.pgm','att_faces_10/s10/10.pgm']

sall = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

training = []
testing = []

#Add the files to their respective lists
#Training: 1, 3, 4, 5, 7, 9
#Test: 2, 6, 8, 10
for i in sall:
	for path in i:
		fileName = os.path.basename(path)
		picNum = fileName[:-4]
		if((int(picNum) % 2 != 0) and int(picNum) != 4):
			# Picture Number 1, 3, 4, 5, 7, 9
			training.append(path)
			# print("Training Added " + picNum)
		else:
			# Picture Number 2, 6, 8, 10
			testing.append(path)
			# print("Test Added " + picNum)
print("All Files Added")

train = []
for path in training:
	img = cv2.imread(path)
	img = img[:, :, 2]
	img = img.flatten()
	train.append(img)

train = np.transpose(train)
train_mean = train.mean(1)
repMean = ml.repmat(train_mean, 60, 1)
transMean = np.transpose(repMean)

train = train - transMean

#DO SVD
u ,s ,v = la.svd(train)
print("SVD done")

K = [ 1, 2, 3, 6, 10 ,20 ,30]


for rank in K:
	hitrate = 0;
	total = 0;
	subNum = []
	minimum = []
	
	sub = (u[0 : k, :])
	sub = np.transpose(u[:, 0 : k]
	proj = sub.dot(train)	
	
	for image in testing:
		total += 1
		
		img2 = cv2.imread(image)
		img2 = img2[:, :, 2]
		img2 = img2.flatten()
		img2 -= train_mean

		projection = sub.dot(img2)
		repTest = np.transpose(ml.repmat(projection, 60, 1))	
		
		norMol = repTest - proj
		norm = la.norm(norMol, axis = 0)
		kNeighbors =  np.argsort(norm)
		minInd = kNeighbors.argsort()

		minInd = minInd.tolist()

		for index in minInd:
			if index < rank:
				minimum.append(minIndex.index(index))
		
		for index in minimum:
			sumNum.append(int(index / 6) + 1)

		find_pred = Counter(sumNum)
		mostNum = max(find_pred.items(), key = operator.itemgetter(1))[0]

		if(int(os.path.basename(os.path.split(image)[0])[1:]) == mostNum):
			hit += 1

	# Find recognition accuracy rate for different K values
	hitrate = hit / total
	print("The Rank " + rank + "\t Hitrate: " + hitrate)				
	
##Demo Purposes
#path = '/home/echeng/Documents/COEN166/Lab5/att_faces_10/att_faces_10/s1/1.pgm'
#img = cv2.imread(path)

#cv2.imshow('image', img)
#cv2.waitKey(0)
