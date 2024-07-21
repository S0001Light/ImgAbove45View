# scs_GLIMPSE_ImgAbove45View_renamed_7-20-2024
# made awhile back, python and pygame must be installed.
# change and search ####(#) below, to view more than 45 photos in viewer none lesser,
# z and x
# on keyboard backwards and forwards
# Q, W, A, S _ Rotate View of All...
# to view images made by my site, https://www.writersjumbler.com/ , or others images
# just as viewer at that size only, for now...

import sys
import os
import pygame
from pygame.locals import *

pygame.init()

backgroundSize = (1800, 1000)
screen01 = pygame.display.set_mode(backgroundSize, RESIZABLE, 32)

surface00 = pygame.Surface((200,200))
surface01 = pygame.Surface((200,200))
surface02 = pygame.Surface((200,200))
surface03 = pygame.Surface((200,200))
surface04 = pygame.Surface((200,200))
surface05 = pygame.Surface((200,200))
surface06 = pygame.Surface((200,200))
surface07 = pygame.Surface((200,200))
surface08 = pygame.Surface((200,200))
surface09 = pygame.Surface((200,200))
surface10 = pygame.Surface((200,200))
surface11 = pygame.Surface((200,200))
surface12 = pygame.Surface((200,200))
surface13 = pygame.Surface((200,200))
surface14 = pygame.Surface((200,200))
surface15 = pygame.Surface((200,200))
surface16 = pygame.Surface((200,200))
surface17 = pygame.Surface((200,200))
surface18 = pygame.Surface((200,200))
surface19 = pygame.Surface((200,200))
surface20 = pygame.Surface((200,200))
surface21 = pygame.Surface((200,200))
surface22 = pygame.Surface((200,200))
surface23 = pygame.Surface((200,200))
surface24 = pygame.Surface((200,200))
surface25 = pygame.Surface((200,200))
surface26 = pygame.Surface((200,200))
surface27 = pygame.Surface((200,200))
surface28 = pygame.Surface((200,200))
surface29 = pygame.Surface((200,200))
surface30 = pygame.Surface((200,200))
surface31 = pygame.Surface((200,200))
surface32 = pygame.Surface((200,200))
surface33 = pygame.Surface((200,200))
surface34 = pygame.Surface((200,200))
surface35 = pygame.Surface((200,200))
surface36 = pygame.Surface((200,200))
surface37 = pygame.Surface((200,200))
surface38 = pygame.Surface((200,200))
surface39 = pygame.Surface((200,200))
surface40 = pygame.Surface((200,200))
surface41 = pygame.Surface((200,200))
surface42 = pygame.Surface((200,200))
surface43 = pygame.Surface((200,200))
surface44 = pygame.Surface((200,200))

#artPhotos = '?C:/Pictures/'
files = []
files = os.listdir(artPhotos)
listLength = len(files)
print(listLength)
files00 = str()
scsTechfiles01 = str()
files02 = str()
files03 = str()
files04 = str()
files05 = str()
files06 = str()
files07 = str()
files08 = str()
files09 = str()
files10 = str()
files11 = str()
files12 = str()
files13 = str()
files14 = str()
files15 = str()
files16 = str()
files17 = str()
files18 = str()
files19 = str()
files20 = str()
files21 = str()
files22 = str()
files23 = str()
files24 = str()
files25 = str()
files26 = str()
files27 = str()
files28 = str()
files29 = str()
files30 = str()
files31 = str()
files32 = str()
files33 = str()
files34 = str()
files35 = str()
files36 = str()
files37 = str()
files38 = str()
files39 = str()
files40 = str()
files41 = str()
files42 = str()
files43 = str()
files44 = str()

