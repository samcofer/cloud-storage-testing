#!/bin/bash

set -x

TEST_DIRECTORIES=${*: 2:$#}
PYTHON_VERSION=$1

for DIRECTORY in $TEST_DIRECTORIES
do
export DIRECTORY=$DIRECTORY
mkdir -p /${DIRECTORY}/testuser/
chmod -R 755 /${DIRECTORY}
chown -R testuser:testuser /${DIRECTORY}
rm -rf /${DIRECTORY}/testuser/*

usermod -d /${DIRECTORY}/testuser testuser
su - testuser <<EOF
export PATH=/opt/python/${PYTHON_VERSION}/bin:$PATH
/opt/scripts/pytorch.sh | tee -a /opt/results/python-testing/${DIRECTORY}1-pytorch-install
rm -rf ~/*
/opt/scripts/pytorch.sh | tee -a  /opt/results/python-testing/${DIRECTORY}2-pytorch-install
rm -rf ~/*
/opt/scripts/pytorch.sh | tee -a  /opt/results/python-testing/${DIRECTORY}3-pytorch-install
rm -rf ~/*
exit
EOF

done
