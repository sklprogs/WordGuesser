#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared    as sh
import sharedGUI as sg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')


class Guesser:

    def __init__(self):
        self.values()
        self.load()
    
    def values(self):
        self.Success = True
        self.file    = sh.objs.pdir().add('..','user','words.txt')
        self.lst     = []
        self.word    = ''
    
    def reset(self,word):
        f = 'guesser.logic.Guesser.reset'
        if word:
            if isinstance(word,str):
                self.word = word.replace(' ','')
                self.word = self.word.lower()
                self.word = self.word.replace('.','?').replace('_','?').replace('*','?')
            else:
                sh.objs.mes (f,_('ERROR')
                            ,_('Wrong input data!')
                            )
        else:
            sh.com.empty(f)
    
    def search(self):
        f = 'guesser.logic.Guesser.search'
        if self.Success:
            if self.word:
                timer = sh.Timer(func_title=f)
                timer.start()
                lst = [word for word in self.lst \
                       if len(word) == len(self.word)
                      ]
                timer.end()
                words = []
                for item in lst:
                    Match    = True
                    item_lst = list(item)
                    for i in range(len(self.word)):
                        if self.word[i] != '?':
                            if self.word[i] != item_lst[i]:
                                Match = False
                                break
                    if Match:
                        words.append(item)
                return words
            else:
                sh.com.empty(f)
        else:
            sh.com.cancel(f)
    
    def load(self):
        f = 'guesser.logic.Guesser.load'
        if self.Success:
            if not self.lst:
                timer = sh.Timer(func_title=f)
                timer.start()
                iread        = sh.ReadTextFile(self.file)
                text         = iread.get()
                self.Success = iread.Success
                if self.Success:
                    text     = text.lower()
                    text     = text.strip()
                    self.lst = text.splitlines()
                timer.end()
            return self.lst
        else:
            sh.com.cancel(f)


if __name__ == '__main__':
    sh.objs.mes(Silent=1)
    guesser = Guesser()
