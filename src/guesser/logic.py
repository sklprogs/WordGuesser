#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared as sh

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
        if word:
            if isinstance(word,str):
                self.word = word
                self.word = self.word.lower()
                self.word = self.word.replace('.','?').replace('_','?')
            else:
                sh.log.append ('Guesser.reset'
                              ,_('ERROR')
                              ,_('Wrong input data!')
                              )
        else:
            sh.log.append ('Guesser.reset'
                          ,_('WARNING')
                          ,_('Empty input is not allowed!')
                          )
    
    def search(self):
        if self.Success:
            if self.word:
                timer = sh.Timer(func_title='Guesser.search')
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
                sh.log.append ('Guesser.search'
                              ,_('WARNING')
                              ,_('Empty input is not allowed!')
                              )
        else:
            sh.log.append ('Guesser.search'
                          ,_('WARNING')
                          ,_('Operation has been canceled.')
                          )
    
    def load(self):
        if self.Success:
            if not self.lst:
                timer = sh.Timer(func_title='Guesser.load')
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
            sh.log.append ('Guesser.load'
                          ,_('WARNING')
                          ,_('Operation has been canceled.')
                          )


if __name__ == '__main__':
    sh.objs.mes(Silent=1)
    guesser = Guesser()
