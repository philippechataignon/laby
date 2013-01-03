#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import laby

LARGEUR = 60
HAUTEUR = 30
TITRE = "Laby"
SIZE = 30

def init(s) :
    lab = laby.Laby(HAUTEUR, LARGEUR)
    lab.make()
    s.fill(white)
    draw_grille(s, lab)
    pygame.display.update()
    return lab

def draw_grille(s, lab):
    for l in range(1, lab.nb_lig):
        for c in range(lab.nb_col):
            if lab.murs_h[(l, c)]:
                pygame.draw.line(s, black, (c*SIZE, l*SIZE), ((c+1)*SIZE, l*SIZE), 1)
    for l in range(lab.nb_lig):
        for c in range(1, lab.nb_col):
            if lab.murs_v[(l, c)]:
                pygame.draw.line(s, black, (c*SIZE, l*SIZE), (c*SIZE, (l+1)*SIZE), 1)
    pygame.display.update()

def draw_solution(s, lab):
    coord_sol = [lab.from_seq(n) for n in lab.solution()]
    for y, x in coord_sol :
        pygame.draw.circle(s, red, (x*SIZE + SIZE/2, y*SIZE + SIZE/2), SIZE/4, 0)
    pygame.display.update()

def draw_point(s, col) :
    x = pygame.mouse.get_pos()[0]/SIZE
    y = pygame.mouse.get_pos()[1]/SIZE
    pygame.draw.circle(s, col, (x*SIZE + SIZE/2, y*SIZE + SIZE/2), SIZE/4, 0)
    pygame.display.update()

def clear(s):
    for y in range(lab.nb_lig):
        for x in range(lab.nb_col):
            pygame.draw.circle(s, white, (x*SIZE + SIZE/2, y*SIZE + SIZE/2), SIZE/4, 0)
    pygame.display.update()

def loop():
    clock = pygame.time.Clock()
    fps = 100
    active = True
    while active :
        event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            active = False
        elif pygame.mouse.get_pressed() == (0, 1, 0):
            draw_solution(screen, lab)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            draw_point(screen, green)
        elif pygame.mouse.get_pressed() == (0, 0, 1):
            draw_point(screen, white)
        elif event.type == KEYDOWN and event.key == K_SPACE:
            lab = init(screen)
        elif pygame.mouse.get_pressed() == (0, 1, 1):
            clear(screen)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR * SIZE, HAUTEUR * SIZE))
    pygame.display.set_caption(TITRE)
    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    lab = init(screen)
    loop()