agZ = 0
rotate0 = 0.
rotate1 = 90.
rotate2 = 180.
rotate3 = -90.
rotateAt = 360.
if agZ in range(0, listLength):
    files00 = artPhotos + files[agZ]
    files01 = artPhotos + files[agZ + 1]
    files02 = artPhotos + files[agZ + 2]
    files03 = artPhotos + files[agZ + 3]
    files04 = artPhotos + files[agZ + 4]
    files05 = artPhotos + files[agZ + 5]
    files06 = artPhotos + files[agZ + 6]
    files07 = artPhotos + files[agZ + 7]
    files08 = artPhotos + files[agZ + 8]
    files09 = artPhotos + files[agZ + 9]
    files10 = artPhotos + files[agZ + 10]
    files11 = artPhotos + files[agZ + 11]
    files12 = artPhotos + files[agZ + 12]
    files13 = artPhotos + files[agZ + 13]
    files14 = artPhotos + files[agZ + 14]
    files15 = artPhotos + files[agZ + 15]
    files16 = artPhotos + files[agZ + 16]
    files17 = artPhotos + files[agZ + 17]
    files18 = artPhotos + files[agZ + 18]
    files19 = artPhotos + files[agZ + 19]
    files20 = artPhotos + files[agZ + 20]
    files21 = artPhotos + files[agZ + 21]
    files22 = artPhotos + files[agZ + 22]
    files23 = artPhotos + files[agZ + 23]
    files24 = artPhotos + files[agZ + 24]
    files25 = artPhotos + files[agZ + 25]
    files26 = artPhotos + files[agZ + 26]
    files27 = artPhotos + files[agZ + 27]
    files28 = artPhotos + files[agZ + 28]
    files29 = artPhotos + files[agZ + 29]
    files30 = artPhotos + files[agZ + 30]
    files31 = artPhotos + files[agZ + 31]
    files32 = artPhotos + files[agZ + 32]
    files33 = artPhotos + files[agZ + 33]
    files34 = artPhotos + files[agZ + 34]
    files35 = artPhotos + files[agZ + 35]
    files36 = artPhotos + files[agZ + 36]
    files37 = artPhotos + files[agZ + 37]
    files38 = artPhotos + files[agZ + 38]
    files39 = artPhotos + files[agZ + 39]
    files40 = artPhotos + files[agZ + 40]
    files41 = artPhotos + files[agZ + 41]
    files42 = artPhotos + files[agZ + 42]
    files43 = artPhotos + files[agZ + 43]
    files44 = artPhotos + files[agZ + 44]
    print(files00)
    print(files01)
    print(files02)
    print(files03)
    print(files04)
    print(files05)
    print(files06)
    print(files07)
    print(files08)
    print(files09)
    print(files10)
    print(files11)
    print(files12)
    print(files13)
    print(files14)
    print(files15)
    print(files16)
    print(files17)
    print(files18)
    print(files19)
    print(files20)
    print(files21)
    print(files22)
    print(files23)
    print(files24)
    print(files25)
    print(files26)
    print(files27)
    print(files28)
    print(files29)
    print(files30)
    print(files31)
    print(files32)
    print(files33)
    print(files34)
    print(files35)
    print(files36)
    print(files37)
    print(files38)
    print(files39)
    print(files40)
    print(files41)
    print(files42)
    print(files43)
    print(files44)

