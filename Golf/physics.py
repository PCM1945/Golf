import math


def ballpath(startx, starty, power, ang, time):
    angle = ang
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    distX = velx * time
    distY = (vely * time) + ((-9.8 * (time ** 2)) / 2)

    newx = round(distX + startx)
    newy = round(starty - distY)

    return distY


def findpower(power, angle, time):
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power

    vfy = vely + (-9.8 * time)
    vf = math.sqrt((vfy**2) + (velx**2))

    return vf


def findangle(power, angle):
    vely = math.sin(angle) * power
    velx = math.cos(angle) * power

    ang = math.atan(abs(vely) / abs(velx))

    return ang


def maxtime(power):
    time = ((power * -1) - (math.sqrt(power**2))) / -9.8

    return time / 2


def linearspeed(velx, vely):
    linear = math.sqrt(vely + velx)
    return linear

def maxalt(power, angle):
    velx = math.cos(angle) * power
    vely = math.sin(angle) * power
    speed = vely/velx
    h = (pow(speed, 2)* pow(math.sin(angle), 2))/ 2*9.8
    return h
