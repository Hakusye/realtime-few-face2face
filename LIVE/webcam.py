## few-shot-vid2vidディレクトリから実行する

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import torch
import time
import cv2 
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import glob
from skimage import io
import concurrent.futures

## フォルダ検索で詰まっている状態(メモリが非同期なのでグローバル変数は参照できない)
def synthesize():
	


if __name__ == '__main__':
	### カメラの前処理
	#base_path = '~/Shirae/vid2vid/few-shot-vid2vid/Record/datasets/train_images/000/'
	base_path = 'Record/datasets/record_images/'
	start_time = time.time()
	ext = '.png'
	cap = cv2.VideoCapture(0)
	num = 0 #ここはマルチプロセスでも使い続けるので扱いに気をつける
	cnt=0
	executor = concurrent.futures.ProcessPoolExecutor(max_workers=15)
	executor.submit(output) #画像をqueueで管理.emptyでモナリザの静止画を出力.
	### ほんへ
	while True:
		cnt+=1
		ret,frame = cap.read()
		cv2.imshow('GPU',frame)
		if ret and (cnt%2 == 0):
			## num+1は非同期処理の不安定さを解消するため
			print(base_path+(num+1).zfill(3)+"/"+str(cnt)+ext) ## フォルダ位置
			cv2.imwrite(base_path+str(cnt)+ext,frame)
		if(time.time()-start_time>5):
			num+=1
			executor.submit(synthesize) ## 書き途中
			start_time = time.time()
			cnt=0-

			
	cap.release()
	cv2.destroyAllWindows()
