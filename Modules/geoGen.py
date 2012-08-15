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

import math,random

######################
#----- Classes ------#
######################

class point():
	def __init__(self,x,y):
		self._x=x
		self._y=y
	
class line():
	def __init__(self,a,b):
		self._list=[a,b]
	def __getitem__(self,key):
		return self._list[key]
	def middle(self):
		return ((self[0][0]+self[1][0])/2,(self[0][1]+self[1][1])/2)

class scatteredLine():
	def __init__(self,list_points,dim=2):
		self._list=[]
		for elt in list_points: self._list.append(elt)
		self._dim=dim
	def __getitem__(self,key):
		return self._list[key]
	def append(self,item):
		self._list.append(item)
	def __len__(self):
		return len(self._list)
	
	def middle(self,a,b):
		ret=[0]*self._dim
		for i in xrange(self._dim):
			ret[i]=(self[a][i]+self[b][i])/2
		return ret

	def ecarts(self,a,b):
		ret=[0]*self._dim
		for i in xrange(self._dim): ret[i]=(self[a][i]-self[b][i])
		return ret
	
	def euclidDist(self,a,b):
		ret=0
		for i in self.ecarts(a,b): ret+=i*i
		return math.sqrt(ret)
	
	def __repr__(self):
		return self._list
	def __str__(self):
		ret=''
		for elt in self:
			ret+=str(elt)+'\n'
		return ret
	dist=euclidDist
	center=middle
		
######################
#     Functions      #
######################		

def shake(pos,distMax):
	ret=[]
	for coord in pos:
		ret.append(coord+random.randint(-distMax,distMax))
	return ret

def scatter(pos,distMax):
	mx=len(pos)
	fangle=random.randint(0,360)
	ret,angle=[],[fangle,fangle]
	
	for i in xrange(mx-2):
		angle.append(random.randint(0,360))
	
	for i in xrange(mx):
		if i%2: funct=math.cos
		else: funct=math.sin
		
		ret.append(int(pos[i]+funct(angle[i])*distMax))
	
	return ret

def scatterList(liste,percent):
	new=scatteredLine([liste[0]])
	mx,i=len(liste),0
	while i<mx-1:
		center=liste.middle(i,i+1)
		dist=liste.euclidDist(i,i+1)/2
		new.append(scatter(center,(dist*percent)/100))
		new.append(liste[i+1])
		i+=1
	return new

def multiScatter(points,times,percent=20):
	if isinstance(points,scatteredLine): old=points
	else: old=scatteredLine(points)
	for i in xrange(times): old=scatterList(old,percent)
	return old
	

######################
#      Testing       #
######################	

if __name__=='__main__':
	print 'Tests in progress...'
	liste=scatteredLine([[0,100],[400,100]])
	random.seed()
	print liste
	print multiScatter(liste,4)
	
