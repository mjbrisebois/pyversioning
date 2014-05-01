#!/usr/bin/python

import os, sys, json

scriptdir	= os.path.dirname(os.path.abspath(__file__)) # clip file name from path
basedir		= os.path.dirname(scriptdir) # tests/..

sys.path.insert(0, basedir)

import logging
from version import Version_dict


def test_version_sort():
    versions		= Version_dict()

    versions['0.1']	= 'create-databases'
    versions['0.2']	= 'create-tables'
    versions['1.0']	= 'feature-cool'
    versions['1.0.1']	= 'hotfix-your-mom'
    versions['2.0']	= 'release-beta'
    versions['2.5']	= 'halfway-super-pack'
    versions['3.0']	= 'upgraded-armory'
    versions['10.0.2']	= 'coolio-bigalo'
    
    start		= versions.slice( start='2.0' )

    assert len(start) == 4
    assert start.keys() == ['2.0', '2.5', '3.0', '10.0.2']

    stop		= versions.slice( stop='2.0' )

    assert len(stop) == 5
    assert stop.keys() == ['0.1', '0.2', '1.0', '1.0.1', '2.0']
    

    startstop		= versions.slice( '1.0', '2.0' )

    assert len(startstop) == 3
    assert startstop.keys() == ['1.0', '1.0.1', '2.0']
