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
class graphic:
	def __init__(self):
		self.posx=0
		self.posy=0
		self.speedx=0
		self.speedy=0
		self.content=[]
	def draw(self,other):
		for row in range(len(self.content)):
			for px in range(len(self.content[row])):
				try:
					if self.content[row][px]!="":
						other.content[row+self.posy][px+self.posx]=self.content[row][px]
				except:
					pass
	def init(self,height,width,color):
		self.content=[]
		for x in range(height+1):
			precontent=[]
			for y in range(width+1):
				precontent.append(color)
			self.content.append(precontent)
	def stayin(self,other,type="none"):
		if type=="none":
			if self.posx<0:
				self.posx=0
			elif self.posx+len(self.content[0])>len(other.content[0]):
				self.posx=len(other.content[0])-len(self.content)
			if self.posy<0:
				self.posy=0
			elif self.posy+len(self.content)>len(other.content):
				self.posy=len(other.content)-len(self.content)
		elif type=="bounce":
			if self.posx<0:
				self.posx=0
				self.speedx*=-1
			elif self.posx+len(self.content[0])>len(other.content[0]):
				self.posx=len(other.content[0])-len(self.content[0])
				self.speedx*=-1
			if self.posy<0:
				self.posy=0
				self.speedy*=-1
			elif self.posy+len(self.content)>len(other.content):
				self.posy=len(other.content)-len(self.content)
				self.speedy*=-1
	def move(self):
		self.posx+=self.speedx
		self.posy+=self.speedy
	def display(self):
		print("",end="\033[1;1H")
		prerend=""
		for row in self.content:
			for px in row:
				prerend+=px
			prerend+=("\n")
		sys.stdout.write(prerend)
	def coldec(self,other):
		for x in range(len(self.content)):
			for y in range(len(self.content[x])):
				for a in range(len(other.content)):
					for b in range(len(other.content[a])):
						if round(x+self.posy)==round(a+other.posy):
							if round(y+self.posx)==round(b+other.posx):
								return True
		return False
	def bounceoff(self,other):
		if self.coldec(other):
			self.speedx*=-1
			self.speedy*=-1
	def clear(self,color):
		for row in range(len(self.content)):
			for col in range(len(self.content[row])):
				if not self.content[row][col]==color:
					self.content[row][col]=color
class fpslimiter:
	def __init__(self):
		self.fps=0
		self.starttime=time.time()
		self.endtime=time.time()
	def start(self):
		self.starttime=time.time()
	def end(self,maxfps=60):
		while True:
			self.endtime=time.time()
			try:
				self.fps=round(1/(self.endtime-self.starttime))
			except:
				pass
			else:
				if self.fps>maxfps:
					pass
				else:
					return self.fps

def intro():
	os.system("cls")
	r=graphic()
	r.content=[[black*3+white+black+white+black*5+white*2+black+white+black*5+white+black*2],[black+white+black+white*8+black+white+black+white*8+black],[black*2+white*2+black+white+black*4+white+black+white+black+white+black*5+white+black+white],[black+white+black+white+black+white*6+black+white+black+white*8+black],[black+white+black+white+black+white+black*5+white*2+black*3+white+black*3+white*2+black]]
	r.display()
	time.sleep(1)