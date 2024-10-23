# encoding: utf-8
# cxx11.py -- check if compiler can compile C++11 code with lambdas
# Copyright (C) 2018 a1batross
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

try: from fwgslib import get_flags_by_compiler
except: from waflib.extras.fwgslib import get_flags_by_compiler
from waflib import Configure

cxx_flags = {
	'cxx11': {
		'msvc'   : [],
		'default': ['-std=c++11'],
	},
	'cxx14': {
		'msvc'   : ['/std:c++14'],
		'default': ['-std=c++14'],
	},
	'cxx17': {
		'msvc'   : ['/std:c++17'],
		'default': ['-std=c++17'],
	},
	'cxx20': {
		'msvc'   : ['/std:c++20'],
		'default': ['-std=c++20'],
	},
	'cxx23': {
		'msvc'   : ['/std:c++latest'], # not supported in MSVC as of 2024
		'default': ['-std=c++23'],
	},
}

cxx_macros = {
	'cxx11': '201103L',
	'cxx14': '201402L',
	'cxx17': '201703L',
	'cxx20': '202002L',
	'cxx23': '202302L',
}

CPLUSPLUS_FRAGMENT='''
#if __cplusplus < %s
#error "not supported"
#endif

int main(int argc, char **argv)
{
	(void)argc;
	(void)argv;
	return 0;
}
'''

c_flags = {
	'c11': {
		'msvc'   : ['/std:c11'],
		'default': ['-std=c11'],
	},
	'c17': {
		'msvc'   : ['/std:c17'],
		'default': ['-std=c11'],
	},
	'c23': {
		'msvc'   : ['/std:clatest'], # not supported in MSVC as of 2024?
		'default': ['-std=c11'],
	},
}

c_macros = {
	'c11': '201112L',
	'c17': '201710L',
	'c23': '202311L',
}

STDC_FRAGMENT='''
#if __STDC_VERSION__ < %s
#error "not supported"
#endif

int main(int argc, char **argv)
{
	(void)argc;
	(void)argv;
	return 0;
}
'''

@Configure.conf
def check_cxx11(ctx, msg, fragment, is_cxx, flags = None, *k, **kw):
	kw['mandatory'] = False
	kw['msg'] = msg
	kw['fragment'] = fragment

	if flags:
		kw['cxxflags' if is_cxx else 'cflags'] = flags

	if is_cxx:
		return ctx.check_cxx(*k, **kw)

	return ctx.check_cc(*k, **kw)

@Configure.conf
def check_std(conf, version, mandatory = False):
	if version.startswith('c++'):
		version.replace('c++', 'cxx')

	textversion = version.replace('cxx', 'c++').upper()

	if version not in cxx_flags and version not in c_flags:
		if mandatory:
			conf.fatal('%s support not available' % textversion)
		return False

	is_cxx = version.startswith('cxx')

	if is_cxx:
		msg = 'Checking if \'%s\' supports %s' % (conf.env.COMPILER_CXX, textversion)
		flags = get_flags_by_compiler(cxx_flags[version], conf.env.COMPILER_CXX)
		frag = CPLUSPLUS_FRAGMENT % cxx_macros[version]
	else:
		msg = 'Checking if \'%s\' supports %s' % (conf.env.COMPILER_C, textversion)
		flags = get_flags_by_compiler(c_flags[version], conf.env.COMPILER_C)
		frag = STDC_FRAGMENT % c_macros[version]

	if conf.check_cxx11(msg, frag, is_cxx):
		return True

	if len(flags) != 0 and conf.check_cxx11('...trying with additional flags', frag, is_cxx, flags):
		conf.env['CXXFLAGS' if is_cxx else 'CFLAGS'] += flags
		return True

	if mandatory:
		conf.fatal('%s support not available!', textversion)

	return False
