#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mistune

from aam.reader.markdown import MyRenderer

def to_unicode(value):
    if isinstance(value, str):
        return value
    if isinstance(value, basestring):
        return value.decode('utf-8')
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def md_to_html(text):
    text = to_unicode(text)
    renderer = MyRenderer()
    #renderer = mistune.Renderer(escape=True, hard_wrap=True)
    md = mistune.Markdown(renderer=renderer)
    return md.render(text)

