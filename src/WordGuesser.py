#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared.shared as sh
from skl_shared.localize import _

import menu.gui             as gi
import guesser.controller   as gc
import scrambler.controller as sc


class Menu:

    def __init__(self):
        self.gui = gi.Menu()
        self.set_bindings()
        
    def set_bindings(self):
        self.gui.btn1.action = objs.get_guesser().show
        self.gui.btn2.action = objs.get_scrambler().show
    
    def show(self,event=None):
        self.gui.show()
    
    def close(self,event=None):
        self.gui.close()



class Objects:
    
    def __init__(self):
        self.guesser = self.scrambler = None
    
    def get_guesser(self):
        if not self.guesser:
            self.guesser = gc.Guesser()
        return self.guesser
    
    def get_scrambler(self):
        if not self.scrambler:
            self.scrambler = sc.Scrambler()
        return self.scrambler


objs = Objects()


if __name__ == '__main__':
    sh.com.start()
    Menu().show()
    sh.com.end()
