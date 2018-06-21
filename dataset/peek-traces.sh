#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cat $DIR/traces/*.traces.gz | gzip -cd | head -n$1
