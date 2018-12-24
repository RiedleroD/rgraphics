import rgraphics
import os
import random
rgraphics.intro()
black="█"*2
light_grey="░"*2
grey="▒"*2
dark_grey="▓"*2
white=" "*2
screen=rgraphics.graphic()
os.system("cls")
fp=rgraphics.fpslimiter()
content=[["","","/red"+black,black,"/reset",""],["",black,black,black,black,""],["",black,black,black,black,""],["","",black,black,"",""]]
screen.init(38,83,light_grey)
for obj in ["1","2","3","4","5","6","7"]:
	globals()[obj]=rgraphics.graphic()
	globals()[obj].content=content
	globals()[obj].posx=random.randrange(5,75)
	globals()[obj].posy=random.randrange(5,30)
	globals()[obj].speedx=1
	globals()[obj].speedy=1
while True:
	fp.start()
	screen.clear(light_grey)
	for obj in ["1","2","3","4","5","6","7"]:
		globals()[obj].move()
		globals()[obj].stayin(screen,"bounce")
	for obj in ["1","2","3","4","5","6","7"]:
		globals()[obj].draw(screen)
	screen.display(colouring=True)
	fp.end(60)