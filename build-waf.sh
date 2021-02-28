#!/bin/bash

TOOLS="msvs,clang_compilation_database,color_msvc,msvc_pdb,pthread"
PRELUDE=$'\tContext.WAIFUVERSION=\'1.1.0\'\n\tsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \'scripts\', \'waifulib\'))'

# a set of relatively stable tools
# TODO: make it possible to override this list
WAIFU_TOOLS="gitversion,reconfigure,msdev,fwgslib,cxx11,force_32bit,subproject,strip_on_install,sdl2,enforce_pic"

pushd wafsrc
echo "-- Building waf without waifu extensions: $TOOLS"
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE" "--set-name=waifu" --nostrip
mv waf ../waf-noext
popd

get_waifu_tools()
{
	OLD_IFS=$IFS
	IFS=","
	retval=""
	for i in $WAIFU_TOOLS; do
		retval="$retval,$PWD/scripts/waifulib/$i.py"
	done
	IFS=$OLD_IFS
	echo "$retval"
}
TOOLS=$TOOLS$(get_waifu_tools)
echo "-- Building waf with waifu extensions: $TOOLS"
pushd wafsrc
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE" "--set-name=waifu" --nostrip
mv waf ../waf-ext
popd
