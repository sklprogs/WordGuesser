#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared2.shared as sh
from skl_shared2.localize import _

import scrambler.gui as gi


class Scrambler:

    def __init__(self):
        self.gui = gi.Scrambler()
        self.set_bindings()
        
    def set_bindings(self):
        pass
    
    def show(self,event=None):
        self.gui.show()
    
    def close(self,event=None):
        self.gui.close()


if __name__ == '__main__':
    sh.com.start()
    Scrambler().show()
    sh.com.end()
