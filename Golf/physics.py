import math


def ballpath(startx, starty, v0, angle, time):  # função que retorna as equações de posição horaria
    # equações de decomposição da velocidade
    vel_x = math.cos(angle) * v0
    vel_y = math.sin(angle) * v0
# equações de movimento retilineo e obliquo respectivamente
    dist_x = vel_x * time
    dist_y = (vel_y * time) + ((-9.8 * (time ** 2)) / 2)
# essas duas variaveis a baixo retornam as posisões que a bola se mexe no pygame
    new_x = round(dist_x + startx)
    new_y = round(starty - dist_y)
    return dist_y


def linearspeed(v0, angle, time):  # função que retorna a velocidade linear do projetil
    # equações de decomposição da velocidade
    vel_x = math.cos(angle) * v0
    vel_y = math.sin(angle) * v0
    # equações que retornam  a velocidade linear e y e geral do progetil
    vfy = vel_y + (-9.8 * time)
    vf = math.sqrt(pow(vfy, 2) + pow(vel_x, 2))
    return vf


def findangle(v0, angle):  # função que retorna o angulo de lançamento do projetil
    # equações de decomposição da velocidade
    vel_y = math.sin(angle) * v0
    vel_x = math.cos(angle) * v0
    ang = math.atan(abs(vel_y) / abs(vel_x))
    return ang


def maxtime(v0): # função que retona o tempo maximo do lançamento
    time = ((v0 * -1) - (math.sqrt(pow(v0, 2))) / -9.8)
    return time / 2


def maxalt(v0, angle,):  # função que retorna a altura mxima do lamçamento
    h = (pow(v0, 2) * pow(math.sin(angle), 2)) / 2*9.8
    return h
