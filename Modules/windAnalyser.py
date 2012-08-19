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
from PIL import Image
from mapGen import mapGen,DEFAULT_COLORS

terrains=DEFAULT_COLORS
#################
# Classes
#################

class vector():
	"Semi mathematical vector, multiplied they should return real vectors, let's see"
#################
# Functions
#################

def windAnalyser(image,wind,upd=DEFAULT_COLORS,**kwargs):
	pixt=image.load()
	size=image.size
	
	terrains.update(upd)
	table=windProcess(pixt,size)
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
#################
# Test
#################
if __name__=='__main__':
	args=sys.argv
	if len(args)>1 and args[1]=='test':
		im=mapGen('RGB',(10,10))
		table=windAnalyser(im,(21,7))
		for i in table:
			print i
