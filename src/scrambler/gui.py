#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared    as sh
import sharedGUI as sg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')

icon_path = sh.objs.pdir().add('..','resources','icon_64x64_solve.gif')


class Scrambler:

    def __init__(self,width=400):
        self._width = width
        self.parent = sg.Top(parent=sg.objs.root())
        self.gui()
        
    def bindings(self):
        sg.bind (obj      = self.parent
                ,bindings = ['<Control-w>','<Control-q>','<Escape>']
                ,action   = self.close
                )
    
    def gui(self):
        sg.Label (parent = self.parent
                 ,text   = _('Not implemented yet!')
                 ,Close  = False
                 )
        self.icon()
        self.title()
        self.bindings()
    
    def icon(self,path=None):
        if not path:
            path = icon_path
        sg.WidgetShared.icon(self.parent,path)
    
    def title(self,text=None):
        if not text:
            text = _('Word Scrambler')
        self.parent.title(text)
    
    def show(self,event=None):
        self.parent.show()
    
    def close(self,event=None):
        self.parent.close()


if __name__ == '__main__':
    sg.objs.start()
    Scrambler().show()
    sg.objs.end()
