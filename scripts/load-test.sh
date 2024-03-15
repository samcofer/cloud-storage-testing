#!/bin/bash

set -x

AZURE_DIRECTORIES="netapp-standard-run netapp-premium-run netapp-ultra-run storage-acct-run"
#AWS_DIRECTORIES="efs-single-zone-run efs-regional-run same-az-lustre-run cross-az-lustre-run"
AWS_DIRECTORIES="efs-single-zone-run efs-regional-run same-az-lustre-run"
GCP_DIRECTORIES="gfs-run"

PYTHON_VERSION=3.11.8
R_VERSION=4.3.2

yum update -y -q

useradd testuser

mkdir -p /opt/results/r-testing/ /opt/results/python-testing/ /opt/results/io-testing/ /opt/scripts/ /opt/work/
cp ./*.sh /opt/scripts/
chmod -R 755 /opt/scripts/ /opt/results/
chown -R testuser:testuser /opt/results /opt/scripts

#Environment preparation


# Python Installation
if ! rpm -q "epel-release-*" &> /dev/null; then
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf install -y dnf-plugins-core
fi
dnf config-manager --set-enabled "codeready-builder-for-rhel-8-*-rpms"

if [ ! -f "/opt/work/python-${PYTHON_VERSION}-1-1.x86_64.rpm" ]; then
curl -o /opt/work/python-${PYTHON_VERSION}-1-1.x86_64.rpm https://cdn.rstudio.com/python/centos-8/pkgs/python-${PYTHON_VERSION}-1-1.x86_64.rpm
fi

if ! rpm -q "python-${PYTHON_VERSION}-1-1.x86_64" &> /dev/null; then
sudo yum install -y python-${PYTHON_VERSION}-1-1.x86_64.rpm
fi

/opt/python/"${PYTHON_VERSION}"/bin/pip install --upgrade pip setuptools wheel

export PATH=/opt/python/"${PYTHON_VERSION}"/bin:$PATH
ln -sf /opt/python/"${PYTHON_VERSION}"/bin/pip /usr/local/bin/pip
ln -sf /opt/python/"${PYTHON_VERSION}"/bin/python /usr/local/bin/python

## R Installation

if [ ! -f "/opt/work/R-${R_VERSION}-1-1.x86_64.rpm" ]; then
curl -o /opt/work/R-${R_VERSION}-1-1.x86_64.rpm https://cdn.rstudio.com/r/centos-8/pkgs/R-${R_VERSION}-1-1.x86_64.rpm
fi

if ! rpm -q "R-${R_VERSION}-1-1.x86_64" &> /dev/null; then
yum install -y R-${R_VERSION}-1-1.x86_64.rpm
fi

ln -sf /opt/R/${R_VERSION}/bin/R /usr/local/bin/R
ln -sf /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript

# Check if the instance metadata service is reachable
if curl -s --connect-timeout 2 http://169.254.169.254/latest/meta-data/ &> /dev/null; then
    # Instance metadata service is reachable, assume running in AWS
    echo "Running in AWS environment."
    DIRECTORIES=$AWS_DIRECTORIES
elif curl -s --connect-timeout 2 -H Metadata:true "http://169.254.169.254/metadata/instance?api-version=2021-02-01" &> /dev/null; then
    # Azure Metadata Service is reachable, assume running in Azure
    echo "Running in Azure environment."
    DIRECTORIES=$AZURE_DIRECTORIES

elif curl -s --connect-timeout 2 "http://metadata.google.internal/computeMetadata/v1/instance/" -H "Metadata-Flavor: Google" &> /dev/null; then
    # GCP metadata service is reachable, assume running in GCP
    echo "Running in GCP environment."
    DIRECTORIES=$GCP_DIRECTORIES
else
    # No metadata service reachable, assume not running in any known cloud environment
    echo "Not running in AWS, Azure, or GCP environment."
    return
fi

#./python-testing.sh $PYTHON_VERSION "$DIRECTORIES"
#
./r-testing.sh "$DIRECTORIES"
#
#./io-testing.sh "$DIRECTORIES"
