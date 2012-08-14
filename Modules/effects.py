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

import utils

######################
#---- Functions -----#
######################

def erode(image,erode,sizePatch):
	"Erode the <eroder> pixels of <image>"
	size=image.size
	for i in xrange(0,size[0]):
		for j in xrange(0,size[1]):
			if image[i,j]==erode:
				image[i,j]=image[randSize(i,sizePatch,size[0]),randSize(j,sizePatch,size[1])]
######################
#    Main Program    #
######################
import sys
if __name__=='__main__':
	if len(sys.argv)>1 and sys.argv[1]=='test':
		print "No test implemented yet"
