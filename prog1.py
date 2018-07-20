# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 17:14:08 2018

@author: Admin
"""
import pythoncom, pyHook
import ctypes
import re
import datetime

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import signal


chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--test-type")

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://translate.google.com/?#id/en/apa%20kabar')
assert "Google Translate" in browser.title