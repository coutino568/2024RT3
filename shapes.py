
from mathcou import *
from numpy import arccos, arctan2,pi,cos,sin
import numpy as np

class Intercept(object):
    def __init__(self,distance, point,normal,obj , texcoords):
        self.distance= distance
        self.point= point
        self.normal = normal
        self.obj= obj
        self.texcoords = texcoords








class Shape(object):
    
    def __init__( self, position, material ):
        self.position = position
        self.material= material
        
        
        
    def ray_intersect(self, origin, dir):
        return False
    
    def moveObject(self, movement):
        self.position= add(self.position,movement)
        
    
class Sphere (Shape):
    
    def __init__(self, position,  material ,radius):
        self.radius =radius
        # self.material= material
        super().__init__( position,material)
        
    def ray_intersect(self, origin, direction):
        direction = normalize(direction)
        Lr = subtract(self.position, origin)
        # print(L)
        # print(direction)
        magnitudL = getmagnitude(Lr)
        tca= dotProduct(Lr, direction)
        d = math.sqrt((magnitudL * magnitudL ) - (tca * tca ) )
        
        if d> self.radius:
            
            return None
        
        thc = math.sqrt((self.radius* self.radius) - (d*d) )
        t0 = tca-thc
        t1 = tca+ thc
        
        if (t0<0):
            t0=t1
        if (t0<0):     
            return None
        # print(t0)
        # print(direction)
        res1= vectorAndScalarMultiplication(direction,t0)
        point = add(origin,  res1 )
        normal = normalize(subtract(point, self.position))
        
        
        
        
        
        texcoords= None
        
        ##si tiene material con textura entonces se devuelve
        if self.material.texture != None:
            
            directionFromInside = normalize(subtract(self.position, point))
            # print(directionFromInside)
            v = arctan2(directionFromInside[2],directionFromInside[0]) / (2*np.pi)
            u = arccos(-directionFromInside[1]) / np.pi
        
        
            # x =int(v*(self.material.texture.width-1))
            # y = int(u*(self.material.texture.height-1))
            
            texcoords= [u,v]
            # print(texcoords)
        
        
        
        
        
        return Intercept(distance=t0,
                         point=point,
                         normal=normal,
                         obj = self,
                         texcoords=texcoords)
        
class Plane (Shape):
    
    def __init__(self, position, normal , material):
        
        self.normal = normalize(normal)
        self.material= material
        super().__init__(position,material)
        
    def ray_intersect(self, origin, direction):
        
        # print("origin")
        # print(origin)
        # print("direction")
        # print(direction)
        # print("normal")
        # print(self.normal)
        
        
        denom= dotProduct( direction, self.normal)
        
        # print("denom")
        # print(denom)
        
        if abs(denom) <= 0.0001 :
            return None
        # num = 
        # substartcito = np.subtract(self.position,origin)
        # print("num")
        
        # print(num)
        
        # print("hecho por numy es")
        # print(substartcito)
        num = dotProduct(subtract(self.position, origin), self.normal)
        
        
        # print("num")
        # petunia
        # print(num)
        # num = np.dot(np.subtract(self.position,origin),self.normal)
        # print("num")
        
        # print(num)
        # print("denom")
        # print(denom)
        
        t = num / denom
        # print("t")
        # print(t)
        if t< 0 :
            return None
        
        point = add(origin , vectorAndScalarMultiplication(direction, t) )
        # print ( point)
        return Intercept(distance=t,
                         point=point,
                         normal=self.normal,
                         obj = self,
                         texcoords=None)
    
    
class Disk(Plane):
    def __init__(self, position, material , normal,radius):
        self.radius = radius
        super().__init__( position, material , normal)
        
    def ray_intersect(self, origin, direction):
        
        planeIntersect = super().ray_intersect(origin,direction)
        
        if planeIntersect == None:
            return None
        
        contactDistance = subtract(planeIntersect.point,self.position)
        contactDistance = normalize(contactDistance)
        
        if contactDistance > self.radius:
            return None
        
        if self.material.texture!= None:
            
            angle= dotProduct(self.origin, planeIntersect.point)
            magnitude= subtract()
            x= cos(angle)* magnitude
            y= sin(angle)*magnitude
            
            
            texcoords = [x*self.material.texture.width, y*self.material.texture.height]
        else:
            texcoords = None        
        
        return Intercept(distance=planeIntersect.distance,
                         point=planeIntersect.point,
                         texcoords = texcoords,
                         normal=self.normal,
                         obj = self
                         )
        
        
        
        
        
    
class Triangle(Shape):
    
    def __init__(self, vertices , position, material):
        self.vertices =vertices
        
        # self.material= material
        super().__init__( position,material)
        
    def ray_intersect(self, origin, direction):
        
        v0=self.vertices[0]
        v1=self.vertices[1]
        v2=self.vertices[2]
        
        
        
        
        return None