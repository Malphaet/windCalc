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
sys.path.append(os.path.join(CURRENT_DIR,'Modules/mapGen'))

import mapGen as mg
######################
#     Functions      #
######################

######################
#    Main Program    #
######################

# -- Vars -- #
colors={(120,50,12):3,(11,101,156):2,(0,0,0):0}
# -- Prog -- #

pict=mg.mapGen((420,420),colors,[mg.confGive(mg.giving,(0,2),(0,3))],mg.dropping,1)

pict.save('test.tiff','tiff')