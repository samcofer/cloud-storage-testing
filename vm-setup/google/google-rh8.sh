uname -a
yum update -y
uname -a
cd /opt || exit
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y make rpm-build wget nfs-utils ioping python3.11 git nfs4-acl-tools
mkdir /gfs-basic-ssd-run /gfs-ent-ssd-run /gfs-zonal-ssd-run /local-storage-ssd-persistent-disk /gfs-regional-ssd-run /gcp-netapp-premium-run

mount -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,nconnect=2,tcp 10.28.197.130:/gfs_ent_ssd_fs /gfs-ent-ssd-run
mount -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,nconnect=7,tcp 10.234.156.194:/gfs_zonal_ssd_fs /gfs-zonal-ssd-run
mount -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,tcp 10.110.88.66:/gfs_basic_ssd /gfs-basic-ssd-run
mount -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,tcp 10.24.44.2:/sjc_evenup_test_fs /gfs-regional-ssd-run
mount -t nfs -o rw,hard,rsize=65536,wsize=65536,vers=4.1,tcp 172.17.29.4:/gcp-netapp-premium-share /gcp-netapp-premium-run



df -h
cd /opt || exit
git clone https://github.com/samcofer/cloud-storage-testing
cd cloud-storage-testing/scripts/ || exit
./load-test.sh