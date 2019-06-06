#!/bin/bash

TOOLS="msvs,clang_compilation_database,color_msvc"
PRELUDE=$'\tsys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), \'scripts\', \'waifulib\'))'

# a set of relatively stable tools
# TODO: make it possible to override this list
WAIFU_TOOLS="gitversion,reconfigure,msdev,fwgslib,cxx11,force_32bit,subproject"

pushd wafsrc
echo "-- Building waf without waifu extensions: $TOOLS"
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE"
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
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE"
mv waf ../waf-ext
popd
