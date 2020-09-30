# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture('File/16416.mp4')
#
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#
# while(True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()

import numpy as np
import cv2

img = cv2.imread('File/abbi.jpg',cv2.IMREAD_COLOR)
#img=cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
cv2.line(img,(0,0),(150,150),(255,255,255),15)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()