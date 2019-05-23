#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from glob import glob
from PIL import Image
import os
#读取图片文件
source_dir='media'
target_dir='output'
filenames=glob('{}/*'.format(source_dir))
print(len(filenames))
#检测文件大小
# for filename in filenames:
# 	with Image.open(filename) as im:
# 		width,height=im.size
# 		print(filename,width,height,os.path.getsize(filename))
#设定缩放阈值
threshold=0
#检测超限文件
# for filename in filenames:
# 	filesize=os.path.getsize(filename)
# 	if filesize>=threshold:
# 		print(filename)
#设置文件目录
if not os.path.exists(target_dir):
	os.makedirs(target_dir)
for filename in filenames:
	filesize=os.path.getsize(filename)
	if filesize>=threshold:
		print(filename)
		with Image.open(filename) as im:
			width,height=im.size
			new_width=200
			new_height=int(new_width*height*1.0/width)
			#print('adjusted size:', new_width, new_height)
			resized_im=im.resize((new_width,new_height))
			output_filename=filename.replace(source_dir,target_dir)
			resized_im.save(output_filename)