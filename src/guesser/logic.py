#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import skl_shared.shared as sh
from skl_shared.localize import _


class Guesser:

    def __init__(self):
        self.set_values()
        self.load()
    
    def set_values(self):
        self.Success = True
        self.file = sh.objs.get_pdir().add('..','user','words.txt')
        self.lst = []
        self.word = ''
    
    def reset(self,word):
        f = '[WordGuesser] guesser.logic.Guesser.reset'
        if word:
            if isinstance(word,str):
                self.word = word.replace(' ','')
                self.word = self.word.lower()
                self.word = self.word.replace('.','?').replace('_','?')
                self.word = self.word.replace('*','?')
            else:
                mes = _('Wrong input data!')
                sh.objs.get_mes(f,mes).show_warning()
        else:
            sh.com.rep_empty(f)
    
    def search(self):
        f = '[WordGuesser] guesser.logic.Guesser.search'
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
                    Match = True
                    items = list(item)
                    for i in range(len(self.word)):
                        if self.word[i] != '?':
                            if self.word[i] != items[i]:
                                Match = False
                                break
                    if Match:
                        words.append(item)
                return words
            else:
                sh.com.rep_empty(f)
        else:
            sh.com.cancel(f)
    
    def load(self):
        f = '[WordGuesser] guesser.logic.Guesser.load'
        if self.Success:
            if not self.lst:
                timer = sh.Timer(f)
                timer.start()
                iread = sh.ReadTextFile(self.file)
                text = iread.get()
                self.Success = iread.Success
                if self.Success:
                    text = text.lower()
                    text = text.strip()
                    self.lst = text.splitlines()
                timer.end()
            return self.lst
        else:
            sh.com.cancel(f)


if __name__ == '__main__':
    guesser = Guesser()