while True:
    pressedKey = pygame.key.get_pressed()
    directionToRotate = 0.
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pressedKey[K_q]:
            rotate0 = directionToRotate * rotateAt + 0.0
            rotate1 = directionToRotate * rotateAt + 0.0
            rotate2 = directionToRotate * rotateAt + 0.0
            rotate3 = directionToRotate * rotateAt + 0.0
        if pressedKey[K_w]:
            rotate0 = directionToRotate * rotateAt + 180.0
            rotate1 = directionToRotate * rotateAt + 180.0
            rotate2 = directionToRotate * rotateAt + 180.0
            rotate3 = directionToRotate * rotateAt + 180.0
        if pressedKey[K_s]:
            rotate0 = directionToRotate * rotateAt - 90.0
            rotate1 = directionToRotate * rotateAt - 90.0
            rotate2 = directionToRotate * rotateAt - 90.0
            rotate3 = directionToRotate * rotateAt - 90.0
        if pressedKey[K_a]:
            rotate0 = directionToRotate * rotateAt + 90.0
            rotate1 = directionToRotate * rotateAt + 90.0
            rotate2 = directionToRotate * rotateAt + 90.0
            rotate3 = directionToRotate * rotateAt + 90.0
            
        if pressedKey[K_z]:
            if agZ in range(0, listLength):
                if agZ < listLength:
                    agZ = agZ + -1
                    print(agZ)
                    if agZ <= -1:
                        agZ = listLength + -1
                        print(agZ)
            files00 = artPhotos + files[agZ]
            files01 = artPhotos + files[agZ - 1]
            files02 = artPhotos + files[agZ - 2]
            files03 = artPhotos + files[agZ - 3]
            files04 = artPhotos + files[agZ - 4]
            files05 = artPhotos + files[agZ - 5]
            files06 = artPhotos + files[agZ - 6]
            files07 = artPhotos + files[agZ - 7]
            files08 = artPhotos + files[agZ - 8]
            files09 = artPhotos + files[agZ - 9]
            files10 = artPhotos + files[agZ - 10]
            files11 = artPhotos + files[agZ - 11]
            files12 = artPhotos + files[agZ - 12]
            files13 = artPhotos + files[agZ - 13]
            files14 = artPhotos + files[agZ - 14]
            files15 = artPhotos + files[agZ - 15]
            files16 = artPhotos + files[agZ - 16]
            files17 = artPhotos + files[agZ - 17]
            files18 = artPhotos + files[agZ - 18]
            files19 = artPhotos + files[agZ - 19]
            files20 = artPhotos + files[agZ - 20]
            files21 = artPhotos + files[agZ - 21]
            files22 = artPhotos + files[agZ - 22]
            files23 = artPhotos + files[agZ - 23]
            files24 = artPhotos + files[agZ - 24]
            files25 = artPhotos + files[agZ - 25]
            files26 = artPhotos + files[agZ - 26]
            files27 = artPhotos + files[agZ - 27]
            files28 = artPhotos + files[agZ - 28]
            files29 = artPhotos + files[agZ - 29]
            files30 = artPhotos + files[agZ - 30]
            files31 = artPhotos + files[agZ - 31]
            files32 = artPhotos + files[agZ - 32]
            files33 = artPhotos + files[agZ - 33]
            files34 = artPhotos + files[agZ - 34]
            files35 = artPhotos + files[agZ - 35]
            files36 = artPhotos + files[agZ - 36]
            files37 = artPhotos + files[agZ - 37]
            files38 = artPhotos + files[agZ - 38]
            files39 = artPhotos + files[agZ - 39]
            files40 = artPhotos + files[agZ - 40]
            files41 = artPhotos + files[agZ - 41]
            files42 = artPhotos + files[agZ - 42]
            files43 = artPhotos + files[agZ - 43]
            files44 = artPhotos + files[agZ - 44]
            print(files01)
            
        if pressedKey[K_x]:
            if agZ in range(0, listLength):
                if agZ < listLength:
                    agZ = agZ + 1
                    print(agZ)
                    if agZ == listLength:
                        agZ = 0 + 1
                        print(agZ)
            files00 = artPhotos + files[agZ]
            files01 = artPhotos + files[agZ + 1]
            files02 = artPhotos + files[agZ + 2]
            files03 = artPhotos + files[agZ + 3]
            files04 = artPhotos + files[agZ + 4]
            files05 = artPhotos + files[agZ + 5]
            files06 = artPhotos + files[agZ + 6]
            files07 = artPhotos + files[agZ + 7]
            files08 = artPhotos + files[agZ + 8]
            files09 = artPhotos + files[agZ + 9]
            files10 = artPhotos + files[agZ + 10]
            files11 = artPhotos + files[agZ + 11]
            files12 = artPhotos + files[agZ + 12]
            files13 = artPhotos + files[agZ + 13]
            files14 = artPhotos + files[agZ + 14]
            files15 = artPhotos + files[agZ + 15]
            files16 = artPhotos + files[agZ + 16]
            files17 = artPhotos + files[agZ + 17]
            files18 = artPhotos + files[agZ + 18]
            files19 = artPhotos + files[agZ + 19]
            files20 = artPhotos + files[agZ + 20]
            files21 = artPhotos + files[agZ + 21]
            files22 = artPhotos + files[agZ + 22]
            files23 = artPhotos + files[agZ + 23]
            files24 = artPhotos + files[agZ + 24]
            files25 = artPhotos + files[agZ + 25]
            files26 = artPhotos + files[agZ + 26]
            files27 = artPhotos + files[agZ + 27]
            files28 = artPhotos + files[agZ + 28]
            files29 = artPhotos + files[agZ + 29]
            files30 = artPhotos + files[agZ + 30]
            files31 = artPhotos + files[agZ + 31]
            files32 = artPhotos + files[agZ + 32]
            files33 = artPhotos + files[agZ + 33]
            files34 = artPhotos + files[agZ + 34]
            files35 = artPhotos + files[agZ + 35]
            files36 = artPhotos + files[agZ + 36]
            files37 = artPhotos + files[agZ + 37]
            files38 = artPhotos + files[agZ + 38]
            files39 = artPhotos + files[agZ + 39]
            files40 = artPhotos + files[agZ + 40]
            files41 = artPhotos + files[agZ + 41]
            files42 = artPhotos + files[agZ + 42]
            files43 = artPhotos + files[agZ + 43]
            files44 = artPhotos + files[agZ + 44]
            print(files01)
    
    sprite00 = pygame.image.load(files00).convert_alpha()
    sprite01 = pygame.image.load(files01).convert_alpha()
    sprite02 = pygame.image.load(files02).convert_alpha()
    sprite03 = pygame.image.load(files03).convert_alpha()
    sprite04 = pygame.image.load(files04).convert_alpha()
    sprite05 = pygame.image.load(files05).convert_alpha()
    sprite06 = pygame.image.load(files06).convert_alpha()
    sprite07 = pygame.image.load(files07).convert_alpha()
    sprite08 = pygame.image.load(files08).convert_alpha()
    sprite09 = pygame.image.load(files09).convert_alpha()
    sprite10 = pygame.image.load(files10).convert_alpha()
    sprite11 = pygame.image.load(files11).convert_alpha()
    sprite12 = pygame.image.load(files12).convert_alpha()
    sprite13 = pygame.image.load(files13).convert_alpha()
    sprite14 = pygame.image.load(files14).convert_alpha()
    sprite15 = pygame.image.load(files15).convert_alpha()
    sprite16 = pygame.image.load(files16).convert_alpha()
    sprite17 = pygame.image.load(files17).convert_alpha()
    sprite18 = pygame.image.load(files18).convert_alpha()
    sprite19 = pygame.image.load(files19).convert_alpha()
    sprite20 = pygame.image.load(files20).convert_alpha()
    sprite21 = pygame.image.load(files21).convert_alpha()
    sprite22 = pygame.image.load(files22).convert_alpha()
    sprite23 = pygame.image.load(files23).convert_alpha()
    sprite24 = pygame.image.load(files24).convert_alpha()
    sprite25 = pygame.image.load(files25).convert_alpha()
    sprite26 = pygame.image.load(files26).convert_alpha()
    sprite27 = pygame.image.load(files27).convert_alpha()
    sprite28 = pygame.image.load(files28).convert_alpha()
    sprite29 = pygame.image.load(files29).convert_alpha()
    sprite30 = pygame.image.load(files30).convert_alpha()
    sprite31 = pygame.image.load(files31).convert_alpha()
    sprite32 = pygame.image.load(files32).convert_alpha()
    sprite33 = pygame.image.load(files33).convert_alpha()
    sprite34 = pygame.image.load(files34).convert_alpha()
    sprite35 = pygame.image.load(files35).convert_alpha()
    sprite36 = pygame.image.load(files36).convert_alpha()
    sprite37 = pygame.image.load(files37).convert_alpha()
    sprite38 = pygame.image.load(files38).convert_alpha()
    sprite39 = pygame.image.load(files39).convert_alpha()
    sprite40 = pygame.image.load(files40).convert_alpha()
    sprite41 = pygame.image.load(files41).convert_alpha()
    sprite42 = pygame.image.load(files42).convert_alpha()
    sprite43 = pygame.image.load(files43).convert_alpha()
    sprite44 = pygame.image.load(files44).convert_alpha()
    w = int(200)
    h = int(200)
    scsImage00 = pygame.transform.scale(sprite00,(w,h))
    scsImage01 = pygame.transform.scale(sprite01,(w,h))
    scsImage02 = pygame.transform.scale(sprite02,(w,h))
    scsImage03 = pygame.transform.scale(sprite03,(w,h))
    scsImage04 = pygame.transform.scale(sprite04,(w,h))
    scsImage05 = pygame.transform.scale(sprite05,(w,h))
    scsImage06 = pygame.transform.scale(sprite06,(w,h))
    scsImage07 = pygame.transform.scale(sprite07,(w,h))
    scsImage08 = pygame.transform.scale(sprite08,(w,h))
    scsImage09 = pygame.transform.scale(sprite09,(w,h))
    scsImage10 = pygame.transform.scale(sprite10,(w,h))
    scsImage11 = pygame.transform.scale(sprite11,(w,h))
    scsImage12 = pygame.transform.scale(sprite12,(w,h))
    scsImage13 = pygame.transform.scale(sprite13,(w,h))
    scsImage14 = pygame.transform.scale(sprite14,(w,h))
    scsImage15 = pygame.transform.scale(sprite15,(w,h))
    scsImage16 = pygame.transform.scale(sprite16,(w,h))
    scsImage17 = pygame.transform.scale(sprite17,(w,h))
    scsImage18 = pygame.transform.scale(sprite18,(w,h))
    scsImage19 = pygame.transform.scale(sprite19,(w,h))
    scsImage20 = pygame.transform.scale(sprite20,(w,h))
    scsImage21 = pygame.transform.scale(sprite21,(w,h))
    scsImage22 = pygame.transform.scale(sprite22,(w,h))
    scsImage23 = pygame.transform.scale(sprite23,(w,h))
    scsImage24 = pygame.transform.scale(sprite24,(w,h))
    scsImage25 = pygame.transform.scale(sprite25,(w,h))
    scsImage26 = pygame.transform.scale(sprite26,(w,h))
    scsImage27 = pygame.transform.scale(sprite27,(w,h))
    scsImage28 = pygame.transform.scale(sprite28,(w,h))
    scsImage29 = pygame.transform.scale(sprite29,(w,h))
    scsImage30 = pygame.transform.scale(sprite30,(w,h))
    scsImage31 = pygame.transform.scale(sprite31,(w,h))
    scsImage32 = pygame.transform.scale(sprite32,(w,h))
    scsImage33 = pygame.transform.scale(sprite33,(w,h))
    scsImage34 = pygame.transform.scale(sprite34,(w,h))
    scsImage35 = pygame.transform.scale(sprite35,(w,h))
    scsImage36 = pygame.transform.scale(sprite36,(w,h))
    scsImage37 = pygame.transform.scale(sprite37,(w,h))
    scsImage38 = pygame.transform.scale(sprite38,(w,h))
    scsImage39 = pygame.transform.scale(sprite39,(w,h))
    scsImage40 = pygame.transform.scale(sprite40,(w,h))
    scsImage41 = pygame.transform.scale(sprite41,(w,h))
    scsImage42 = pygame.transform.scale(sprite42,(w,h))
    scsImage43 = pygame.transform.scale(sprite43,(w,h))
    scsImage44 = pygame.transform.scale(sprite44,(w,h))
    rotateSprite00 = pygame.transform.rotate(scsImage00, (rotate0))
    rotateSprite01 = pygame.transform.rotate(scsImage01, (rotate0))
    rotateSprite02 = pygame.transform.rotate(scsImage02, (rotate0))
    rotateSprite03 = pygame.transform.rotate(scsImage03, (rotate0))
    rotateSprite04 = pygame.transform.rotate(scsImage04, (rotate0))
    rotateSprite05 = pygame.transform.rotate(scsImage05, (rotate0))
    rotateSprite06 = pygame.transform.rotate(scsImage06, (rotate0))
    rotateSprite07 = pygame.transform.rotate(scsImage07, (rotate0))
    rotateSprite08 = pygame.transform.rotate(scsImage08, (rotate0))
    rotateSprite09 = pygame.transform.rotate(scsImage09, (rotate0))
    rotateSprite10 = pygame.transform.rotate(scsImage10, (rotate0))
    rotateSprite11 = pygame.transform.rotate(scsImage11, (rotate0))
    rotateSprite12 = pygame.transform.rotate(scsImage12, (rotate0))
    rotateSprite13 = pygame.transform.rotate(scsImage13, (rotate0))
    rotateSprite14 = pygame.transform.rotate(scsImage14, (rotate0))
    rotateSprite15 = pygame.transform.rotate(scsImage15, (rotate0))
    rotateSprite16 = pygame.transform.rotate(scsImage16, (rotate0))
    rotateSprite17 = pygame.transform.rotate(scsImage17, (rotate0))
    rotateSprite18 = pygame.transform.rotate(scsImage18, (rotate0))
    rotateSprite19 = pygame.transform.rotate(scsImage19, (rotate0))
    rotateSprite20 = pygame.transform.rotate(scsImage20, (rotate0))
    rotateSprite21 = pygame.transform.rotate(scsImage21, (rotate0))
    rotateSprite22 = pygame.transform.rotate(scsImage22, (rotate0))
    rotateSprite23 = pygame.transform.rotate(scsImage23, (rotate0))
    rotateSprite24 = pygame.transform.rotate(scsImage24, (rotate0))
    rotateSprite25 = pygame.transform.rotate(scsImage25, (rotate0))
    rotateSprite26 = pygame.transform.rotate(scsImage26, (rotate0))
    rotateSprite27 = pygame.transform.rotate(scsImage27, (rotate0))
    rotateSprite28 = pygame.transform.rotate(scsImage28, (rotate0))
    rotateSprite29 = pygame.transform.rotate(scsImage29, (rotate0))
    rotateSprite30 = pygame.transform.rotate(scsImage30, (rotate0))
    rotateSprite31 = pygame.transform.rotate(scsImage31, (rotate0))
    rotateSprite32 = pygame.transform.rotate(scsImage32, (rotate0))
    rotateSprite33 = pygame.transform.rotate(scsImage33, (rotate0))
    rotateSprite34 = pygame.transform.rotate(scsImage34, (rotate0))
    rotateSprite35 = pygame.transform.rotate(scsImage35, (rotate0))
    rotateSprite36 = pygame.transform.rotate(scsImage36, (rotate0))
    rotateSprite37 = pygame.transform.rotate(scsImage37, (rotate0))
    rotateSprite38 = pygame.transform.rotate(scsImage38, (rotate0))
    rotateSprite39 = pygame.transform.rotate(scsImage39, (rotate0))
    rotateSprite40 = pygame.transform.rotate(scsImage40, (rotate0))
    rotateSprite41 = pygame.transform.rotate(scsImage41, (rotate0))
    rotateSprite42 = pygame.transform.rotate(scsImage42, (rotate0))
    rotateSprite43 = pygame.transform.rotate(scsImage43, (rotate0))
    rotateSprite44 = pygame.transform.rotate(scsImage44, (rotate0))
    space00 = Rect(0,0,200,200)
    space01 = Rect(0,0,200,200)
    space02 = Rect(0,0,200,200)
    space03 = Rect(0,0,200,200)
    space04 = Rect(0,0,200,200)
    space05 = Rect(0,0,200,200)
    space06 = Rect(0,0,200,200)
    space07 = Rect(0,0,200,200)
    space08 = Rect(0,0,200,200)
    space09 = Rect(0,0,200,200)
    space10 = Rect(0,0,200,200)
    space11 = Rect(0,0,200,200)
    space12 = Rect(0,0,200,200)
    space13 = Rect(0,0,200,200)
    space14 = Rect(0,0,200,200)
    space15 = Rect(0,0,200,200)
    space16 = Rect(0,0,200,200)
    space17 = Rect(0,0,200,200)
    space18 = Rect(0,0,200,200)
    space19 = Rect(0,0,200,200)
    space20 = Rect(0,0,200,200)
    space21 = Rect(0,0,200,200)
    space22 = Rect(0,0,200,200)
    space23 = Rect(0,0,200,200)
    space24 = Rect(0,0,200,200)
    space25 = Rect(0,0,200,200)
    space26 = Rect(0,0,200,200)
    space27 = Rect(0,0,200,200)
    space28 = Rect(0,0,200,200)
    space29 = Rect(0,0,200,200)
    space30 = Rect(0,0,200,200)
    space31 = Rect(0,0,200,200)
    space32 = Rect(0,0,200,200)
    space33 = Rect(0,0,200,200)
    space34 = Rect(0,0,200,200)
    space35 = Rect(0,0,200,200)
    space36 = Rect(0,0,200,200)
    space37 = Rect(0,0,200,200)
    space38 = Rect(0,0,200,200)
    space39 = Rect(0,0,200,200)
    space40 = Rect(0,0,200,200)
    space41 = Rect(0,0,200,200)
    space42 = Rect(0,0,200,200)
    space43 = Rect(0,0,200,200)
    space44 = Rect(0,0,200,200)
    srotatebSprite00 = rotateSprite00.subsurface(space00)
    srotatebSprite01 = rotateSprite01.subsurface(space01)
    srotatebSprite02 = rotateSprite02.subsurface(space02)
    srotatebSprite03 = rotateSprite03.subsurface(space03)
    srotatebSprite04 = rotateSprite04.subsurface(space04)
    srotatebSprite05 = rotateSprite05.subsurface(space05)
    srotatebSprite06 = rotateSprite06.subsurface(space06)
    srotatebSprite07 = rotateSprite07.subsurface(space07)
    srotatebSprite08 = rotateSprite08.subsurface(space08)
    srotatebSprite09 = rotateSprite09.subsurface(space09)
    srotatebSprite10 = rotateSprite10.subsurface(space10)
    srotatebSprite11 = rotateSprite11.subsurface(space11)
    srotatebSprite12 = rotateSprite12.subsurface(space12)
    srotatebSprite13 = rotateSprite13.subsurface(space13)
    srotatebSprite14 = rotateSprite14.subsurface(space14)
    srotatebSprite15 = rotateSprite15.subsurface(space15)
    srotatebSprite16 = rotateSprite16.subsurface(space16)
    srotatebSprite17 = rotateSprite17.subsurface(space17)
    srotatebSprite18 = rotateSprite18.subsurface(space18)
    srotatebSprite19 = rotateSprite19.subsurface(space19)
    srotatebSprite20 = rotateSprite20.subsurface(space20)
    srotatebSprite21 = rotateSprite21.subsurface(space21)
    srotatebSprite22 = rotateSprite22.subsurface(space22)
    srotatebSprite23 = rotateSprite23.subsurface(space23)
    srotatebSprite24 = rotateSprite24.subsurface(space24)
    srotatebSprite25 = rotateSprite25.subsurface(space25)
    srotatebSprite26 = rotateSprite26.subsurface(space26)
    srotatebSprite27 = rotateSprite27.subsurface(space27)
    srotatebSprite28 = rotateSprite28.subsurface(space28)
    srotatebSprite29 = rotateSprite29.subsurface(space29)
    srotatebSprite30 = rotateSprite30.subsurface(space30)
    srotatebSprite31 = rotateSprite31.subsurface(space31)
    srotatebSprite32 = rotateSprite32.subsurface(space32)
    srotatebSprite33 = rotateSprite33.subsurface(space33)
    srotatebSprite34 = rotateSprite34.subsurface(space34)
    srotatebSprite35 = rotateSprite35.subsurface(space35)
    srotatebSprite36 = rotateSprite36.subsurface(space36)
    srotatebSprite37 = rotateSprite37.subsurface(space37)
    srotatebSprite38 = rotateSprite38.subsurface(space38)
    srotatebSprite39 = rotateSprite39.subsurface(space39)
    srotatebSprite40 = rotateSprite40.subsurface(space40)
    srotatebSprite41 = rotateSprite41.subsurface(space41)
    srotatebSprite42 = rotateSprite42.subsurface(space42)
    srotatebSprite43 = rotateSprite43.subsurface(space43)
    srotatebSprite44 = rotateSprite44.subsurface(space44)
    
    screen01.fill((255,255,255))
    screen01.blit(srotatebSprite00,(0+10, 0+10, 200+10, 200+10))
    screen01.blit(srotatebSprite01,(200+15, 0+10, 200+15, 200+10))
    screen01.blit(srotatebSprite02,(400+20, 0+10, 200+20, 200+10))
    screen01.blit(srotatebSprite03,(600+25, 0+10, 200+25, 200+10))
    screen01.blit(srotatebSprite04,(800+30, 0+10, 200+30, 200+10))
    screen01.blit(srotatebSprite05,(1000+35, 0+10,  200+35, 200+10))
    screen01.blit(srotatebSprite06,(1200+40, 0+10,  200+40, 200+10))
    screen01.blit(srotatebSprite07,(1400+45, 0+10,  200+45, 200+10))
    screen01.blit(srotatebSprite08,(1600+50, 0+10,  200+50, 200+10))
    screen01.blit(srotatebSprite09,(0+10, 200+15,  200+10, 200+15))
    screen01.blit(srotatebSprite10,(200+15, 200+15,  200+15, 200+15))
    screen01.blit(srotatebSprite11,(400+20, 200+15,  200+20, 200+15))
    screen01.blit(srotatebSprite12,(600+25, 200+15,  200+25, 200+15))
    screen01.blit(srotatebSprite13,(800+30, 200+15,  200+30, 200+15))
    screen01.blit(srotatebSprite14,(1000+35, 200+15,  200+35, 200+15))
    screen01.blit(srotatebSprite15,(1200+40, 200+15,  200+40, 200+15))
    screen01.blit(srotatebSprite16,(1400+45, 200+15,  200+45, 200+15))
    screen01.blit(srotatebSprite17,(1600+50, 200+15,  200+50, 200+15))
    screen01.blit(srotatebSprite18,(0+10, 400+20,  200+10, 200+20))
    screen01.blit(srotatebSprite19,(200+15, 400+20,  200+15, 200+20))
    screen01.blit(srotatebSprite20,(400+20, 400+20,  200+20, 200+20))
    screen01.blit(srotatebSprite21,(600+25, 400+20,  200+25, 200+20))
    screen01.blit(srotatebSprite22,(800+30, 400+20,  200+30, 200+20))
    screen01.blit(srotatebSprite23,(1000+35, 400+20,  200+35, 200+20))
    screen01.blit(srotatebSprite24,(1200+40, 400+20,  200+40, 200+20))
    screen01.blit(srotatebSprite25,(1400+45, 400+20,  200+45, 200+20))
    screen01.blit(srotatebSprite26,(1600+50, 400+20,  200+50, 200+20))
    screen01.blit(srotatebSprite27,(0+10, 600+25,  200+10, 200+25))
    screen01.blit(srotatebSprite28,(200+15, 600+25,  200+15, 200+25))
    screen01.blit(srotatebSprite29,(400+20, 600+25,  200+20, 200+25))
    screen01.blit(srotatebSprite30,(600+25, 600+25,  200+25, 200+25))
    screen01.blit(srotatebSprite31,(800+30, 600+25,  200+30, 200+25))
    screen01.blit(srotatebSprite32,(1000+35, 600+25,  200+35, 200+25))
    screen01.blit(srotatebSprite33,(1200+40, 600+25,  200+40, 200+25))
    screen01.blit(srotatebSprite34,(1400+45, 600+25,  200+45, 200+25))
    screen01.blit(srotatebSprite35,(1600+50, 600+25,  200+50, 200+25))
    screen01.blit(srotatebSprite36,(0+10, 800+30,  200+10, 200+30))
    screen01.blit(srotatebSprite37,(200+15, 800+30,  200+15, 200+30))
    screen01.blit(srotatebSprite38,(400+20, 800+30,  200+20, 200+30))
    screen01.blit(srotatebSprite39,(600+25, 800+30,  200+25, 200+30))
    screen01.blit(srotatebSprite40,(800+30, 800+30,  200+30, 200+30))
    screen01.blit(srotatebSprite41,(1000+35, 800+30,  200+35, 200+30))
    screen01.blit(srotatebSprite42,(1200+40, 800+30,  200+40, 200+30))
    screen01.blit(srotatebSprite43,(1400+45, 800+30,  200+45, 200+30))
    screen01.blit(srotatebSprite44,(1600+50, 800+30,  200+50, 200+30))

    pygame.display.update()
