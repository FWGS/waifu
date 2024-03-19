#!/bin/bash

if [ -z $1 ]; then
	echo "$0: <ext|noext>"
	exit 1
fi

die()
{
#	cat $1/config.log
	exit 1
}

# build waf
./build-waf.sh

# run tests
python waf-$1 configure build msdev clean || die build

# reconfigure needs a special case
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --test-option || die build-reconfigure
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --reconfigure || die build-reconfigure
