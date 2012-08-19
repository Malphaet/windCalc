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

from PIL import Image,ImageDraw
from floodFill import floodFill 
import geoGen as gg

######################
#     Functions      #
######################

DEFAULT_COLORS={'coast':(120,50,12),'sea':(11,101,156),'borders':(0,0,0)}
DEFAULT_MAPGEN={'genCoast_iter':5,'genCoast_scatter':20}
######################
#     Generators
##########

def mapGen(mode,size,terrains=DEFAULT_COLORS,**kwargs):
	"""mapgen(mode,size,terrains,**kwargs) => Generate a <size> PIL immage
	The aditional arguments can set some more specific parameters"""
	pict=init_image(mode,size)
	drpict=ImageDraw.Draw(pict)
	pixt=pict.load()
	init_map(kwargs)
	
	genSea(drpict,size,terrains['sea'])
	middle=genCoast(drpict,size,terrains['coast'],kwargs['genCoast_iter'],kwargs['genCoast_scatter'])
	genBorders(drpict,size,terrains['borders'])
	floodFill(pixt,middle,terrains['coast'],terrains['borders'])
	
	return pict

def genSea(pict,size,color):
	pict.rectangle((0,0,size[0],size[1]),color)
	
def genCoast(pict,size,color,iters,scatter):
	ax,ay,aX,aY=randEdges(size)
	liste=gg.multiScatter([[ax,ay],[aX,aY]],iters,scatter)
	liste.draw(pict,color)
	return liste.middle(0,len(liste)-1)

def genBorders(pict,size,color):
	pict.rectangle([(0,0),(size[0]-1,size[1]-1)],outline=color)
######################
#     Utils
##########
def init_map(kwargs):
	random.seed()
	for elt in DEFAULT_MAPGEN:
		if elt not in kwargs:
			kwargs[elt]=DEFAULT_MAPGEN[elt]
	
def init_image(mode,size):
	return Image.new(mode,size)

def randEdges(size):
	i,j,mx=0,0,len(size)
	crds=[None]*(2*mx)
	cx,cy=[0,size[0]],[0,size[1]]
	while i<mx:
		rd=random.randint(0,1)
		if rd:
			crds[2*i]=cx.pop(random.randint(0,len(cx)-1))
			crds[2*i+1]=random.randint(0,size[1])
		else:
			crds[2*i]=random.randint(0,size[0])
			crds[i*2+1]=cy.pop(random.randint(0,len(cy)-1))
		i+=1
	return crds

######################
#       Tests        #
######################

if __name__=='__main__':
	args=sys.argv
	if len(args)>1 and args[1]=='test':
		size,mode=(420,420),'RGB'
		sys.setrecursionlimit(size[0]*size[1]+1000)
		colors=DEFAULT_COLORS
		dprint("Map being generated...")
		
		pict=init_image(mode,size)
		pict=mapGen(mode,size,colors)

		dprint("Map generated")

		pict.save('test_map.tiff','tiff')
