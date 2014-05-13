#!/usr/bin/env python
# -*- coding: utf-8 -*-

## cube.py
##

import random
import numpy

#random.seed(0)

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

#rotation matrix
Rx_neg = numpy.array([[1,0,0],[0,0,-1],[0,1,0]]) 
Rx_pos = numpy.array([[1,0,0],[0,0,1],[0,-1,0]]) 
Ry_neg = numpy.array([[0,0,1],[0,1,0],[-1,0,0]]) 
Ry_pos = numpy.array([[0,0,-1],[0,1,0],[1,0,0]]) 
Rz_neg = numpy.array([[0,-1,0],[1,0,0],[0,0,1]]) 
Rz_pos = numpy.array([[0,1,0],[-1,0,0],[0,0,1]]) 

dico_rot = {0:Rx_pos, 1:Rx_neg, 2:Ry_pos, 3:Ry_neg, 4:Rz_pos, 5:Rz_neg}
#----------------------------------------------------------


# elementary cube
class s_cube:
    
  def __init__(self,pos,col):
    self.x = pos[0]
    self.y = pos[1]
    self.z = pos[2]
    self.colors = col

  def __repr__(self):
    return str(self.x)+','+str(self.y)+','+str(self.z)+'   '+str(self.colors)

#Rubik's cube
class cube:

  def __init__(self):
    self.s_cubes = []
    index = [-2,-1,1,2] #4 crowns
    for x in index:
      for y in index:
        for z in index:
          colors = ['n']*6 # no color (interior cube)
          # if the cube is one a face, it gets a color
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
          
#return 3 listes (une pour chaque direction). Chaque liste est composée de 4 listes qui sont les cubes appartenant à une couronne.
#Les couronnes 0 et 3 sont les faces visibles de la direction.
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
      
      # on trie les listes des faces (dans le sens des deux autres axes) pour l'affichage.
      crownsX[0] = sorted(crownsX[0],key = lambda s_cube:(s_cube.y,s_cube.z))
      crownsX[3] = sorted(crownsX[3],key = lambda s_cube:(s_cube.y,s_cube.z))
      crownsY[0] = sorted(crownsY[0],key = lambda s_cube:(s_cube.x,s_cube.z))
      crownsY[3] = sorted(crownsY[3],key = lambda s_cube:(s_cube.x,s_cube.z))
      crownsZ[0] = sorted(crownsZ[0],key = lambda s_cube:(s_cube.x,s_cube.y))
      crownsZ[3] = sorted(crownsZ[3],key = lambda s_cube:(s_cube.x,s_cube.y))

    return (crownsX,crownsY,crownsZ)

  # return the color of each face
  def faces_color(self):
    cr_axes = self.give_crowns() 
    f_color = []
    for a,axe in enumerate(cr_axes): #3 listes, X, Y et Z
      for i,cr in enumerate(axe): # 4 couronnes par listes
        if i%3==0: #sur une face
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
    str_ = ['','','','']
    sep = ''

    f_color = self.faces_color()
    for i,f in enumerate(f_color):
      for j,col in enumerate(f):
        if col=='n':
          print 'Error: interior cube on a face'
          exit(0)
        # 4premiers cubes sur première ligne, 4 suivants sur 2ième...
        str_[j/4]+=dico_fct[str(col)](motif)+' '

        if j/4==0:
          sep += '--'

      # espace entre les faces
      for i in range(4):
        str_[i] += '  '
        

    for s in str_:
      print s

    print sep


#r : rotation voulu (dico rotation), cr: couronne dans l'axe de la rotation
  def move(self,r,cr):
    crown = self.give_crowns()[r/2][cr]
    for c  in crown:
      pos0 = numpy.array([c.x,c.y,c.z])
      pos1 = numpy.dot(pos0,dico_rot[r])
      c.x = pos1[0]
      c.y = pos1[1]
      c.z = pos1[2]
      
      # rotation de c:
      # trouver un meilleur moyen, c'est pourri
      col = c.colors
      if r==0:
        c.colors = [col[0],col[1],col[5],col[4],col[2],col[3]]
      if r==1:
        c.colors = [col[0],col[1],col[4],col[5],col[3],col[2]]
      if r==2:
        c.colors = [col[4],col[5],col[2],col[3],col[1],col[0]]
      if r==3:
        c.colors = [col[5],col[4],col[2],col[3],col[0],col[1]]
      if r==4:
        c.colors = [col[3],col[2],col[0],col[1],col[4],col[5]]
      if r==5:
        c.colors = [col[2],col[3],col[1],col[0],col[4],col[5]]


cube1 = cube()
#print cube1
#faces = cube1.give_faces()

#print cube1

#print cube1.faces_color()

cube1.print_face()

# succesion de 10 mouvements:
r = [random.randint(0,5) for i in xrange(10)]
c = [random.randint(0,3) for i in xrange(10)]

for rot,cr in zip(r,c):
  cube1.move(rot,cr)

cube1.print_face()

