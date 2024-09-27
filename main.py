
import pygame
import random
from gl import Raytracer
from shapes import Sphere , Plane, Disk
from lights import *
from materials import *

height = 600
width = 800

pixels= []


pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

envMapFile = "env1.bmp"
metalTexture="metal.bmp"
waveTexture="env3.bmp"
snowTextureFile="snow.bmp"
clayTextureFile = "clay.bmp"
# pixels= [[self.bgColor for x in range(self.width)] for y in range(self.height)]

myRaytracer =  Raytracer(screen,envMapFile)
myRaytracer.rtClearColor(0.09,0.2,0.5)

DIFUSE =0
REFLECTIVE = 1
TRANSPARENT = 2

brick = Material(difuse = (0.5,0.1,0),specular=0.2,type=DIFUSE)
snow= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE , texture=snowTextureFile)
water= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE , texture=waveTexture)
black= Material(difuse=(0.1,0.1,0.1),specular=0.5,type=DIFUSE)
carrot = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=DIFUSE)
mirror = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=REFLECTIVE)
metal = Material(difuse=(0.9,0.5,0.2), specular=0.5,type=DIFUSE, texture=metalTexture)

clay= Material(difuse=(1,1,1),specular=0.99,type=DIFUSE , texture=clayTextureFile)




materials= [brick,snow,black,carrot, mirror]

myRaytracer.objects.append( Sphere(position=(0,-2,-7), radius =1.5, material = snow))
# myRaytracer.objects.append( Sphere(position=(-2,0,-5), radius =1.5, material = metal))
myRaytracer.objects.append( Sphere(position=(2,0,-5), radius =1, material = mirror))

# myRaytracer.objects.append( Plane(position=(-5,0,-50),normal=(1,0,0), material= mirror))
# myRaytracer.objects.append( Plane(position=(0,-10,-0),normal=(0,1,0), material= brick))

# myRaytracer.objects.append( Disk(position=(-5,0,-50),material= mirror , normal=(1,0,0) ,radius=5))
myRaytracer.objects.append( Sphere(position=(0,0,-10), radius =5 ,material = mirror))

myRaytracer.objects.append( Sphere(position=(-7,-3, -2), radius =1.5, material = clay))


# numofspheres = 10

# for x in range (numofspheres):
#     minx=-2
#     miny=-2
#     maxx=2
#     maxy=2
#     maxz=-2
#     minz=-7
    
#     x= random.randint(minx,maxx)
#     y= random.randint(miny,maxy)
#     z= random.randint(minz,maxz)
    
#     myRaytracer.objects.append( Sphere(position=(x,y,z), radius =random.random(), material = materials[random.randint(0,len(materials)-1)]))


# myRaytracer.objects.append( Sphere(position=(3,0,-5), radius =1.5, material = brick))


myRaytracer.Lights.append( AmbientLight(intensity = 0.1))
# myRaytracer.Lights.append (DirectionalLight(direction=(-0.9,-1,-2),intensity=0.4))
myRaytracer.Lights.append (DirectionalLight(direction=(-0.9,-1,-2),intensity=0.4))


myRaytracer.rtClear()
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

   
    # screen.fill("black")
    # pygame.draw.circle(screen, "white", [width/2, height/2] , 40)

    
    
    # myRaytracer.rtPoint(random.randint(0,width),random.randint(0,height),(1,1,0))
    
    time= pygame.time.get_ticks()
    # print(time)
    factor=6
    # for light in myRaytracer.Lights:
    #     if light.LightType =="Directional":  
    #         movement = [math.sin(time)/factor,0,0]
    #         light.moveObject(movement)
    myRaytracer.rtRender()
    pygame.display.flip()
    
    # clock.tick(60) 

pygame.quit()