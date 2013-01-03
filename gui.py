#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

import laby

LARGEUR = 10
HAUTEUR = 8
TITRE = "Laby"
SIZE = 50

def draw_grille(s, lab) :
    for l in range(1, lab.nb_lig):
        for c in range(lab.nb_col):
            if lab.murs_h[(l, c)] :
                pygame.draw.line(s, black, (c*SIZE, l*SIZE), ((c+1)*SIZE, l*SIZE), 1)
    for l in range(lab.nb_lig):
        for c in range(1, lab.nb_col):
            if lab.murs_v[(l, c)] :
                pygame.draw.line(s, black, (c*SIZE, l*SIZE), (c*SIZE, (l+1)*SIZE), 1)

def loop():
    clock = pygame.time.Clock()
    fps = 100
    active = True
    while active :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                active = False
        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    lab = laby.Laby(HAUTEUR, LARGEUR)
    lab.make()

    pygame.init()
    screen = pygame.display.set_mode((LARGEUR * SIZE, HAUTEUR * SIZE))
    pygame.display.set_caption(TITRE)

    white = pygame.Color(255, 255, 255)
    black = pygame.Color(0, 0, 0)
    screen.fill(white)
    draw_grille(screen, lab)
    loop()
