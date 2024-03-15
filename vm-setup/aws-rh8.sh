uname -a
yum update -y
uname -a
cd /opt || exit
git clone https://github.com/aws/efs-utils
cd efs-utils/ || exit
yum install -y make rpm-build wget
make rpm
yum -y install ./build/amazon-efs-utils*rpm
if [[ "$(python3 -V 2>&1)" =~ ^(Python 3.6.*) ]]; then sudo wget https://bootstrap.pypa.io/pip/3.6/get-pip.py -O /tmp/get-pip.py; elif [[ "$(python3 -V 2>&1)" =~ ^(Python 3.5.*) ]]; then sudo wget https://bootstrap.pypa.io/pip/3.5/get-pip.py -O /tmp/get-pip.py; elif [[ "$(python3 -V 2>&1)" =~ ^(Python 3.4.*) ]]; then sudo wget https://bootstrap.pypa.io/pip/3.4/get-pip.py -O /tmp/get-pip.py; else sudo wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py; fi
python3 /tmp/get-pip.py
pip3 install botocore
mkdir /efs-single-zone-run /efs-regional-run /same-az-lustre-run /cross-az-lustre-run
mount -t efs fs-0464a88d835ac9b33 /efs-single-zone-run/
mount -t efs fs-0520054dd6a022e3d /efs-regional-run/
curl https://fsx-lustre-client-repo-public-keys.s3.amazonaws.com/fsx-rpm-public-key.asc -o /tmp/fsx-rpm-public-key.asc
sudo rpm --import /tmp/fsx-rpm-public-key.asc
sudo curl https://fsx-lustre-client-repo.s3.amazonaws.com/el/8/fsx-lustre-client.repo -o /etc/yum.repos.d/aws-fsx.repo
reboot
#Reconnect here to make sure you're on the latest rhel 8 kernel
yum install -y kmod-lustre-client lustre-client
mount -t lustre -o relatime,flock fs-053ad0199cbba13dd.fsx.us-east-2.amazonaws.com@tcp:/4gkrzbev /same-az-lustre-run
df -h
cd /opt || exit
git clone https://github.com/samcofer/cloud-storage-testing
