#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared2.shared as sh
from skl_shared2.localize import _

PRODUCT = 'WordGuesser'
VERSION = '1.0.1'
ICON = sh.objs.get_pdir().add('..','resources','icon_64x64_solve.gif')


class Guesser:

    def __init__(self,width=400):
        self.width = width
        self.set_gui()
        
    def reset(self,text=_('No match')):
        self.ent1.clear_text()
        self.lbl3.set_text(text)
    
    def set_bindings(self):
        sh.com.bind (obj      = self.parent
                    ,bindings = ['<Control-w>','<Control-q>','<Escape>']
                    ,action   = self.close
                    )
    
    def set_frames(self):
        self.frm  = sh.Frame (parent = self.parent)
        self.frm1 = sh.Frame (parent = self.frm
                             ,expand = False
                             )
        self.frm2 = sh.Frame (parent = self.frm
                             ,expand = False
                             ,propag = False
                             ,height = 100
                             )
        self.frmy = sh.Frame (parent = self.frm2
                             ,expand = False
                             ,fill   = 'y'
                             ,side   = 'right'
                             )
        self.frm3 = sh.Frame (parent = self.frm
                             ,expand = False
                             ,fill   = 'x'
                             ,side   = 'bottom'
                             )
        self.frmx = sh.Frame (parent = self.frm3
                             ,expand = False
                             ,fill   = 'x'
                             )
        self.frm4 = sh.Frame (parent = self.frm3
                             ,expand = False
                             ,fill   = 'x'
                             )
    
    def set_buttons(self):
        self.btn1 = sh.Button (parent = self.frm4
                              ,side   = 'left'
                              ,text   = _('Close')
                              ,hint   = _('Close this window')
                              ,action = self.close
                              )
        self.btn2 = sh.Button (parent = self.frm4
                              ,side   = 'right'
                              ,text   = _('Guess')
                              ,hint   = _('Guess missing characters in the word')
                              )
    
    def set_region(self,height=20):
        self.cvs.set_region (x       = self.width
                            ,y       = height
                            ,xborder = 5
                            ,yborder = 5
                            )
        self.cvs.scroll()
    
    def update_scroll(self):
        sh.objs.get_root().update_idle()
        height = self.lbl3.get_reqheight()
        self.set_region(height=height)
    
    def set_widgets(self):
        message = _('Enter a word to guess. Use a question mark, a dot or an underscore to set a missing character.')
        message = list(message)
        for i in range(len(message)):
            if i % 50 == 0:
                message.insert(i,'\n')
        message = ''.join(message)
        self.lbl1 = sh.Label (parent = self.frm1
                             ,text   = message
                             ,expand = True
                             )
        self.ent1 = sh.Entry (parent = self.frm1
                             ,expand = True
                             ,fill   = 'x'
                             )
        self.lbl2 = sh.Label (parent = self.frm1
                             ,text   = _('Guessed words:')
                             ,expand = True
                             )
        self.cvs = sh.Canvas (parent = self.frm2
                             ,expand = False
                             )
        self.frme = sh.Frame (parent = self.frm2
                             ,expand = False
                             )
        self.cvs.embed(self.frme)
        self.lbl3 = sh.Label (parent = self.frme
                             ,text   = _('No match')
                             ,expand = False
                             )
        self.ent1.set_focus()
        
    def set_scroll(self):
        self.xscr = sh.Scrollbar (parent = self.frmx
                                 ,scroll = self.cvs
                                 ,Horiz  = True
                                 )
        self.yscr = sh.Scrollbar (parent = self.frmy
                                 ,scroll = self.cvs
                                 )
    
    def set_gui(self):
        self.parent = sh.Top (icon   = ICON
                             ,title  = sh.List([PRODUCT,VERSION]).space_items()
                             ,AutoCr = False
                             )
        self.set_frames()
        self.set_widgets()
        self.set_buttons()
        self.set_region()
        self.set_scroll()
        self.set_bindings()
        self.cvs.set_top_bindings(self.parent)
        self.parent.center()
        self.close()
    
    def show(self,event=None):
        self.parent.show()
    
    def close(self,event=None):
        self.parent.close()


if __name__ == '__main__':
    sh.com.start()
    guesser = Guesser()
    sh.com.end()
