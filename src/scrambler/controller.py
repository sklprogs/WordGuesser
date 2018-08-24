#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared        as sh
import sharedGUI     as sg
import scrambler.gui as gi

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordScrambler','../../resources/locale')


class Scrambler:

    def __init__(self):
        self.gui = gi.Scrambler()
        self.gui.close()
        self.bindings()
        
    def bindings(self):
        pass
    
    def show(self,event=None):
        self.gui.show()
    
    def close(self,event=None):
        self.gui.close()


if __name__ == '__main__':
    sg.objs.start()
    Scrambler().show()
    sg.objs.end()
