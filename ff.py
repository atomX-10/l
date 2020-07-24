#! /usr/bin/env python
# -*- coding: utf-8 -*-
import webbot
import time
web = webbot.Browser()
web.go_to('https://scratch.mit.edu/projects/')
web.click('Вход')
web.type('', into='username')
web.type('', into='Password')
web.press(web.Key.ENTER)
time.sleep(2)
web.click('Вперёд' , classname = 'stage_green-flag-overlay_gNXnv')
