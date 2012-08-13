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


def randSize(nb,toAdd,maxV):
	return random.randint(max(nb-toAdd,0),min(nb+toAdd,maxV))
