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
		self._mid=(self._minV+self._maxV)/2
		self._val=self._mid
		self._iter=0
		self._state=0
	def __iter__(self):
		return self
	def next(self):
		if not self._state:
			self._state=-1
			self._iter+=1
			return self._val
		return self.evolve()
	def evolve(self):
		self._val=self._state*self._iter+self._mid
		if self._val>=self._maxV or self._val<self._minV: raise StopIteration
		if self._state==1:
			self._iter+=1
		self._state*=-1
		return self._val
######################
#     Functions      #
######################

def mapGen(originPict,percents,give,drop,sizeFunction,yell=xrange):
	"""mapgen(size,percents,givingFunction,droppingFunction,sizeFunction)
	Generate a size image according to the percentages of pixels provided, using the given functions
	givingFunction is used to generate a pixel according to a percendage dictionnary
	droppingFunction is used to put the pixel on the map
	sizeF is the size needed af pixels to give to the functions"""
	size=originPict.size
	mode=originPict.mode
	pixtO=originPict.load()

	pict=init_image(mode,size)
	pixt=pict.load()
	
	for i in yell(0,size[0]):
		for j in yell(0,size[1]):
			drop(pixt,(i,j),give(percents,collect(pixtO,(i,j),sizeFunction,size)))
	
	return pict

def init_image(mode,size):
	return Image.new(mode,size)

def collect(imageTable,center,sizeP,size):
	ret=[]
	for i in xrange(max(center[0]-sizeP,0),min(center[0]+sizeP,size[0])):
		for j in xrange(max(center[1]-sizeP,0),min(center[1]+sizeP,size[1])):
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
