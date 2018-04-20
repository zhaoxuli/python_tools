# -*- coding: utf-8 -*-
import cv2
import os
import sys
#import numpy as np
# 处理鼠标事件
drawing = False #鼠标按下为真
ix,iy=-1,-1
px,py=-1,-1
class Draw:
    def __init__(self,txt_path):
        self.txt_path = txt_path
    #def draw_rectangle(self,event,x,y,flags,param):
    #    global ix,iy,drawing,px,py
    #    if event == cv2.EVENT_LBUTTONDOWN:
    #        drawing = True
    #        ix,iy=x,y
    #    elif event == cv2.EVENT_MOUSEMOVE:
    #        if drawing == True:
    #            src = cp.copy(self.img)
    #            cv2.rectangle(src,(ix,iy),(x,y),(0,255,0),1)
    #            cv2.imshow('image',src)
    #            px,py=x,y
    #    elif event == cv2.EVENT_LBUTTONUP:
    #        drawing = False
    #        cv2.rectangle(self.img,(ix,iy),(x,y),(0,255,0),0)
    #        px,py=-1,-1

    def draw_circle(self,event,x,y,flags,param):
        global ix,iy,drawing,px,py
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix,iy=x,y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.circle(self.img,(x,y),2,(0,0,255),-1)
            if len(self.points) >= 7:
                cv2.putText(self.img,'The points largger than 7,False!!',
                            ((x-15),y),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,255),1)
            else:
                cv2.putText(self.img,str(self.num),((x-15),y),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,255,0),1)
            self.points.append([x,y])
            self.num = self.num +1
            px,py=-1,-1

    def save_ctx(self,points):
        file = open(self.txt_path,'a')
        ctx = self.img_url.split(os.sep)[-1]
        for  ele in points:
            ctx = ctx + ' '+str(ele)
        ctx = ctx + '\n'
        file.write(ctx)
        file.close


    def run(self,img_url):
        F_next = False
        self.num = 1
        self.points = []
        self.img_url = img_url
        self.img= cv2.imread(img_url)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.draw_circle)

        while(1):
            cv2.imshow('image',self.img)
            k = chr(cv2.waitKey(20) & 255)
            if k == 'q' :
                break
            elif k == 'r':
               self.run(img_url)
               return True
            elif k == 's':
                print self.points
                self.save_ctx(self.points)
                return  True
            elif k == 'n':
                return True
        return F_next

def search_recoder(txt_path):
    f = open(txt_path,'r')
    ctx = f.readlines()
    final = ctx[-1][0:-1]
    img_history =  final.split(' ')[0]
    return  img_history


if __name__ == '__main__':
    i = 0
    img_history  = 0
    #Img_file_path = './Image'
    Img_file_path = sys.argv[1]
    Imgs = os.listdir(Img_file_path)
    txt_path = './'+Img_file_path.split(os.sep)[-1]+'.txt'
    if  os.path.exists(txt_path) :
        img_history = search_recoder(txt_path)
    if img_history == 0:
        i = 0
    else:
        i = Imgs.index(img_history)+1
    draw_class = Draw(txt_path)
    while  (i < len(Imgs)):
        ele = Imgs[i]
        print  i
        print ele
        img_url = Img_file_path +os.sep+ ele
        F_next = draw_class.run(img_url)
        i =i +1
        if F_next == False:
             break















