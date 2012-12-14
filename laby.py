#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

class Laby(object) :
    def __init__(self, nb_lig, nb_col) :
        self.nb_lig = nb_lig
        self.nb_col = nb_col
        self.max_seq = nb_lig * nb_col
        self.grille = {(r, c): self.to_seq(r, c) for r in range(nb_lig) for c in range(nb_col)}
        self.murs_v = {(r, c): True for r in range(nb_lig) for c in range(nb_col+1)}
        self.murs_h = {(r, c): True for r in range(nb_lig+1) for c in range(nb_col)}

    def to_seq(self, r, c) :
        return c + self.nb_col * r + 1 

    def from_seq(self, n) :
        return (n-1) / self.nb_col, (n-1) % self.nb_col

    def affiche_seq(self) :
        for l in range(self.nb_lig) :
            for c in range(self.nb_col) :
                print("%03d" % self.grille.get((l, c), 0), end="")
            print()

    def affiche(self) :
        for l in range(self.nb_lig+1) :
            for c in range(self.nb_col) :
                print(u' \u2014' if self.murs_h[l, c] else '  ', end="")
            print()
            if l >= self.nb_lig :
                break
            for c in range(self.nb_col+1) :
                print('| ' if self.murs_v[l, c] else '  ', end="")
            print()
l = Laby(4, 5)
l.affiche()

# print l.from_seq(13)
