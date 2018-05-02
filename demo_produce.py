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

res = client.synthesis('我听到了，有什么吩咐呢？', 'zh', 1, {
    'vol': 5, 'per':4
})
if not isinstance(res, dict):
    try:
        with open(target, 'wb') as f:
            f.write(res)
        commands.getstatusoutput('omxplayer {}'.format(target))
    except Exception as e:
        sys.stderr.write('ERR: {}'.format( e.strerror )) 
else:
    print res

