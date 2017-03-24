# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:20:37 2017

@author: RAVI_SHEKHAR_SINGH
Date :- 24/03/2017
File :- auto_putty_login.py
Description :- automate putty login from windows & attach various tmux sessions
Version :- 1.0 - created initial script
           2.0 - removed linux scripts and replaced with alias, reduced code size
Licence :- GPLv3

"""

from pywinauto.application import Application
import time

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
# tmuxscripts is my alias to tmux attach command
putty.TypeKeys ("shayla")
time.sleep (1)
putty.TypeKeys ("{ENTER}")

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("quasar")
time.sleep (1)
putty.TypeKeys ("{ENTER}")

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("injustice")
time.sleep (1)
putty.TypeKeys ("{ENTER}")

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("ciri")
time.sleep (1)
putty.TypeKeys ("{ENTER}")

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("felicity")
time.sleep (1)
putty.TypeKeys ("{ENTER}")

app = Application ().Start (cmd_line=u'putty -load server -ssh arya@10.13.93.32')
putty = app.PuTTY
putty.Wait ('ready')
time.sleep (2)
putty.TypeKeys ("password")
putty.TypeKeys ("{ENTER}")
time.sleep (1)
putty.TypeKeys ("immortals")
time.sleep (1)
putty.TypeKeys ("{ENTER}")