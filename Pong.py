import rgraphics
import msvcrt
import time
screen=rgraphics.screen()
fpslimiter=rgraphics.fpslimiter()
leftpad=rgraphics.square()
rightpad=rgraphics.square()
ball=rgraphics.square()

ball.speedx=1
ball.speedy=1

screen.width=32
screen.height=32



inpot=""
def input2command(inpot):
	if inpot=="w":
		leftpad.goup()
	elif inpot=="s":
		leftpad.godown()
	elif inpot=="H":
		rightpad.goup()
	elif inpot=="P":
		rightpad.godown()
	elif inpot=="q":
		inpot=input("Do you really wanna leave? (y/n)\n")
		if inpot=="y":
			quit()
while True:
	inpot=msvcrt.getwch()
	input2command(inpot)
	