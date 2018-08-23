#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared        as sh
import sharedGUI     as sg
import guesser.logic as lg

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../../resources/locale')


class Guesser:

    def __init__(self):
        self.logic = lg.Guesser()
        self.logic.word = 'he??o'
        print(self.logic.search())


if __name__ == '__main__':
    sg.objs.start()
    guesser = Guesser()
    sg.objs.end()
