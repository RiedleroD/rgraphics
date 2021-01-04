import rgraphics as rgr
import os
import random
import asyncio
fp=rgr.FpsLimiter()
shds=rgr.Shades()
colr=rgr.Color()
Px=rgr.Px
screen=rgr.Graphic(width=300,height=100,bg=Px(shade=shds.d))
content=[]
objlist=["","","",""]
for shade in shds.shades(let=True,shds=False):
	precontent=[]
	for color in colr.colrs():
		precontent.append(Px(color,shade))
	content.append(precontent)
objlist[1]=rgr.Graphic(content=content,posx=random.randrange(5,75),posy=random.randrange(5,30),speedx=1,speedy=1)
content=[]
for shade in shds.shades(let=False):
	precontent=[]
	for color in colr.colrs():
		precontent.append(Px(color,shade))
	content.append(precontent)
objlist[0]=rgr.Graphic(content=content,posx=random.randrange(5,75),posy=random.randrange(5,30),speedy=1,speedx=0)
objlist[2]=rgr.Graphic(width=4,height=4,posx=random.randrange(5,75),posy=random.randrange(5,30),speedy=1,speedx=0)
fps=0
n=0
try:
	while True:
		fp.start()
		objlist[1].move()
		objlist[1].stayin(screen,1)
		objlist[0].move()
		objlist[0].stayin(objlist[1],1)
		objlist[0].stayin(screen,1)
		screen.draw(objlist[1])
		screen.draw(objlist[0],offx=objlist[1].posx-2,offy=objlist[1].posy-1)
		screen.display()
		fps+=fp.end(counter=True)
		n+=1
except KeyboardInterrupt:
	pass
finally:
	if n>0:
		fps/=n
	else:
		fps=0
	os.system("reset")
	print("Average fps:",fps)
