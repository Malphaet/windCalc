# -*- coding:utf8 -*-

###########################################
# windAnalyser.py
# Nom: windCalc
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of windCalc.
#
# windCalc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# windCalc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with windCalc. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

#################
# Modules
#################

import os,sys
from PIL import Image,ImageDraw
from mapGen import mapGen,DEFAULT_COLORS
from math import cos,sin,tan,atan,atan2,acos,asin,sqrt,radians,degrees

terrains=DEFAULT_COLORS
DEFAULT_WIND_SIZE=5
#################
# Classes
#################

class vector():
	"Semi mathematical vector, multiplied they should return real vectors, let's see"
	def __init__(self,*coords):
		if type(coords[0])==list: coords=coords[0]
		self._list=list(coords)
	def __getitem__(self,pos):
		return self._list[pos]
	def __add__(self,other):
		return vector([i+j for i,j in (self,other)])
	def __str__(self):
		return str(self._list)
	
class windVector(vector):
	def __init__(self,pos,angle,value,size=DEFAULT_WIND_SIZE):
		vector.__init__(self,pos)
		self.value=value
		self.angle=radians(angle)
		self._size=size
		self._dist=0
	
	def update(self):
		self.dist()
		
	def dist(self):
		if self._dist==0:
			self._dist=sqrt((self._size**2)+((self._size/3.)**2))
		return self._dist
		
	def __str__(self):
		return '({},{}): {}° {}N'.format(self[0],self[1],self.angle,self.value)
		
	def write(self,d_image):
		"Write the vector to the given picture"
		lengh,size=self._size,self._size/3.
		dist=self.dist()
		a,b=self.angle,0.3
		c,d=radians(180)+a-b,radians(180)+a+b
		
		R=[]
		for angle in (a,c,d):
			R.append(tuple([int((f(angle)*dist)+add) for f,add in zip((sin,cos),(self[0],self[1]))]))
		
		d_image.polygon(R,fill=colorVector(self.value))
#################
# Functions
#################

def windAnalyser(image,wind,upd=DEFAULT_COLORS,**kwargs):
	pixt=image.load()
	size=image.size
	
	terrains.update(upd)
	# Dispatch wind (from source point), know where the wind will be
	table=windProcess(pixt,size)
	# Create acceleration maps (Perpendicular to the coast)
	# Blurr them
	return table

def windProcess(pixt,size):
	table=[]
	for i in xrange(size[0]):
		table.append([])
		for j in xrange(size[1]):
			table[i].append(windAtPos(pixt,i,j,size))
	return table
	
#################
# Utilities
#######

def init_wind(update):
	terrains.update(update)
	
def windAtPos(pixt,i,j,size):
	ret=[pixt[i,j] for i,j in [(i,min(j+1,size[1]-1)),(i,max(j-1,0)),(min(i+1,size[0]-1),j),(max(i-1,0),j)]]
	ret=map(value,ret)
	if ret==[1,1,1,1]:
		return (0,0)
	return ret[0]+ret[1],ret[2]+ret[3]


def value(val):
	if val==terrains['sea']:
		return 0
	if val==terrains['coast']:
		return 1
	if val==terrains['borders']:
		return 0
	print val
	raise ValueError

def colorVector(val):
	return (val%255,val%255,val%255)
#################
# Test
#################
if __name__=='__main__':
	args=sys.argv
	if len(args)>1 and args[1]=='test':
		im=mapGen('RGB',(500,500))
		dr_im=ImageDraw.Draw(im)
#		table=windAnalyser(im,(21,7))
#		for i in table:
#			print i
#		a=vector(1,2)
#		b=vector([1,5])
#		print a,b
		for i in xrange(1,101):
			for j in xrange(1,101):
				windVector([i*10,j*10],(i+j)*25,(i+j)*10).write(dr_im)
#		print c
#		c.write(dr_im)
		im.show()
