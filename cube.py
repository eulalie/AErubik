#!/usr/bin/env python
# -*- coding: utf-8 -*-

## cube.py
##

import random
import numpy

random.seed(0)

#----------------------------------------------------------
# Color

NORMAL="\033[0;39m"
GREEN="\033[1;32m" 
RED="\033[1;31m" 
BLUE="\033[1;34m" 
YELLOW="\033[1;33m"
WHITE="\033[0;37m"
ORANGE="\033[1;35m"  # Ok, it's not really orange, but who cares ?

# Fonctions
def print_b(s):
  return BLUE+str(s)+NORMAL
def print_r(s):
  return RED+str(s)+NORMAL
def print_g(s):
  return GREEN+str(s)+NORMAL
def print_y(s):
  return YELLOW+str(s)+NORMAL
def print_w(s):
  return WHITE+str(s)+NORMAL
def print_o(s):
  return ORANGE+str(s)+NORMAL

dico_fct={'r':print_r, 'b':print_b, 'g':print_g, 'y':print_y, 'o':print_o, 'w':print_w}


Rx_pos = numpy.array([[1,0,0],[0,0,-1],[0,1,0]]) 

#----------------------------------------------------------


class s_cube:
    
  def __init__(self,pos,col):
    self.x = pos[0]
    self.y = pos[1]
    self.z = pos[2]
    self.colors = col

  def __repr__(self):
    return str(self.x)+','+str(self.y)+','+str(self.z)+'   '+str(self.colors)

class cube:

  def __init__(self):
    self.s_cubes = []
    index = [-2,-1,1,2]
    for x in index:
      for y in index:
        for z in index:
          colors = ['n']*6
          if x == -2:
            colors[0] = 'r'  #color x1
	  if x == 2:
            colors[1] = 'o'
          if y == -2:
            colors[2] = 'b'
          if y == 2:
            colors[3] = 'g'
          if z == -2:
            colors[4] = 'y'
          if z == 2:
            colors[5] = 'w'
          self.s_cubes.append(s_cube([x,y,z],colors))

  def give_crowns(self):
    crownsX = [[],[],[],[]]
    crownsY = [[],[],[],[]]
    crownsZ = [[],[],[],[]]
    for c in self.s_cubes:
      if c.x == -2:
        crownsX[0].append(c)
      if c.x == -1:
        crownsX[1].append(c)
      if c.x == 1:
        crownsX[2].append(c)
      if c.x == 2:
        crownsX[3].append(c)

      if c.y == -2:
        crownsY[0].append(c)
      if c.y == -1:
        crownsY[1].append(c)
      if c.y == 1:
         crownsY[2].append(c)
      if c.y == 2:
         crownsY[3].append(c)

      if c.z == -2:
        crownsZ[0].append(c)
      if c.z == -1:
        crownsZ[1].append(c)
      if c.z == 1:
        crownsZ[2].append(c)
      if c.z == 2:
        crownsZ[3].append(c)
      
      crownsX[0] = sorted(crownsX[0],key = lambda s_cube:(s_cube.y,s_cube.z))
      crownsX[3] = sorted(crownsX[3],key = lambda s_cube:(s_cube.y,s_cube.z))
      crownsY[0] = sorted(crownsY[0],key = lambda s_cube:(s_cube.x,s_cube.z))
      crownsY[3] = sorted(crownsY[3],key = lambda s_cube:(s_cube.x,s_cube.z))
      crownsZ[0] = sorted(crownsZ[0],key = lambda s_cube:(s_cube.x,s_cube.y))
      crownsZ[3] = sorted(crownsZ[3],key = lambda s_cube:(s_cube.x,s_cube.y))

    return (crownsX,crownsY,crownsZ)

  def faces_color(self):
    cr_axes = self.give_crowns()
    f_color = []
    for a,axe in enumerate(cr_axes):
      for i,cr in enumerate(axe):
        if i%3==0:
          f_color.append([])
          for c in cr:
            f_color[-1].append(c.colors[a*2+i*1/3])

    return f_color

  def __repr__(self):
    res = ''
    for c in self.s_cubes:
      res += c.__repr__() + '\n'

    return res

  def print_face(self):
    motif='■'
    str_=''
  
    f_color = self.faces_color()
    for f in f_color:
      sep=''
      for col in f:
        str_+=dico_fct[str(col)](motif)+' '
        sep+='--'
      str_+= '\n'+sep+'\n'

    print str_



cube1 = cube()
#print cube1
#faces = cube1.give_faces()

#print cube1

#print cube1.faces_color()

cube1.print_face()
  
