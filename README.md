# Waifu Build System

This is a fork of Waf build system. It's not a complete build system, though.

This repo is focused on developing our own modules, testing them, syncing with upstream and maybe sending back patches to original Waf in future.

## Build

We add some additional tools from original Waf extras and prelude to load waifulib is added.

You can use `build-waf.sh` shell script(TODO: move to wscript) either prebuilt `waf` from this root repo

## Running tests

They are enabled by default. Just run:
```
$ waf configure build
```

If it succeded, then tests are not failed.

## Using in your project

Copy `scripts` and generated/prebuilt `waf` file to your project
