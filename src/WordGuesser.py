#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared               as sh
import sharedGUI            as sg
import menu.gui             as gi
import guesser.controller   as gc
import scrambler.controller as sc

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')


class Menu:

    def __init__(self):
        self.gui = gi.Menu()
        self.bindings()
        
    def bindings(self):
        self.gui.btn1.action = objs.guesser().show
        self.gui.btn2.action = objs.scrambler().show
    
    def show(self,event=None):
        self.gui.show()
    
    def close(self,event=None):
        self.gui.close()



class Objects:
    
    def __init__(self):
        self._guesser = self._scrambler = None
    
    def guesser(self):
        if not self._guesser:
            self._guesser = gc.Guesser()
        return self._guesser
    
    def scrambler(self):
        if not self._scrambler:
            self._scrambler = sc.Scrambler()
        return self._scrambler


objs = Objects()


if __name__ == '__main__':
    sg.objs.start()
    Menu().show()
    sg.objs.end()
