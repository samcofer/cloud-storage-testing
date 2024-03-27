#!/bin/bash
set -x

TEST_DIRECTORIES=${*: 1:$#}

for DIRECTORY in $TEST_DIRECTORIES
do

# Test application locks

touch /${DIRECTORY}/testfile
/opt/cloud-storage-testing/bin/locktester /${DIRECTORY}/testfile &
spawned_pid=$!
sleep 5
timeout 10s /opt/cloud-storage-testing/bin/locktester /${DIRECTORY}/testfile | tee -a /opt/results/app-testing/${DIRECTORY}-lock-testing
sleep 5
kill -9 $spawned_pid

# Test extended ACLs

if setfacl -m u:testuser:x /${DIRECTORY}/testfile; then
  echo "Extended ACLs are supported" > /opt/results/app-testing/${DIRECTORY}-extended-acl-support
else
  echo "Extended ACLs are not supported" > /opt/results/app-testing/${DIRECTORY}-extended-acl-support
fi

done