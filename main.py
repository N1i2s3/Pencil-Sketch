import cv2

image = cv2.imread("3.jpeg")

grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert, (21,21),0)

convert = cv2.bitwise_not(blur)

sketch = cv2.divide(grey_filter, convert, scale=256.0)

cv2.imwrite("Output4.jpeg",sketch)