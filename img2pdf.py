from PIL import Image
import os
import sys
if(len(sys.argv)<3):
	print("Execute in the format python  name.py  pg_count  pdf_name_with_extension")
	exit()

pwd = os.getcwd()
#########enter the no of pages#####
#pg_count=19
#print(sys.argv[0],type(sys.argv[0]),type(int(sys.argv[0])))

pg_count=int(sys.argv[1])

#####PDF name here####

name=str(sys.argv[2])

#name="hello.pdf"
######################
img_name_list=[]

for i in range(1,pg_count+1):
	img_name_list.append(str(i) + ".png")

imglist=[]
flag=1
im1=Image.open(pwd + "\\" + img_name_list[0])

for img in img_name_list:
	if(flag==1):
		flag=0
		continue
	tmp_img=Image.open(pwd + "\\" + img)
	imglist.append(tmp_img)

pdf1_filename = pwd +"\\"+ name

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=imglist)
