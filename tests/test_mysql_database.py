#!/usr/bin/python

import os, sys

scriptdir	= os.path.dirname(os.path.abspath(__file__)) # clip file name from path
basedir		= os.path.dirname(scriptdir) # tests/..

sys.path.insert(0, basedir)

import logging, os, json

from mysql_versioning import MySQL_database

def test_mysql_database():
    manager		= MySQL_database( user		= "root",
                                          password	= "",
                                          packages	= [ os.path.abspath('./tests/packages/'+pack) for pack in os.listdir('./tests/packages') ] )

    packages		= manager.packages()
    assert len(packages) == 8
    assert packages.keys() == ['0.1', '0.2', '1.0', '1.0.1', '2.0', '2.5', '3.0', '10.0.2']

    packages		= manager.upgrade( '1.5' )
    assert len(packages) == 4
    assert packages.keys() == ['0.1', '0.2', '1.0', '1.0.1']

    packages		= manager.upgrade( '1.0.1' )
    assert len(packages) == 4
    assert packages.keys() == ['0.1', '0.2', '1.0', '1.0.1']

    packages		= manager.downgrade( '1.5' )
    assert len(packages) == 4
    assert packages.keys() == ['10.0.2', '3.0', '2.5', '2.0']

    packages		= manager.downgrade( '2.0' )
    assert len(packages) == 3
    assert packages.keys() == ['10.0.2', '3.0', '2.5']

