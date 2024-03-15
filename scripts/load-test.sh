#!/bin/bash

AZURE_DIRECTORIES="netapp-standard-run netapp-premium-run netapp-ultra-run storage-acct-run"
AWS_DIRECTORIES="efs-single-zone-run efs-regional-run same-az-lustre-run cross-az-lustre-run"
GCP_DIRECTORIES="gfs-run"

PYTHON_VERSION=3.11.8
R_VERSION=4.3.2

useradd testuser

mkdir -p /opt/results/r-testing/
mkdir -p /opt/results/python-testing/
mkdir -p /opt/results/io-testing/
mdkir -p /opt/scripts/
cp ./* /opt/scripts/
chmod -R 755 /opt/scripts/
chown -R testuser:testuser /opt/results
chmod -R 755 /opt/results/

#Environment preparation

# Python Installation
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf install dnf-plugins-core
dnf config-manager --set-enabled "codeready-builder-for-rhel-8-*-rpms"
curl -O https://cdn.rstudio.com/python/centos-8/pkgs/python-${PYTHON_VERSION}-1-1.x86_64.rpm
sudo yum install python-${PYTHON_VERSION}-1-1.x86_64.rpm
/opt/python/"${PYTHON_VERSION}"/bin/pip install --upgrade pip setuptools wheel
export PATH=/opt/python/"${PYTHON_VERSION}"/bin:$PATH

# R Installation

curl -O https://cdn.rstudio.com/r/centos-8/pkgs/R-${R_VERSION}-1-1.x86_64.rpm
yum install R-${R_VERSION}-1-1.x86_64.rpm
ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R
ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript

./python-testing.sh $PYTHON_VERSION "$DIRECTORIES"

./r-testing.sh "$DIRECTORIES"

./io-testing.sh "$DIRECTORIES"
