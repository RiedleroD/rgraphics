import rgraphics
import os
import random
import asyncio
#rgraphics.intro()
screen=rgraphics.graphic()
os.system("clear")
fp=rgraphics.fpslimiter()
content=[]
for shade in ["B","D","G","L","W"," "]:
	precontent=[]
	for color in ["1","2","3","4","5","6","7","8"]:
		precontent.append(color+shade+"0")
	content.append(precontent)
screen.init(38,83,"B1")
ball=rgraphics.graphic()
ball.content=rgraphics.dispform(content)
ball.posx=random.randrange(5,75)
ball.posy=random.randrange(5,30)
ball.speedx=1
ball.speedy=1
while True:
	#fp.start()
	asyncio.run(screen.clear("L"))
	ball.move()
	ball.stayin(screen,"bounce")
	ball.draw(screen)
	screen.display(colouring=True)
	#fp.end(60)