from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import torch
import time
import cv2 
import os
import glob
from skimage import io
import dlib
import sys
### 特徴量抽出class
### あとで分割する可能性大
class Make_keypoints:
	def __init__(self): ##mydatasetsは後で作る
		self.dataset_path = 'LIVE/result/' ##後にモナリザをいれる
		self.predictor_path = os.path.join(self.dataset_path, 'shape_predictor_68_face_landmarks.dat')
		self.detector = dlib.get_frontal_face_detector()
		self.predictor = dlib.shape_predictor(self.predictor_path)
		self.save_path = self.dataset_path + "org_keypoints/"
		self.points = None
	def calc(self,img):
		#img = io.imread(img_name) ##直接画像を送りたい
		dets = self.detector(img, 1)
		ok = False
		if len(dets) > 0:
			shape = self.predictor(img, dets[0])
			self.points = np.empty([68, 2], dtype=int)
			ok = True
			#b = [i for i in range(68)]
			#self.points[:,0] = shape.part(b).x
			#self.points[:,1] = shape.part(b).y #こんな感じのことがしたい

			for b in range(68): ## おそらくこの処理がネックになってる。完成したらここ治す
				self.points[b,0] = shape.part(b).x
				self.points[b,1] = shape.part(b).y
		#save_name = os.path.join(self.save_path, 'result.txt')
		if(ok):
			np.savetxt(self.save_path+'result.txt', self.points, fmt='%d', delimiter=',')

