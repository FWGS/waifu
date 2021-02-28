#!/bin/bash

die()
{
	cat $1/config.log
	exit 1
}

# build waf
./build-waf.sh

# disable conan for python < 3.4
if python -c 'import sys; exit(sys.hexversion < 0x03050000)'; then
	# install conan
	pip install pip --upgrade
	pip install conan
fi

# run tests
python waf-$1 configure build msdev clean || die build

# reconfigure needs a special case
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --test-option || die build-reconfigure
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --reconfigure || die build-reconfigure
