# -*- coding:utf8 -*-

###########################################
# Date: 2012                              #
# Auteur: Malphaet                        #
# Nom: windCalc                           #
# Version: 0.1a                           #
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
import os,sys
from PIL import Image, ImageDraw
#------ Ajouts ------#
CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR,'Modules'))

import mapGen as mg
import geoGen as gg

######################
#     Functions      #
######################

######################
#    Main Program    #
######################

im=Image.new('1',(400,400))

draw=ImageDraw.Draw(im)
old=gg.scatteredLine([[50,0],[50,400]])
for nb in xrange(7):
	etapes=1*(nb+1)
	old=gg.multiScatter(old,1)
	for i in xrange(2**etapes):
		draw.line((old[i][0]+nb*50,old[i][1],old[i+1][0]+nb*50,old[i+1][1]),1)
im.save('test.bmp','bmp')
