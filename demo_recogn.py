#!/bin/env python
# -*- coding: utf-8 -*- 

import sys, os, commands

if len(sys.argv) < 2: 
    sys.stderr.write('error: input audio-file?\n')
    sys.exit(1)

from aip import AipSpeech
import tmp_keys as my

client = AipSpeech(my.id, my.key, my.secret)

target = sys.argv[1]

# read file
def get_file_content(filePath):
    try:
        with open(filePath, 'rb') as fp:
            return fp.read()
    except FileNotFoundError:
        sys.stderr.write('file not found.')
    except PermissionError:
        sys.stderr.write('not permitted.')

# record
commands.getstatusoutput('arecord -D "plughw:1,0" -r 16000 -d 5 {}'.format(target))

# invoke api
res = client.asr(get_file_content(target), 'wav', 16000, {
    'dev_pid': '1536',
})

print res

