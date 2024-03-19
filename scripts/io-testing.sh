#!/bin/bash
set -x

TEST_DIRECTORIES=${*: 1:$#}

nfsiostat | tee -a /opt/results/io-testing/nfsiostat-output

for DIRECTORY in $TEST_DIRECTORIES
do

ioping -c 50 /${DIRECTORY} | tee -a /opt/results/io-testing/${DIRECTORY}-ioping-ping

ioping -c 50 -s 1024k /${DIRECTORY} | tee -a /opt/results/io-testing/${DIRECTORY}-ioping-large-ping

ioping -RAL -w 30 /${DIRECTORY} | tee -a /opt/results/io-testing/${DIRECTORY}-ioping-linear-async-read

ioping -RWAL -w 30 /${DIRECTORY} | tee -a /opt/results/io-testing/${DIRECTORY}-ioping-linear-async-write

done