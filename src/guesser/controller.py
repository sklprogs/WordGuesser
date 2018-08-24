#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared        as sh
import sharedGUI     as sg
import guesser.logic as lg
import guesser.gui   as gi

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../../resources/locale')


class Guesser:

    def __init__(self):
        self.logic = lg.Guesser()
        self.gui   = gi.Guesser()
        self.bindings()
        
    def bindings(self):
        sg.bind (obj      = self.gui.ent1
                ,bindings = ['<Return>','<KP_Enter>']
                ,action   = self.guess
                )
        self.gui.btn2.action = self.guess
    
    def show(self,event=None):
        self.gui.show()
    
    def close(self,event=None):
        self.gui.close()
    
    def guess(self,event=None):
        word = self.gui.ent1.get()
        self.logic.reset(word=word)
        search = self.logic.search()
        if search:
            self.gui.lbl3.text('\n'.join(search))
        else:
            self.gui.lbl3.text(_('No match'))


if __name__ == '__main__':
    sg.objs.start()
    guesser = Guesser()
    guesser.show()
    sg.objs.end()
