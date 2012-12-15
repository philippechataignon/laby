#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import networkx as nx
import random


class Laby(object) :
    def __init__(self, nb_lig, nb_col) :
        self.nb_lig = nb_lig
        self.nb_col = nb_col
        self.max_seq = nb_lig * nb_col
        self.grille = {(r, c): self.to_seq(r, c) for r in range(nb_lig) for c in range(nb_col)}
        self.murs_v = {(r, c): 2 if c==0 or c==nb_col else 1 for r in range(nb_lig) for c in range(nb_col+1)}
        self.murs_h = {(r, c): 2 if r==0 or r==nb_lig else 1 for r in range(nb_lig+1) for c in range(nb_col)}
        self.del_murs = 0
        self.chemin = []

    def to_seq(self, r, c) :
        return c + self.nb_col * r + 1 

    def from_seq(self, n) :
        return (n-1) / self.nb_col, (n-1) % self.nb_col

    def affiche(self, seq=True) :
        scale = 6
        for l in range(self.nb_lig+1) :
            for c in range(self.nb_col) :
                print(u'\u2014'*scale if self.murs_h[l, c] else ' '*scale, end="")
            print()
            if l >= self.nb_lig :
                break
            for c in range(self.nb_col) :
                if seq :
                    print(('|' if self.murs_v[l, c] else ' ') + ' %3s ' % self.grille[l, c], end="")
                else :
                    print(('|' if self.murs_v[l, c] else ' ') + '    ', end="")
            print('|' if self.murs_v[l, self.nb_col] else '', end="")
            print()

    def grille_change(self, fr, to) :
        for key, val in self.grille.iteritems() :
            if val == fr :
                self.grille[key] = to

    def mur_alea(self) :
        v = random.randint(0, 1)
        l = random.randrange(self.nb_lig+1)
        c = random.randrange(self.nb_col+1)

        if v and self.murs_v.get((l, c)) == 1 :
            c1 = self.grille[l, c-1]
            c2 = self.grille[l, c]
            if c1 != c2 :
                self.chemin.append((self.to_seq(l, c-1), self.to_seq(l, c)))
                self.murs_v[(l, c)] = 0
                self.grille_change(c1, c2)
                self.del_murs += 1
        elif not v and self.murs_h.get((l, c)) == 1 :
            c1 = self.grille[l-1, c]
            c2 = self.grille[l, c]
            if c1 != c2 :
                self.chemin.append((self.to_seq(l-1, c), self.to_seq(l, c)))
                self.murs_h[(l, c)] = 0
                self.grille_change(c1, c2)
                self.del_murs += 1

    def make(self) :
        while self.del_murs <  self.nb_col * self.nb_lig - 1:
            self.mur_alea()
        G = nx.Graph()
        for c1, c2 in self.chemin :
            G.add_edge(c1 ,c2)
        self.grille = {(r, c): ' '  for r in range(l.nb_lig) for c in range(l.nb_col)}
        solution = nx.shortest_path(G,source=1,target=self.max_seq)
        for seq in solution :
            self.grille[self.from_seq(seq)] = 'X'
        self.affiche()

l = Laby(30, 35)
l.make()
