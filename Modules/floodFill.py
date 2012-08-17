# -*- coding:utf8 -*-

###########################################
# floodFill.py
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
# LICENCE					      #
########################################################

#################
# Vars
#################

#NULL,RIGHT,LEFT,UP,DOWN=(0,1,2,3,4)
#DIRS={NULL:(0,0),RIGHT:(1,0),LEFT:(-1,0),UP:(0,1),DOWN:(0,-1)}
BLACK=(0,0,0)

#################
# Functions
#################

#################
# Utils
#######

#def val(table,pos,DIR=NULL):
#	if DIR!=NULL: x,y=move(pos,DIR)
#	else: x,y=pos
#	return table[x][y]

#def move(pos,DIR)
#	x,y=DIRS[DIR]
#	x,y=pos[0]+x,pos[1]+y
#	return x,y

#################
# Floodfill
#######

def floodFill(pixels,pos,value,BORDER_COLOR=BLACK):
	"Flood fill on a region of non-BORDER_COLOR pixels."
	x,y=pos
	if pixels[x,y] == BORDER_COLOR: return
	edge = [(x, y)]
	pixels[x,y]=value
	while edge:
		newedge = []
		for (x, y) in edge:
			for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)): # No boundary control: BORDER_COLOR is here for that
				if pixels[s,t] not in (BORDER_COLOR, value):
					pixels[s,t]=value
					newedge.append((s, t))
		edge = newedge
