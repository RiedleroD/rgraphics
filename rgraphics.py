import sys
import random
import colorama
import os
import time
colorama.init()
black="█"*2
light_grey="░"*2
grey="▒"*2
dark_grey="▓"*2
white=" "*2
class square:
	def __init__(self):
		self.color=black
		self.height=1
		self.width=1
		self.posx=0
		self.posy=0
		self.speedx=0
		self.speedy=0
		self.motionstyle="Bounce"
	def draw(self,scrn):
		for x in range(self.height):
			for y in range(self.width):
				try:
					scrn.content[x+self.posy][y+self.posx]=self.color
				except:
					pass
	def motion(self,scrn):
		if self.motionstyle=="Bounce":
			if self.posx+self.width-1==scrn.width or self.posx==0:
				self.speedx*=-1
			if self.posy+self.height-1==scrn.height or self.posy==0:
				self.speedy*=-1
		elif self.motionstyle=="none":
			pass
		else:
			raise ValueError("No valid motionstyle for "+str(self)+".")
		self.posx+=self.speedx
		self.posy+=self.speedy
	def noob(self,scrn):	#This stands actually for "no out of bounce". idk how to give this a better name...
		if self.width<=scrn.width and self.height<=scrn.height:
			while self.posx+self.width-1>scrn.width:
				self.posx-=1
			while self.posy+self.height-1>scrn.height:
				self.posy-=1
			while self.posx<0:
				self.posx+=1
			while self.posy<0:
				self.posy+=1
class screen:
	def __init__(self):
		self.color=white
		self.content=[]
		self.height=0
		self.width=0
	def init(self):
		self.content=[]
		for x in range(self.height+1):
			precontent=[]
			for y in range(self.width+1):
				precontent.append(self.color)
			self.content.append(precontent)
	def display(self,overwrite=True):
		endwrite=""
		for row in self.content:
			for px in row:
				endwrite+=px
			endwrite+=("\n")
		if overwrite==True:
			os.system("cls")
		sys.stdout.write(endwrite)
class fpslimiter:
	def start(self):
		self.starttime=time.time()
	def end(self,maxfps=60):
		while True:
			self.endtime=time.time()
			try:
				self.fps=1/(self.endtime-self.starttime)
			except:
				pass
			else:
				if self.fps>maxfps:
					pass
				else:
					return self.fps
screen=screen()
square=square()
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
fpslimiter=fpslimiter()
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