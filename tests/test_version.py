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
    
    start		= list(versions.slice( start='2.0' ))
    
    # ('2.0', 'release-beta')
    # ('2.5', 'halfway-super-pack')
    # ('3.0', 'upgraded-armory')
    # ('10.0.2', 'coolio-bigalo')

    assert len(start) == 4
    assert start[0][0] == '2.0'
    assert start[0][1] == 'release-beta'
    assert start[3][0] == '10.0.2'
    assert start[3][1] == 'coolio-bigalo'

    stop		= list(versions.slice( stop='2.0' ))
    
    # ('0.1', 'create-databases')
    # ('0.2', 'create-tables')
    # ('1.0', 'feature-cool')
    # ('1.0.1', 'hotfix-your-mom')
    # ('2.0', 'release-beta')

    assert len(stop) == 5
    assert stop[0][0] == '0.1'
    assert stop[0][1] == 'create-databases'
    assert stop[4][0] == '2.0'
    assert stop[4][1] == 'release-beta'

    startstop		= list(versions.slice( '1.0', '2.0' ))

    # ('1.0', 'feature-cool')
    # ('1.0.1', 'hotfix-your-mom')
    # ('2.0', 'release-beta')

    assert len(startstop) == 3
    assert startstop[0][0] == '1.0'
    assert startstop[0][1] == 'feature-cool'
    assert startstop[2][0] == '2.0'
    assert startstop[2][1] == 'release-beta'
