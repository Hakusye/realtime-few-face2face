import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg',fps=2):
	cap = cv2.VideoCapture(video_path)
	if not cap.isOpened():
		return
	os.makedirs(dir_path, exist_ok=True)
	base_path = os.path.join(dir_path, basename)
	digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
	n = 0
	while True:
		if n==fps*100:
			break
		ret, frame = cap.read()
		if ret and ((n % fps) == 0):
			cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
		else:
			return
		n += 1

#save_all_frames('data/temp/sample_video.mp4', 'data/temp/result', 'sample_video_img','png',3)

if __name__ == "__main__":
	mp4path = "datasets/manipulated_sequences/videos/" #相対
	resultpath = "datasets/manipulated_sequences/vid2images/" #相対

	mp4files = os.listdir(mp4path)
	for path in mp4files:
		if not os.path.isdir(resultpath+path[:-4]):
			print("mkdir:"+resultpath+path[:-4])
			os.mkdir(resultpath+path[:-4])
		save_all_frames(mp4path+path, resultpath+path[:-4], '','png',1)
		print("saving"+path[:-4])
