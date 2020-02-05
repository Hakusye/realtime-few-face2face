import shutil
import os
import random
random.seed(334)
if __name__ == '__main__':
	org = "datasets/manipulated_sequences/vid2images/"
	org_folders = os.listdir(org)
	topath = "datasets/"
	for org_path in org_folders:
		if(random.random()<0.15):
			if not os.path.isdir(topath+"test_images/"+org_path):
				shutil.copytree(org+org_path,topath+"test_images/"+org_path)
		else:
			if not os.path.isdir(topath+"train_images/"+org_path):
				shutil.copytree(org+org_path,topath+"train_images/"+org_path)
