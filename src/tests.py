#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import shared             as sh
import sharedGUI          as sg
import guesser.controller as gc

import gettext, gettext_windows
gettext_windows.setup_env()
gettext.install('WordGuesser','../resources/locale')


if __name__ == '__main__':
    sg.objs.start()
    gc.show()
    sg.objs.end()
