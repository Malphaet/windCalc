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

from mapGen import mapGen
from windAnalyser import windAnalyser
import argparse

#---------------------#
#------ Parser -------#

parser=argparse.ArgumentParser(description="Analyse a picture and apply a uniform wind to the coasts, hence giving the resulting local wind.")
parser.add_argument('picture', metavar='Picture', nargs='?', type=str, help='The picture to analyse')

parser.add_argument('-o','--output',metavar='OUT', dest='output', type=str, default='a.bmp', help='where the resulting image will be saved')
parser.add_argument('-v','--verbose', dest='debug', action='store_true', default=False, help='be verbose')

parser.add_argument('-c','--config', metavar='CONF', dest='config', nargs=1, type=str, help='config file to load')

parser.add_argument('-g','--generate', dest='generate', action='store_true', default=False, help='generate a random map')
parser.add_argument('--genCoast_size', metavar='SIZE', dest='genCoast_size', nargs=2, type=int, default=(420,420), help='size of the generated map')
parser.add_argument('--genCoast_mode', metavar='MODE',dest='genCoast_mode', nargs=1, type=str,default='RGB', help='color mode of the generated map')
parser.add_argument('--genCoast_iter', metavar='ITER', dest='genCoast_iter', nargs=1, type=int,default=5, help='number of iteration the coast generation will do')
parser.add_argument('--genCoast_scatter', metavar='SCATTER', dest='genCoast_scatter', nargs=1, type=int,default=20, help='percentage of randomness in the scattering')

args = parser.parse_args()

if args.generate: im=mapGen(args.genCoast_mode,args.genCoast_size,genCoast_iter=args.genCoast_iter,genCoast_scatter=args.genCoast_scatter)
else: im=Image.open(args.picture)

wind=(21,5)
windAnalyser(im,wind)

im.save(args.output,'bmp')
