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
import geoGen as gg

######################
#     Functions      #
######################

######################
#     Generators
##########

def mapGen(mode,size,terrains):
	"""mapgen(mode,size,terrains) => Generate a <size> PIL immage"""
	pict=init_image(mode,size)
	drpict=ImageDraw.Draw(pict)
	pixt=pict.load()
	
	random.seed()
	genSea(drpict,size,terrains['sea'])
	middle=genCoast(drpict,size,terrains['coast'])
	fillRegion(pixt,size,middle,terrains['coast'])
	return pict

def genSea(pict,size,color):
	pict.rectangle((0,0,size[0],size[1]),color)
	
def genCoast(pict,size,color):
	ax,ay,aX,aY=fourBorders(size)
	liste=gg.multiScatter([[ax,ay],[aX,aY]],4)
	liste.draw(pict,color)
	return liste.middle(0,len(liste)-1)
######################
#     Utils
##########

def init_image(mode,size):
	return Image.new(mode,size)

def fourBorders(size,opposites=1):
	crds=[random.randint(0,1)]
	crds.append(int(not crds[0]))
	if not opposites: crds.append(random.randint(0,1))
	else: crds.append(int(not crds[0]))
	crds.append(int(not crds[1]))
	
	ax,ay=random.randint(0,size[0]),random.randint(0,size[1])
	aX,aY=random.randint(0,size[0]),random.randint(0,size[1])
	return ax*crds[0],ay*crds[1],aX*crds[2],aY*crds[3]

def fillRegion(pixt,size,start,color):
	limits=[[0 for i in xrange(size[1])] for j in xrange(size[0])]
	for i in xrange(size[0]):
		limits[i][0]=1
		limits[i][size[1]-1]=1
	for i in xrange(size[1]):
		limits[0][i]=1
		limits[size[1]-1][i]=1
	print "    !> Not filled: Implementation not done",start
######################
#       Tests        #
######################

if __name__=='__main__':
	args=sys.argv
	if len(args)>1 and args[1]=='test':
		size,mode=(420,420),'RGB'
		sys.setrecursionlimit(size[0]*size[1]+1000)
		colors={'coast':(120,50,12),'sea':(11,101,156)}
		
		dprint("Map being generated...")
		
		pict=init_image(mode,size)
		pict=mapGen(mode,size,colors)

		dprint("Map generated")

		pict.save('test_map.tiff','tiff')
