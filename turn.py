#项目名称：·········································植保机器人路径导航······································
#时   间：·········································2021、10、22··········································
#程序编写：·············································朱玉垒············································
#地   点：··································· 北京工业大学科学楼1037·······································
#作   用：····························本程序作为合成视频专用，将图片转换为视频·································



import os
import cv2
import numpy as np

path = '/home/zyl/wheel_2021/result/5/image/'
filelist = os.listdir(path)
filelist.sort()
print(filelist)

fps = 12.5 #视频每秒24帧
size = (1280,720) #需要转为视频的图片的尺寸
#可以使用cv2.resize()进行修改

video = cv2.VideoWriter("images_003.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
#视频保存在当前目录下

for item in filelist:
    if item.endswith('.png'): 
    #找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
