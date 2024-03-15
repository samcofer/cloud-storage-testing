#!/bin/bash

TEST_DIRECTORIES=${@: 1:$#}

for DIRECTORY in $TEST_DIRECTORIES
do

rm -rf /${DIRECTORY}/testuser/*

usermod -d /${DIRECTORY}/testuser testuser
su - testuser
/opt/scripts/fsbench.sh > /opt/results/r-testing/${DIRECTORY}1
rm -rf ~/*
/opt/scripts/fsbench.sh > /opt/results/r-testing/${DIRECTORY}2
rm -rf ~/*
/opt/scripts/fsbench.sh > /opt/results/r-testing/${DIRECTORY}3
rm -rf ~/*
exit

done