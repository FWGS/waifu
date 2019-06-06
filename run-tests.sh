#!/bin/bash

die()
{
	exit 1
}

# build waf
./build-waf.sh

# install conan
python -m pip install pip --upgrade --user
pip install conan --user

# run tests
python waf-$1 configure build msdev clean || die

# reconfigure needs a special case
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --test-option || die
python waf-$1 -t tests/reconfigure -o build-reconfigure configure --reconfigure || die
