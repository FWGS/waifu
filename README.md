# Waifu Build System

[![Build Status](https://api.travis-ci.com/FWGS/waifu.svg?branch=master)](https://travis-ci.com/FWGS/waifu) 

This is a Waf build system with experimental tools developed for FWGS projects.

This repo is focused on developing our own tools, testing them, syncing with upstream and maybe sending back patches to original Waf in future.

## Build

We add some additional tools from original Waf extras and prelude to load waifulib is added.

To build use `build-waf.sh` shell script

## Running tests

```
$ sh run-tests.sh
```

If it succeded, then tests are not failed.

## Using in your project

`build-waf.sh` creates two waf binaries.
1) `waf-ext` as a prebuilt waf binary with stable tools.
2) `waf-noext` as a prebuilt vanilla waf binary, only with waifulib preloader.

They published to [GitHub Releases](https://github.com/FWGS/waifu/releases/) as well.

You may need to create `scripts/waifulib` folder where you will place `waf` binary.
Depending on your needs, copy modules from our `scripts/waifulib` folder to yours.

