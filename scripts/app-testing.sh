#!/bin/bash
set -x

TEST_DIRECTORIES=${*: 1:$#}

for DIRECTORY in $TEST_DIRECTORIES
do

# Test application locks

touch /${DIRECTORY}/testfile
../bin/locktester /${DIRECTORY}/testfile &
spawned_pid=$!
timeout 10s ../bin/locktester /${DIRECTORY}/testfile | tee -a /opt/results/app-testing/${DIRECTORY}-lock-testing
kill -9 $spawned_pid

# Test extended ACLs

if setfacl -m u:ec2-user:x /${DIRECTORY}/testfile; then
  echo "File locks are supported" > /opt/results/app-testing/${DIRECTORY}-extended-acl-supported
else
  echo "File locks are not supported" > /opt/results/app-testing/${DIRECTORY}-no-extended-acl-support
fi

done