# -*- coding:utf8 -*-

###########################################
# Date: 2012                              #
# Auteur: Malphaet                        #
# Nom: windCalc                           #
# Copyright 2011: Malphaet                #
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

######################
#----- Modules ------#
######################

debug=True

#---- Importation ---#
import random
from PIL import Image


class twistYeld():
	def __init__(self,minV,maxV=None):
		self._minV=minV
		self._maxV=maxV
		if maxV==None:
			self._maxV=minV
			self._minV=0
		self._valM=(self._minV+self._maxV)/2
		self._valm=self._valM
		self._state=1
	def __iter__(self):
		return self
	def next(self):
		self._state*=-1
		if self._state==1: return self.add()
		else: return self.sub()
	def add(self):
		self._valM+=1
		if self._valM>self._maxV:
			if self._valm<self._minV:
				raise StopIteration
			else: 
				return self.sub()
		return self._valM
	def sub(self):
		self._valm-=1
		if self._valm<self._minV:
			if self._valm>self._maxV:
				raise StopIteration
			else: 
				return self.add()
		return self._valm
######################
#     Functions      #
######################

def mapGen(size,percents,give,drop,sizeFunction,yell=xrange):
	"""mapgen(size,percents,givingFunction,droppingFunction,sizeFunction)
	Generate a size image according to the percentages of pixels provided, using the given functions
	givingFunction is used to generate a pixel according to a percendage dictionnary
	droppingFunction is used to put the pixel on the map
	sizeF is the size needed af pixels to give to the functions"""
	pict=init_image('RGB',size)
	pixt=pict.load()
	i=0
	dprint("Map being generated...")
	for g in give:
		dprint("Pass ",i,' (',str(g),')')
		for i in yell(1,size[0]-1):
			for j in yell(1,size[1]-1):
				drop(pixt,(i,j),give(percents,collect(pixt,(i,j),sizeFunction)))
		i+=1
	dprint("Map generated")
	return pict

def init_image(mode,size):
	return Image.new(mode,size)

def collect(imageTable,center,size):
	ret=[]
	for i in xrange(center[0]-size,center[0]+size):
		for j in xrange(center[1]-size,center[1]+size):
			ret.append(imageTable[i,j])
	return ret
	
#--- Spetial functions ---#
def confGive(funct,randomness,genuine):
	def configuratedGive(percent,pixels):
		return giving(percent,pixels,randomness,genuine)
	return configuratedGive
	

def giving(percents,pixels,randomness,genuine):
	pixs=dict.fromkeys(percents.keys(),0)
	for pix in pixels: pixs[pix]+=random.randint(*randomness)*percents[pix]
	for pix in percents: pixs[pix]+=random.randint(*genuine)*percents[pix]
	return max(pixs,key=pixs.get) #random.choice(percents.keys())

def dropping(imageTable,pos,pixel):
	imageTable[pos[0],pos[1]]=pixel

def dprint(*txt):
	if debug: print txt
