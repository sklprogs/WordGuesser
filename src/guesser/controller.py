#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared.shared as sh
from skl_shared.localize import _

import guesser.logic as lg
import guesser.gui   as gi


class Guesser:

    def __init__(self):
        self.logic = lg.Guesser()
        self.gui   = gi.Guesser()
        self.set_bindings()
        
    def set_bindings(self):
        sh.com.bind (obj      = self.gui.ent1
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
            self.gui.lbl3.set_text('\n'.join(search))
        else:
            self.gui.lbl3.set_text(_('No match'))
        self.gui.update_scroll()


if __name__ == '__main__':
    sh.com.start()
    Guesser().show()
    sh.com.end()
