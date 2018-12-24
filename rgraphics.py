import sys
import random
import colorama
import os
import time
colorama.init()
formatdict={" ":"  ","B":"██","L":"░░","G":"▒▒","D":"▓▓","W":"  ","1":"\u001b[30m","2":"\u001b[31m","3":"\u001b[32m","4":"\u001b[33m","5":"\u001b[34m","6":"\u001b[35m","7":"\u001b[36m","8":"\u001b[37m","0":"\u001b[0m"}
def dispform(inpot):
	if inpot==list(inpot):
		for row in range(len(inpot)):
			for px in range(len(inpot[row])):
				prepx=""
				for char in range(len(inpot[row][px])):
					prepx+=formatdict[inpot[row][px][char]]
				inpot[row][px]=prepx
	elif inpot==str(inpot):
		preinpot=""
		for char in range(len(inpot)):
			preinpot+=formatdict[inpot[char]]
		inpot=preinpot
	return inpot
class graphic:
	def __init__(self):
		self.posx=0
		self.posy=0
		self.speedx=0
		self.speedy=0
		self.content=[[""]]
	def draw(self,other):
		roundedposx = round(self.posx)
		roundedposy = round(self.posy)
		for row in range(len(self.content)):
			currentrow = self.content[row]
			currentposy = row+roundedposy
			othercurrentrow = other.content[currentposy]
			for px in range(len(currentrow)):
				try:
					if currentrow[px]!="":
						if "\u001b[0m" in currentrow[px]:
							othercurrentrow[px+roundedposx]=currentrow[px]+"\u001b[0m"
						else:
							othercurrentrow[px+roundedposx]=currentrow[px]
				except:
					pass
	def init(self,height,width,shade):
		self.content=[]
		for x in range(height+1):
			precontent=[]
			for y in range(width+1):
				precontent.append(shade)
			self.content.append(precontent)
		self.content=dispform(self.content)
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
	def display(self,colouring=False):
		print("",end="\033[1;1H")
		prerend=""
		for row in self.content:
			for px in row:
				prerend+=px
			prerend+=("\n")
		sys.stdout.write(prerend)
	async def clear(self,shade):
		shade=dispform(shade)
		for row in range(len(self.content)):
			for col in range(len(self.content[row])):
				self.content[row][col]=shade
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