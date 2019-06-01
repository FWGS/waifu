#! /usr/bin/env python
# encoding: utf-8
# a1batross, mittorn, 2018

from __future__ import print_function

VERSION = '1.0'
APPNAME = 'waifu-tests'
top = '.'

def subdirs():
	return map(lambda x: x.name, SUBDIRS)

def options(opt):
	opt.load('subproject')
	opt.add_subproject('tests')
	pass

def configure(conf):
	conf.add_subproject('tests')
	pass

def build(bld):
	bld.add_subproject('tests')
	pass
