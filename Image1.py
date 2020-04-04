import cv2
#image 1
image1=cv2.imread('ManimaranB.jpg',0)
#image 2
image2=cv2.imread('ManimaranB.jpg',0)
#image compare
cv2.imshow('Image 1',image1)
cv2.waitKey(0)
cv2.imshow('Image 2',image2)
cv2.waitKey(0)
result=cv2.matchTemplate(image1,image2,cv2.TM_CCOEFF_NORMED)
print(result)
if result<=0.8:
	print('Not matched')
else:
	print('Images are matching')
