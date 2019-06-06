# Waifu Build System

This is a Waf build system with some experimental modules developed for FWGS projects.

This repo is focused on developing our own modules, testing them, syncing with upstream and maybe sending back patches to original Waf in future.

## Build

We add some additional tools from original Waf extras and prelude to load waifulib is added.

To build use `build-waf.sh` shell script

## Running tests

```
$ sh run-tests.sh
```

If it succeded, then tests are not failed.

## Using in your project

There is two prebuilt waf binaries, to those who don't want build by themselves.
1) `waf-ext` as a prebuilt waf binary with some of our modules
2) `waf-noext` as a prebuilt vanilla waf binary, only with line of code, to preload waifulib

Then you need to create `scripts/waifulib` folder where you will place `waf` binary.
Depending on your needs, copy modules from our `scripts/waifulib` folder to yours.
