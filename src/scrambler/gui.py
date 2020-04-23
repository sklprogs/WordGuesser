#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared.shared as sh
from skl_shared.localize import _

ICON = sh.objs.get_pdir().add('..','resources','icon_64x64_solve.gif')


class Scrambler:

    def __init__(self,width=400):
        self.width = width
        self.set_gui()
        
    def set_bindings(self):
        sh.com.bind (obj      = self.parent
                    ,bindings = ['<Control-w>','<Control-q>','<Escape>']
                    ,action   = self.close
                    )
    
    def set_gui(self):
        self.parent = sh.Top (icon   = ICON
                             ,title  = _('Word Scrambler')
                             )
        sh.Label (parent = self.parent
                 ,text   = _('Not implemented yet!')
                 )
        self.set_bindings()
        self.parent.center()
        self.close()
    
    def show(self,event=None):
        self.parent.show()
    
    def close(self,event=None):
        self.parent.close()


if __name__ == '__main__':
    sh.com.start()
    Scrambler().show()
    sh.com.end()
