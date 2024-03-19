#!/bin/bash
set -x

TEST_DIRECTORIES=${*: 1:$#}

nfsiostat | tee -a /opt/results/io-testing/nfsiostat-${DIRECTORY}

for DIRECTORY in $TEST_DIRECTORIES
do

ioping -c 50 ${DIRECTORY} | tee -a /opt/results/io-testing/ioping-${DIRECTORY}

ioping -c 50 -s 1024k ${DIRECTORY} | tee -a /opt/results/io-testing/ioping-${DIRECTORY}

ioping -RAL -w 30 ${DIRECTORY} | tee -a /opt/results/io-testing/ioping-${DIRECTORY}

ioping -RWAL -w 30 ${DIRECTORY} | tee -a /opt/results/io-testing/ioping-${DIRECTORY}

done