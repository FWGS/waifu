# encoding: utf-8
# enforce_pic.py -- enforcing PIC if requested
# Copyright (C) 2021 a1batross
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from waflib.Configure import conf

@conf
def check_pic(conf, enable):
	if enable:
		# Every static library must have fPIC
		if '-fPIC' in conf.env.CFLAGS_cshlib:
			conf.env.append_unique('CFLAGS_cstlib', '-fPIC')
			conf.env.append_unique('CXXFLAGS_cxxstlib', '-fPIC')
	else:
		vars = ['CFLAGS_cstlib',
			'CFLAGS_cshlib',
			'CXXFLAGS_cxxshlib',
			'CXXFLAGS_cxxstlib',
			'CFLAGS_MACBUNDLE',
			'CXXFLAGS_MACBUNDLE',]

		for i in vars:
			if '-fPIC' in conf.env[i]:
				conf.env[i].remove('-fPIC')
			conf.env.append_unique(i, '-fno-PIC')
