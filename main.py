
import pygame
import random
from gl import Raytracer
from shapes import Sphere , Plane, Disk , AABB
from lights import *
from materials import *

height = 600
width = 800

pixels= []


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

envMapFile = "env3.bmp"
metalTexture="metal.bmp"
waveTexture="env3.bmp"
snowTextureFile="snow.bmp"
clayTextureFile = "clay.bmp"
brickTextureFile = "bricks.bmp"
# pixels= [[self.bgColor for x in range(self.width)] for y in range(self.height)]

myRaytracer =  Raytracer(screen,envMapFile)
myRaytracer.rtClearColor(0.09,0.2,0.5)

DIFUSE =0
REFLECTIVE = 1
TRANSPARENT = 2

brick = Material(difuse = (0.5,0.1,0),specular=0.2,type=DIFUSE ,texture= brickTextureFile)
snow= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE )
water= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE , texture=waveTexture)
black= Material(difuse=(0.1,0.1,0.1),specular=0.5,type=DIFUSE)
carrot = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=DIFUSE)
mirror = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=REFLECTIVE)
metal = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=DIFUSE, texture=metalTexture)

clay= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE , texture=clayTextureFile)




materials= [brick,snow,black,carrot, mirror]



##leftandright
myRaytracer.objects.append( Plane(position=(-20,0,-50),normal=(1,0,0), material= snow))
myRaytracer.objects.append( Plane(position=(20,0,-50),normal=(-1,0,0), material= snow))
#back
myRaytracer.objects.append( Plane(position=(0,-8,-50),normal=(0,0,1), material= snow))
#bottom and top
myRaytracer.objects.append( Plane(position=(0,8,-6),normal=(0,-1,0), material= snow))
myRaytracer.objects.append( Plane(position=(0,-8,-6),normal=(0,1,0), material= snow))


#discos
myRaytracer.objects.append( Disk(position=(1,-3,-10), normal = (1,0,1) , material= carrot  ,radius=2))
myRaytracer.objects.append( Disk(position=(-2,-2,-5), normal = (0,1,0) , material= carrot  ,radius=1))


#luces
myRaytracer.Lights.append( AmbientLight(intensity = 0.1))
myRaytracer.Lights.append (DirectionalLight(direction=(-0.9,-1,-2),intensity=0.4))
myRaytracer.Lights.append (DirectionalLight(direction=(-0.2,-1,-1),intensity=0.4))


myRaytracer.rtClear()
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

   
    time= pygame.time.get_ticks()

    myRaytracer.rtRender()
    pygame.display.flip()
    
  

pygame.quit()