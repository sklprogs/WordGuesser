#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared.shared as sh
from skl_shared.localize import _

PRODUCT = 'WordGuesser'
VERSION = '1.0.1'
ICON = sh.objs.get_pdir().add('..','resources','icon_64x64_solve.gif')


class Menu:
    
    def __init__(self):
        self.set_gui()
        
    def set_gui(self):
        self.parent = sh.Top (icon  = ICON
                             ,title = sh.List([PRODUCT,VERSION]).space_items()
                             )
        self.set_buttons()
        self.set_bindings()
        
    def set_buttons(self):
        self.btn1 = sh.Button (parent = self.parent
                              ,text   = _('Word Guesser')
                              ,side   = 'top'
                              )
        self.btn2 = sh.Button (parent = self.parent
                              ,text   = _('Word Scrambler')
                              ,side   = 'top'
                              )
        self.btn1.focus()
        
    # If this does not work, set 'takefocus=1'
    def focus_next(self,event=None):
        event.widget.tk_focusNext().focus_set()
        return 'break'
        
    # If this does not work, set 'takefocus=1'
    def focus_prev(self,event=None):
        event.widget.tk_focusPrev().focus_set()
        return 'break'
    
    def set_bindings(self):
        sh.com.bind (obj      = self.parent
                    ,bindings = ['<Control-q>','<Control-w>','<Escape>']
                    ,action   = self.close
                    )
        sh.com.bind (obj      = self.parent
                    ,bindings = '<Down>'
                    ,action   = self.focus_next
                    )
        sh.com.bind (obj      = self.parent
                    ,bindings = '<Up>'
                    ,action   = self.focus_prev
                    )

    def show(self,event=None):
        self.parent.show()

    def close(self,event=None):
        self.parent.close()
    
    def set_title(self,text=None):
        if not text:
            text = _('Word Puzzles')
        self.parent.set_title(text)


if __name__ == '__main__':
    sh.com.start()
    Menu().show()
    sh.com.end()
