import cmpt120image as c
import random

#1
def recolor(img,color):

 for row in range (len(img)):
     for col in range(len(img)):
         if img[row][col]!=[255,255,255]:
            img[row][col]=color

 return img

#2
def minify(img):
 newI=c.getBlackImage(len(img),len(img))
 a=1
 b=1
 for row in range(0,len(img),2):
  for col in range(0,len(img),2):
      for i in range(2):
          newI[a][b][i]=((img[row][col][i]+img[row][col+1][i]+img[row+1][col][i]+img[row+1][col+1][i])/4)
      b=b+1
  a=a+1
  b=1
 return newI

#3
def mirror(img):
  col_1=int(len(img)/2)
  for row in range(len(img)):
      for col in range(col_1):
           current=img[row][col]
           img[row][col]=img[row][len(img)-col-1]
           img[row][len(img)-1-col]=current

  return img

#4
def getCanvas(w,h):
    return[[[255, 255, 255] for i in range(w)] for j in range(h)]
canvas=getCanvas(800,800)
def drawItem (canvas,item,row,col):
 for i in range(len(item)):
     for j in range(len(item)):
              canvas[row+i][col+j]=item[i][j]
 return canvas

#5
def distributeItems(canvas,item,n):

    for i in range(n):
     rowR=random.randrange(len(item))
     colR=random.randrange(len(item))
     item_draw=drawItem(canvas,item,rowR,colR)
    return item_draw




