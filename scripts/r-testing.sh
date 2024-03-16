#!/bin/bash

set -x


TEST_DIRECTORIES=${*: 1:$#}

# sudoers edit is required for testuser to run sudo make -C tools install
echo "testuser ALL=(ALL) NOPASSWD: /usr/bin/make *" >> /etc/sudoers

for DIRECTORY in $TEST_DIRECTORIES
do

export DIRECTORY=$DIRECTORY
rm -rf /${DIRECTORY}/testuser/
mkdir -p /${DIRECTORY}/testuser/
chmod -R 755 /${DIRECTORY}
chown -R testuser:testuser /${DIRECTORY}


usermod -d /${DIRECTORY}/testuser testuser
su - testuser <<EOF
/opt/scripts/fsbench.sh /opt/results/r-testing/${DIRECTORY} | tee -a /opt/results/r-testing/${DIRECTORY}1
rm -rf ~/*
/opt/scripts/fsbench.sh /opt/results/r-testing/${DIRECTORY} | tee -a /opt/results/r-testing/${DIRECTORY}2
rm -rf ~/*
/opt/scripts/fsbench.sh /opt/results/r-testing/${DIRECTORY} | tee -a /opt/results/r-testing/${DIRECTORY}3
rm -rf ~/*
exit
EOF
done

sudo sed -i '$d' /etc/sudoers