"""A renderer with almost no dependencies which draws directly into the shell"""
__authors__		=	["Riedler"]
__copyright__		=	"Copyright 2019, Riedler"
__credits__		=	["Riedler","Philip Damianik"]
__license__		=	"CC"
__version__		=	"0.03a"
__maintainer__		=	"Riedler"
__status__		=	"Development"
import os
import sys
import time
import asyncio
from contextlib import suppress
if os.name=="nt":
	import colorama
	colorama.init()
	def clearscreen():
		os.system("cls")
else:
	def clearscreen():
		os.system("reset")
stdwrite=sys.stdout.write
										#COLOR
class Color():
	def __init__(self):
		self.bck="\033[30m"
		self.red="\033[31m"
		self.grn="\033[32m"
		self.yel="\033[33m"
		self.bue="\033[34m"
		self.mag="\033[35m"
		self.cyn="\033[36m"
		self.wht="\033[37m"
		self.rst="\033[0m"
	def colrs(self,rst=False):
		if rst:
			return (self.bck,self.red,self.grn,self.yel,self.bue,self.mag,self.cyn,self.wht,self.rst)
		else:
			return (self.bck,self.red,self.grn,self.yel,self.bue,self.mag,self.cyn,self.wht)
colr=Color()
rst=colr.rst
										#SHADES
class MiscCont():
	def __init__(self):
		self.bar=		"㍴"
		self.dm=		"㍷"
		self.dm2=		"㍸"
		self.dm3=		"㍹"
		self.kb=		"㎅"
		self.mb=		"㎆"
		self.gb=		"㎇"
		self.cal=		"㎈"
		self.kcal=		"㎉"
		self.hz=		"㎐"
		self.khz=		"㎑"
		self.mhz=		"㎒"
		self.ghz=		"㎓"
		self.cc=		"ᄄ"
		self._2l=		"ᄘ"
		self.dotb=		"⏺ "
		self.dots=		"‧ "
		self.b_circle=	"⚫"
		self.h_circle=	"〇"
		self.arr_left=	"〈"
		self.arr_right=	"〉"
		self.brack1_o=	"【"
		self.brack1_c=	"】"
		self.brack2_o=	"〔"
		self.brack2_c=	"〕"
		self.brack3_o=	"〖"
		self.brack3_c=	"〗"
		self.brack4_o=	"〘"
		self.brack4_c=	"〙"
		self.vase=		"〠"
		self.refmark=	"※"
		self.line=		"〡"
		self.lines=		"||"
		self.wiggx=		"〤"
		self.wiggxx=	"〷"
		self.cross=		"〸"
		self.cross2=	"〹"
		self.triangle=	"ᅀ"
		self.pill=		"ↀ "
		self.sonar=		"ↂ "
		self.sonar2=	"ↈ "
		self.anker=		"⚓"
		self.check_mark="✅"
		self.umbrella=	"☔"
		self.coffee=	"☕"
		self.stars=		"✨"
		self.qmark_red=	"❓"
		self.qmark_grey="❔"
		self.emark_grey="❕"
		self.emark_red=	"❗"
		self.plus=		"➕"
		self.minus=		"➖"
		self.divison=	"➗"
		self.m1=		"ᄀ"
		self.m2=		"ᄁ"
		self.m3=		"ᄂ"
		self.m4=		"ᄇ"
		self.m5=		"ᄈ"
		self.m6=		"ᄉ"
		self.m7=		"ᄒ"
		self.m8=		"ᄓ"
		self.m9=		"ᄖ"
		self.m10=		"ᄗ"
		self.m11=		"ᄘ"
		self.m12=		"ᄠ"
		self.m13=		"ᄡ"
		self.m14=		"ᄢ"
		self.m15=		"ᄣ"
		self.m16=		"ᄤ"
		self.m17=		"ᄥ"
		self.m18=		"ᄦ"
		self.m19=		"ᄧ"
		self.m20=		"ᄨ"
		self.m21=		"ᄩ"
		self.m22=		"ᄰ"
		self.m23=		"ᄱ"
		self.m24=		"ᄲ"
		self.m25=		"ᄳ"
		self.m26=		"ᄴ"
		self.m27=		"ᄵ"
		self.m28=		"ᄶ"
		self.m29=		"ᄷ"
		self.m30=		"ᄸ"
		self.m31=		"ᄹ"
		self.m32=		"ᅁ"
		self.m33=		"ᅂ"
		self.m34=		"ᅃ"
		self.m35=		"ᅄ"
		self.m36=		"ᅅ"
		self.m37=		"ᅆ"
		self.m38=		"ᅈ"
		self.m39=		"ᅉ"
		self.m40=		"ᅐ"
		self.m41=		"ᅑ"
		self.m42=		"ᅒ"
		self.m43=		"ᅓ"
		self.m44=		"ᅔ"
		self.m45=		"ᅕ"
		self.m46=		"ᅖ"
		self.m47=		"ᅗ"
		self.m48=		"ᅘ"
		self.m49=		"ᅙ"
		self.m50=		"ឈ "
		self.m51=		"ញ "
		self.m52=		"យ "
		self.m53=		"ℳ "
		self.m54=		"ᄑ"
		self.m55=		"〈"
		self.m58=		"♈"
		self.m59=		"♉"
		self.m60=		"♐"
		self.m61=		"♑"
		self.m62=		"♒"
		self.m63=		"♓"
		self.m64=		"〄"
	def shades(self):
		return [value for name, value in vars(self).items()]
