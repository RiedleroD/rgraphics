import rgraphics
screen=rgraphics.screen()
square=rgraphics.square()
screen.color=white
screen.height=16
screen.width=16
screen.init()
square.height=19
square.width=1
square.posx=11
square.posy=2
square.speedy=1
square.speedx=-1
square.motionstyle="no0e"
fpslimiter=rgraphics.fpslimiter()
fps=0
fpslimiter.start()
while True:
	fps=str(round(fpslimiter.end(30)))
	fpslimiter.start()
	screen.init()
	screen.content[16][16]=fps
	square.motion(screen)
	square.noob(screen)
	square.draw(screen)
	screen.display()