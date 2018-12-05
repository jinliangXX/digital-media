# encoding: UTF-8
import glob as gb
import cv2

img_path = gb.glob("*.jpeg")
videoWriter = cv2.VideoWriter('result.mp4',
                              cv2.VideoWriter_fourcc(
                                  *'MJPG'), 30, (640, 480))

for path in img_path:
    img = cv2.imread(path)
    img = cv2.resize(img, (640, 480))
    print img.shape
    videoWriter.write(img)