class NumberCont():
	def __init__(self):
		self._0=	"ᄆ"
		self._00=	"ᅇ"
		self._2=	"ᄅ"
		self._22=	"ᄙ"
		self.r1=	"Ⅰ "
		self.r2=	"Ⅱ "
		self.r3=	"Ⅲ "
		self.r4=	"Ⅳ "
		self.r5=	"Ⅴ "
		self.r6=	"Ⅵ "
		self.r7=	"Ⅶ "
		self.r8=	"Ⅷ "
		self.r9=	"Ⅸ "
		self.r10=	"Ⅹ "
		self.c1=	"① "
		self.c2=	"② "
		self.c3=	"③ "
		self.c4=	"④ "
		self.c5=	"⑤ "
		self.c6=	"⑥ "
		self.c7=	"⑦ "
		self.c8=	"⑧ "
		self.c9=	"⑨ "
		self.c10=	"⑩ "
		self.c17=	"⑰ "
		self.c18=	"⑱ "
		self.c19=	"⑲ "
		self.c20=	"⑳ "
		self.b1=	"⑴ "
		self.b2=	"⑵ "
		self.b3=	"⑶ "
		self.b4=	"⑷ "
		self.b5=	"⑸ "
		self.b6=	"⑹ "
		self.b13=	"⒀ "
		self.b14=	"⒁ "
		self.b15=	"⒂ "
		self.b16=	"⒃ "
		self.b17=	"⒄ "
		self.b18=	"⒅ "
		self.b19=	"⒆ "
		self.b20=	"⒇ "
		self.p1=	"⒈ "
		self.p1=	"⒉ "
		self.p1=	"⒐ "
		self.p1=	"⒑ "
		self.p1=	"⒒ "
		self.p1=	"⒓ "
		self.p1=	"⒔ "
		self.p1=	"⒕ "
		self.p1=	"⒖ "
		self.p1=	"⒗ "
		self.p1=	"⒘ "
		self.p1=	"⒙ "
	def shades(self):
		return [value for name, value in vars(self).items()]
class LetterCont():
	def __init__(self):
		self.a=		"a "
		self.b=		"b "
		self.c=		"ᄃ"
		self.d=		"d "
		self.e=		"ᄐ"
		self.f=		"f "
		self.g=		"g "
		self.h=		"h "
		self.i=		"i "
		self.j=		"j "
		self.k=		"l "
		self.l=		"ᄂ"
		self.m=		"m "
		self.o=		"o "
		self.p=		"p "
		self.q=		"q "
		self.r=		"r "
		self.s=		"s "
		self.t=		"t "
		self.u=		"u "
		self.v=		"v "
		self.w=		"w "
		self.x=		"x "
		self.y=		"y "
		self.z=		"z "
		self.ä=		"ä "
		self.ö=		"ö "
		self.ü=		"ü "
		self.ll=	"ᄔ"
		self.lc=	"ᄕ"
	def shades(self):
		return [value for name, value in vars(self).items()]
class Shades():
	def __init__(self):
		self.a=	"██"
		self.b=	"▓▓"
		self.c=	"▒▒"
		self.d=	"░░"
		self.e=	"  "
		self.let=LetterCont()
		self.num=NumberCont()
		self.misc=MiscCont()
	def shades(self,shds=True,num=False,let=False,misc=False):
		l=[]
		if shds:
			l+=[self.a,self.b,self.c,self.d,self.e]
		if let:
			l+=self.let.shades()
		if num:
			l+=self.num.shades()
		if misc:
			l+=self.misc.shades()
		return l
shds=Shades()
class Settings():
	def __init__(self):
		self.warnings=True
		self.spawnvisible=False
		self.defwidth=2
		self.defheight=2
		self.defcontent=[]
sett=Settings()
										#PIXEL
class Px():
	def __init__(self,color=colr.bck,shade=shds.a):
		self.shade=shade
		self.color=color
		if type(color)==type(shade)==type(""):
			self.content=color+shade
	def clear(self):
		self.shade=shds.a
		self.color=colr.bck
	def equals(self,px):
		if self.__class__==px.__class__:
			return self.color==px.color and self.shade==px.shade
		else:
			return False

										#GRAPHIC
