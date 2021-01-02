from PIL import Image
import pyautogui, time
from cv2 import cv2

def drawBlack(width, length):
    for i in range(width):
        j = 0
        while j < length:
            if px[i,j] < treshold:
                while px[i,j] < treshold and j < length - 1:
                    j += 1
                pyautogui.dragTo(x + i, y + j - 1) 
                time.sleep(0.002) 
            if px[i,j] >= treshold:
                while px[i,j] > treshold and j < length - 1:
                    j += 1
                pyautogui.moveTo(x + i, y + j - 1)
                time.sleep(0.002) 
            j += 1


im = Image.open("your link to the image folder")

if (im.mode == "RGB"):
    img = cv2.imread("your link to the image folder")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("your link to the image folder with other file name", imgGray)
    
    im = Image.open("your link to the image folder with other file name")


px = im.load()

print(im.mode)

width = im.size[0]
length = im.size[1]

x = 800
y = 300

time.sleep(2.5)
pyautogui.PAUSE = 0.01

pyautogui.click(800, 300)

treshold = 160
drawBlack(width, length)

cv2.waitKey(0)
