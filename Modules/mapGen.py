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
import random,sys
from utils import dprint

from PIL import Image


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
		for j in xrange(max(center[1]-sizeP,0),min(center[1],size[1])):
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


if __name__=='__main__':
	args=sys.argv

	if len(args)>1 and args[1]=='test': 
	
		colors={(120,50,12):10,(11,101,156):11,(0,0,0):0}
		vals=[((1,2),(0,2))]
		functs=[confGive(giving,i,j) for i,j in vals]
		patch_sizes=[0]

		# -- Prog -- #
		pict=init_image('RGB',(420,420))

		np=0
		dprint("Map being generated...")
		for funct in functs:
			dprint("Pass ",np)
			pict=mapGen(pict,colors,funct,dropping,patch_sizes[np])
#			pict.save('tmp_{}.tiff'.format(np),'tiff')
			np+=1
		dprint("Map generated")

		pict.save('test.tiff','tiff')