class Graphic():
	def __init__(self,visible=sett.spawnvisible,width=sett.defwidth,height=sett.defheight,bg=Px(),warning=sett.warnings,content=sett.defcontent,speedx=0,speedy=0,posx=1,posy=1):
		if bg.__class__!=Px:
			raise TypeError("Attribute 'bg' has to be a "+Px+", but it's a "+bg.__class__)
		for row in content:
			for col in row:
				if col.__class__!=Px:
					raise TypeError("Attribute 'content' has to be a list of lists of "+Px+", but it's a list od "+bg.__class__)
		self.posx=posx
		self.posy=posy
		self.speedx=speedx
		self.speedy=speedy
		self.content=content
		self.prevcontent=[]
		self.visible=visible
		self.bg=bg
		for row in range(height):
			precontent=[]
			nonearray=[]
			for col in range(width):
				precontent.append(self.bg)
				nonearray.append(Px(shade=None,color=None))
			if self.content==sett.defcontent:
				self.content.append(precontent)
			self.prevcontent.append(nonearray)
		rows, columns=os.popen('stty size', 'r').read().split()
		if int(rows)<height or int(columns)<width*2:
			input("You need to zoom out! Press enter to continue.")
	def display(self):
		changes2write=""
		bg=self.bg
		for row in range(len(self.content)):
			rowcontent=tuple(self.content[row])
			prevrowcontent=tuple(self.prevcontent[row])
			if rowcontent!=prevrowcontent:
				rowstr=str(row+1)+";"
				waslastpixdiff=False		#this marks if the last checked pixel was different
				waslastdrawdiffcolr=False	#this marks if the last checked pixel that will be drawn has the same color yes I know diff stands for different, but I'm too lazy to change the name now.
				lastdrawcolr=None			#this is the color of the previousely drawn pixel
				for col in range(len(rowcontent)):
					colcontent=rowcontent[col]
					prevcolcontent=prevrowcontent[col]
					if colcontent!=prevcolcontent:
						waslastdrawdiffcolr=colcontent.color==lastdrawcolr
						if waslastpixdiff and waslastdrawdiffcolr:
							changes2write+=colcontent.content
						elif waslastpixdiff:
							changes2write+=rst+colcontent.content
						elif waslastdrawdiffcolr:
							changes2write+="\033["+rowstr+str((col*2)+1)+"H"+colcontent.content
						else:
							changes2write+=rst+"\033["+rowstr+str((col*2)+1)+"H"+colcontent.content
						self.prevcontent[row][col]=colcontent
						waslastpixdiff=True
						lastdrawcolr=colcontent.color
					else:
						waslastpixdiff=False
					self.content[row][col]=bg
		stdwrite("".join(changes2write))
	def stayin(self,other,type=0):
		x=self.posx
		y=self.posy
		w=len(self.content)
		h=len(self.content[0])
		ow=len(other.content)
		oh=len(other.content[0])
		o=oh-h
		o2=ow-w
		if type==0:		#Normal
			if x<1:
				self.posx=1
			elif x>o:
				self.posx=o
			if y<1:
				self.posy=1
			elif y>o2:
				self.posy=o2
		elif type==1:	#Bounce
			if x<1:
				self.posx=2
				self.speedx*=-1
			elif x>o:
				self.posx=o-1
				self.speedx*=-1
			if y<1:
				self.posy=2
				self.speedy*=-1
			elif y>o2:
				self.posy=o2-1
				self.speedy*=-1
		else:
			raise ValueError("Wrong stayin type")
	def draw(self,other,noerr=False,offx=0,offy=0):
		posx=other.posx+offx
		precontent=self.content
		for row in range(len(other.content)):
			newrow=row+other.posy+offy
			rowcontent=other.content[row]
			for col in range(len(rowcontent)):
				if other.content[row][col] not in ("",None,''):
					precontent[newrow][col+posx]=rowcontent[col]
		self.content=precontent
	def move(self):
		try:
			self.posx+=self.speedx
			self.posy+=self.speedy
		except KeyboardInterrupt:
			clearscreen()
			quit()
class FpsLimiter():
	def __init__(self):
		self.fps=0
		self.maxfps=60
		self.time=time.time()
	def start(self):
		self.time=time.time()
	def end(self,counter=False):
		if counter:
			return round(1/(time.time()-self.time))
		else:
			try:
				mintime=1/self.maxfps
				t=self.time+mintime
				while time.time()<t:
					pass
				return round(1/(time.time()-self.time))
			except KeyboardInterrupt:
				clearscreen()
				quit()
# ¢: ← If you need help, please ask this daemon.
