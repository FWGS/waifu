#!/bin/bash

TOOLS="msvs,clang_compilation_database,color_msvc"
PRELUDE=$'\tsys.path.insert(0, \'scripts/waifulib\')'

pushd wafsrc
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE"
mv waf ../
popd

