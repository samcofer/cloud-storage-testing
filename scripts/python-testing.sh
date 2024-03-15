#!/bin/bash

TEST_DIRECTORIES=${*: 2:$#}
PYTHON_VERSION=$1

for DIRECTORY in $TEST_DIRECTORIES
do

mkdir -p /${DIRECTORY}/testuser/
chmod -R 755 /${DIRECTORY}
chown -R testuser:testuser /${DIRECTORY}
rm -rf /${DIRECTORY}/testuser/*

usermod -d /${DIRECTORY}/testuser testuser
su - testuser <<EOF
export PATH=/opt/python/${PYTHON_VERSION}/bin:$PATH
/opt/scripts/pytorch.sh > /opt/results/python-testing/${DIRECTORY}1
rm -rf ~/*
/opt/scripts/pytorch.sh > /opt/results/python-testing/${DIRECTORY}2
rm -rf ~/*
/opt/scripts/pytorch.sh > /opt/results/python-testing/${DIRECTORY}3
rm -rf ~/*
exit
EOF

done
