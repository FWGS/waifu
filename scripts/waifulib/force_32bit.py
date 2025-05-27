# encoding: utf-8
# force_32bit.py -- force compiler to create 32-bit code
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

# Output:
#   DEST_SIZEOF_VOID_P -- an integer, equals sizeof(void*) on target

DEST_CPU_64_TO_32 = {
'x86_64'  : 'x86',
'amd64'   : 'x86',
'aarch64' : 'thumb',
}

@Configure.conf
def check_32bit(ctx, *k, **kw):
	if not 'msg' in kw:
		kw['msg'] = 'Checking if \'%s\' generates 32-bit code' % ctx.env.COMPILER_CC

	if not 'mandatory' in kw:
		kw['mandatory'] = False

	return ctx.check_cc(fragment='int main(void){int check[sizeof(void*)==4?1:-1];return 0;}', *k, **kw)

@Configure.conf
def force_32bit(ctx, set_dest_cpu = True):
	# no work to do
	if ctx.env.DEST_SIZEOF_VOID_P == 4:
		return

	msg = 'Configuring \'%s\' to generate 32-bit code' % ctx.env.COMPILER_CC
	flags = ['-m32'] if not ctx.env.DEST_OS == 'darwin' else ['-arch', 'i386']

	if ctx.check_32bit(msg=msg, cflags=flags, linkflags=flags):
		ctx.env.LINKFLAGS += flags
		ctx.env.CXXFLAGS += flags
		ctx.env.CFLAGS += flags
		ctx.env.DEST_SIZEOF_VOID_P = 4

		if set_dest_cpu and ctx.env.DEST_CPU in DEST_CPU_64_TO_32:
			ctx.env.DEST_CPU = DEST_CPU_64_TO_32[ctx.env.DEST_CPU]
			ctx.msg('New target CPU', ctx.env.DEST_CPU)
	else:
		ctx.fatal('Compiler can\'t create 32-bit code!')

def configure(ctx):
	ctx.env.DEST_SIZEOF_VOID_P = 4 if ctx.check_32bit() else 8
