from PIL import Image
import pyautogui, time

def drawColor(width, length):
    for i in range(width):
        j = 0
        while j < length:
            if px[i,j][0:] < treshold:
                while px[i,j][0:] < treshold and j < length - 1:
                    j += 1
                pyautogui.dragTo(x + i, y + j - 1) 
                time.sleep(0.002) 
            if px[i,j][0:] >= treshold:
                while px[i,j][0:] > treshold and j < length - 1:
                    j += 1
                pyautogui.moveTo(x + i, y + j - 1)
                time.sleep(0.002) 
            j += 1

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


im = Image.open("C:\\Emil\\Proiecte\\Python\\Proiecte_Python\\Automation\\AutoDrawing\\monablack.jpg")
px = im.load()

width = im.size[0]
length = im.size[1]

x = 800
y = 300

time.sleep(2.5)
pyautogui.PAUSE = 0.01

pyautogui.click(800, 300)

if(im.mode == 'RGB'):
    treshold = (160, 160, 160)
    drawColor(width, length)
else:
    treshold = 160
    drawBlack(width, length)
