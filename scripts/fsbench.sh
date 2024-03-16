#!/bin/bash

git clone https://github.com/samcofer/fsbench
cd fsbench/ || exit
export OUTPUT_FILE=$1
make setup
make