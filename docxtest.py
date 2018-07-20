# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 17:35:49 2018

@author: Admin
"""

from docx import *

document = opendocx('xxxzzz.docx')
table = document.xpath('/w:document/w:body/w:tbl', namespaces=nsprefixes)[0]

body.append("Inilah saya yang suka makan telor")

output.save('new-file-name.docx')