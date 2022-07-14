#!/usr/bin/env bash

bin/ginit
bin/gbuild db triple.txt
rm /usr/src/gstore/triple.txt
