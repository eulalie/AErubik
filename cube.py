import random

random.seed(0)

cube = []
class s_cube:
    
    def __init__(self,pos,col):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.colors = col

    def __repr__(self):
        return str(self.x)+','+str(self.y)+','+str(self.z)+'   '+str(self.colors)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


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

    def give_faces(self):
        faces = [[],[],[],[],[],[]]
        for c in cube1.s_cubes:
            if c.x == -2:
                faces[0].append(c)
#                print '0',c.x,c.y,c.z
            if c.x == 2:
                faces[1].append(c)
#                print '1'
            if c.y == -2:
                faces[2].append(c)
#                print '2'
            if c.y == 2:
                faces[3].append(c)
#                print '3'
            if c.z == -2:
                faces[4].append(c)
#                print '4'
            if c.z == 2:
                faces[5].append(c)
            
            faces[0] = sorted(faces[0],key = lambda s_cube: (s_cube.y, s_cube.z))
            faces[1] = sorted(faces[1],key = lambda s_cube: (s_cube.y, s_cube.z))
            faces[2] = sorted(faces[2],key = lambda s_cube: (s_cube.x, s_cube.z))
            faces[3] = sorted(faces[3],key = lambda s_cube: (s_cube.x, s_cube.z))
            faces[4] = sorted(faces[4],key = lambda s_cube: (s_cube.x, s_cube.y))
            faces[5] = sorted(faces[5],key = lambda s_cube: (s_cube.x, s_cube.y))          

        return faces

    def faces_color(self):
        faces = self.give_faces()
        f_color = []
        for i,f in enumerate(faces):
            f_color.append([])
            for c in f:
                f_color[i].append(c.colors[i])

        return f_color

    def __repr__(self):
        res = ''
        faces = self.give_faces()
        for f in faces:
            for c in f:
                res += c.__repr__() + '\n'
            res += '\n ------ \n'

        return res

    def aff_colors(self):
        res = ''
        f_color = self.faces_color()
        for f in f_color:
            for col in f:
                res += col + ' '
            res += '\n ------ \n'

        print res


cube1 = cube()
#print cube1
faces = cube1.give_faces()

print cube1

cube1.aff_colors()

'''
print 'x0'
for c in facex0:
    print c

print 'y0'
for c in facey0:
    print c 

print 'z0'
for c in facez0:
    print c
'''
