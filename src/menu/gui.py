#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared    as sh
import sharedGUI as sg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')

icon_path = sh.objs.pdir().add('..','resources','icon_64x64_solve.gif')


class Menu:
    
    def __init__(self):
        self.gui()
        
    def gui(self):
        self.parent = sg.objs.new_top()
        self.buttons()
        self.icon()
        self.title()
        self.bindings()
        
    def icon(self,path=None):
        if not path:
            path = icon_path
        sg.WidgetShared.icon(self.parent,path)
        
    def buttons(self):
        self.btn1 = sg.Button (parent = self.parent
                              ,text   = _('Word Guesser')
                              ,side   = 'top'
                              )
        self.btn2 = sg.Button (parent = self.parent
                              ,text   = _('Word Scrambler')
                              ,side   = 'top'
                              )
        self.btn1.focus()
        
    # If this does not work, set 'takefocus=1'
    def focus_next(self,event=None):
        event.widget.tk_focusNext().focus()
        return 'break'
        
    # If this does not work, set 'takefocus=1'
    def focus_prev(self,event=None):
        event.widget.tk_focusPrev().focus()
        return 'break'
    
    def bindings(self):
        sg.bind (obj      = self.parent
                ,bindings = ['<Control-q>','<Control-w>','<Escape>']
                ,action   = self.close
                )
        sg.bind (obj      = self.parent
                ,bindings = '<Down>'
                ,action   = self.focus_next
                )
        sg.bind (obj      = self.parent
                ,bindings = '<Up>'
                ,action   = self.focus_prev
                )

    def show(self,event=None):
        self.parent.show()

    def close(self,event=None):
        self.parent.close()
    
    def title(self,text=None):
        if not text:
            text = _('Word Puzzles')
        self.parent.title(text)


if __name__ == '__main__':
    sg.objs.start()
    Menu().show()
    sg.objs.end()
