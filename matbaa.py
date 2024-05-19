import cv2
import numpy as np
import keyboard
import time
kamera = cv2.VideoCapture(0)
y=240
a=255
b=255
c=255
renk_index = 0
renkler = { "kirmizi":(0, 0, 255),"sari":(0, 255, 255),"Mavi":(255, 0, 0),"Yesil":(0, 255, 0),"turuncu":(10,128,255),"beyaz":(255,255,255)}
gri = False
kenar=False
while True:
    a,b,c = list(renkler.items())[renk_index][1]
    _, kare_1 = kamera.read()
    _, kare_2 = kamera.read()
    if gri:
        kare_1 = cv2.cvtColor(kare_1, cv2.COLOR_RGB2GRAY)
        kare_2 = cv2.cvtColor(kare_2, cv2.COLOR_RGB2GRAY)
        kare_1 = cv2.cvtColor(kare_1, cv2.COLOR_GRAY2RGB)
        kare_2 = cv2.cvtColor(kare_2, cv2.COLOR_GRAY2RGB)
    if kenar:
        kare_1 = cv2.Canny(kare_1, 100,200)
        kare_2 = cv2.Canny(kare_2, 100,200)
        kare_1 = cv2.cvtColor(kare_1, cv2.COLOR_GRAY2RGB)
        kare_2 = cv2.cvtColor(kare_2, cv2.COLOR_GRAY2RGB)
    cv2.line(kare_1, (0,240), (680,240), (a,b,c),1)#yatayqqq
    cv2.line(kare_1, (320, 0), (320, 480),(a,b,c),1)#dikey
    cv2.line(kare_2, (0, 240), (680, 240), (a, b, c), 1)  # yatay
    cv2.line(kare_2, (0, y), (680, y), (a, b, c), 1)  # yatay
    cv2.line(kare_2, (320, 0), (320, 480), (a, b, c), 1)  # dikey
    horizontalAppendedImg = np.hstack((kare_1, kare_2))
    out = cv2.resize(horizontalAppendedImg, (1600, 880), 2, 2, interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow('image', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("image", out)
    cv2.waitKey(1)
    if keyboard.is_pressed("f"):
        cv2.destroyAllWindows()
        kamera.release()
        break
    if keyboard.is_pressed("r"):
        if renk_index == 5:
            renk_index = 0
        else:
            renk_index += 1
    if keyboard.is_pressed("g"):
        if gri:
            time.sleep(0.25)
            gri = False
        else:
            time.sleep(0.25)
            gri = True
    if keyboard.is_pressed("w"):
        y -= 13
    if keyboard.is_pressed("s"):
        y += 13
    if keyboard.is_pressed("k"):
        if kenar:
            kenar=False
        else:
            kenar=True
        pass