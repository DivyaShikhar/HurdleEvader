import pygame
import random
import math

pygame.init()

screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("Car Lap")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Grass
grass=pygame.image.load("grass.png")

life=1000

#Player
carimg=pygame.image.load("car.png")
carx=220
cary=520
car_change=0

#Holes
holes=pygame.image.load("hole.png")
holex=random.randint(90, 345)
holey=0
car_change=0

#Life
heart=pygame.image.load("life.png")
lifex=random.randint(90, 345)
lifey=0
life_change=0


def car(x,y):
    screen.blit(carimg,(x,y))

def hole(x,y):
    screen.blit(holes, (x,y))

def lifes(x,y):
    screen.blit(heart,(x,y))

def collide(holex,holey,carx,cary):
    dist = math.sqrt(math.pow(holex - carx, 2) + math.pow(holey - cary, 2))
    if dist<35:
        return True
    else:
        return False




driving = True
while driving:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            driving = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                car_change=-0.2
                print(carx)
            if event.key == pygame.K_RIGHT:
               car_change=0.2
               print(carx)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_change=0
    carx += car_change
    holey+=0.2

    if carx<90:
        life-=1
    elif carx>350:
        life -= 1
    if life==0:
        quit()
    screen.fill((0,0,0))
    screen.blit(grass,(-500,0))
    screen.blit(grass, (400, 0))

    coll=collide(holex,holey,carx,cary)
    if coll:
        life-=1

    if holey>500:
        holex = random.randint(90, 345)
        holey = 0
        print("Yes")

    if life< 500:
        lifes(lifex, lifey)
        lifey+=0.2
        print("life")
        dist1 = math.sqrt(math.pow(lifex - carx, 2) + math.pow(lifey - cary, 2))
        if dist1 < 35:
            life+=200

#Result
    car(carx,cary)
    hole(holex,holey)

    pygame.display.update()
    print(life)