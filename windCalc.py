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

#------ Ajouts ------#
CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR,'Modules'))

import mapGen as mg

######################
#     Functions      #
######################

def dprint(*txt):
	if debug: 
		st=''
		for s in txt: st+=str(s)+' '
		print st
######################
#    Main Program    #
######################

# -- Vars -- #
debug=True

colors0={(120,50,12):9,(11,101,156):9,(0,0,0):0}
colors1={(120,50,12):10,(11,101,156):11,(0,0,0):0}
colors=colors1

vals=[((0,1),(1,2)),((1,1),(0,5)),((1,2),(0,2))]
functs=[mg.confGive(mg.giving,i,j) for i,j in vals]
patch_sizes=[0,1,2]

# -- Prog -- #
pict=mg.init_image('RGB',(420,420))

#for i in mg.twistYeld(-1,5):
#	print i

np=0
dprint("Map being generated...")
for funct in functs:
	dprint("Pass ",np)
	pict=mg.mapGen(pict,colors,funct,mg.dropping,patch_sizes[np])
	pict.save('tmp_{}.bmp'.format(np),'bmp')
	np+=1
dprint("Map generated")

pict.save('test.tiff','tiff')
