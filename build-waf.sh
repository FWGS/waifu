#!/bin/bash

TOOLS="msvc,clang_compilation_database"
PRELUDE=$'\tsys.path.insert(0, \'scripts/waifulib\')'

pushd wafsrc
./waf-light "--tools=$TOOLS" "--prelude=$PRELUDE"
mv waf ../
popd

