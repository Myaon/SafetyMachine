# -*- coding: utf-8 -*-
import subprocess

def toText(text):
	subprocess.call(['./jtalk.sh', text])
