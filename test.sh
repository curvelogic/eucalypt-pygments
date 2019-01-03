#!/bin/bash

testdir=$1

for f in $testdir/*.eu ; do
    pygmentize -l eucalypt.py:EucalyptLexer -x -O full,style=tango -f html $f > $(basename "${f%.eu}.html")
done
