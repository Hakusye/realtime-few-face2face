import cv2


if __name__ == '__main__':
#    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#    video = cv2.VideoWriter('video.mp4', fourcc, 20.0, (640, 480))
    base_path = "datasets/test_images/004/"
    for i in range(100):
#        img = cv2.imread(base_path+'_{0:03d}.png'.format(i))
        print(base_path+'_{0:03d}.png'.format(i))
#        img = cv2.resize(img, (640,480))
#       video.write(img)
	
#    video.release()
