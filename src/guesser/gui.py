#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared    as sh
import sharedGUI as sg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')

icon_path = sh.objs.pdir().add('..','resources','icon_64x64_solve.gif')


class Guesser:

    def __init__(self,width=400):
        self._width = width
        self.parent = sg.Top(parent=sg.objs.root())
        self.gui()
        
    def reset(self,text=_('No match')):
        self.ent1.clear_text()
        self.lbl3.text(text)
    
    def bindings(self):
        sg.bind (obj      = self.parent
                ,bindings = ['<Control-w>','<Control-q>','<Escape>']
                ,action   = self.close
                )
    
    def frames(self):
        self.frm  = sg.Frame (parent = self.parent)
        self.frm1 = sg.Frame (parent = self.frm
                             ,expand = False
                             )
        self.frm2 = sg.Frame (parent = self.frm
                             ,expand = False
                             ,propag = False
                             ,height = 100
                             )
        self.frmy = sg.Frame (parent = self.frm2
                             ,expand = False
                             ,fill   = 'y'
                             ,side   = 'right'
                             )
        self.frm3 = sg.Frame (parent = self.frm
                             ,expand = False
                             ,fill   = 'x'
                             ,side   = 'bottom'
                             )
        self.frmx = sg.Frame (parent = self.frm3
                             ,expand = False
                             ,fill   = 'x'
                             )
        self.frm4 = sg.Frame (parent = self.frm3
                             ,expand = False
                             ,fill   = 'x'
                             )
    
    def buttons(self):
        self.btn1 = sg.Button (parent = self.frm4
                              ,side   = 'left'
                              ,text   = _('Close')
                              ,hint   = _('Close this window')
                              ,action = self.close
                              )
        self.btn2 = sg.Button (parent = self.frm4
                              ,side   = 'right'
                              ,text   = _('Guess')
                              ,hint   = _('Guess missing characters in the word')
                              )
    
    def region(self,lines_no=1):
        self.cvs.region (x        = self._width
                        ,y        = 22 * lines_no
                        ,x_border = 5
                        ,y_border = 5
                        )
        self.cvs.scroll()
    
    def widgets(self):
        message   = _('Enter a word to guess. Use a question mark, a dot or an underscore to set a missing character.')
        message = list(message)
        for i in range(len(message)):
            if i % 50 == 0:
                message.insert(i,'\n')
        message = ''.join(message)
        self.lbl1 = sg.Label (parent = self.frm1
                             ,text   = message
                             ,expand = True
                             ,Close  = False
                             )
        self.ent1 = sg.Entry (parent    = self.frm1
                             ,Composite = True
                             ,expand    = True
                             ,fill      = 'x'
                             )
        self.lbl2 = sg.Label (parent = self.frm1
                             ,text   = _('Guessed words:')
                             ,expand = True
                             ,Close  = False
                             )
        self.cvs  = sg.Canvas (parent = self.frm2
                              ,expand = False
                              )
        self.frme = sg.Frame (parent = self.frm2
                             ,expand = False
                             )
        self.cvs.embed(self.frme)
        self.lbl3 = sg.Label (parent = self.frme
                             ,text   = _('No match')
                             ,expand = False
                             ,Close  = False
                             )
        self.ent1.focus()
        
    def scrollbars(self):
        self.xscr = sg.Scrollbar (parent     = self.frmx
                                 ,scroll     = self.cvs
                                 ,Horizontal = True
                                 )
        self.yscr = sg.Scrollbar (parent     = self.frmy
                                 ,scroll     = self.cvs
                                 )
    
    def gui(self):
        self.frames()
        self.widgets()
        self.buttons()
        self.bindings()
        self.icon()
        self.title()
        self.region()
        self.scrollbars()
    
    def icon(self,path=None):
        if not path:
            path = icon_path
        sg.WidgetShared.icon(self.parent,path)
    
    def title(self,text=None):
        if not text:
            text = _('Word Guesser')
        self.parent.title(text)
    
    def show(self,event=None):
        self.parent.show()
    
    def close(self,event=None):
        self.parent.close()



class Objects:
    
    def __init__(self):
        self._guesser = None
    
    def guesser(self):
        if not self._guesser:
            self._guesser = Guesser()
        return self._guesser


objs = Objects()


if __name__ == '__main__':
    sg.objs.start()
    guesser = Guesser()
    sg.objs.end()
