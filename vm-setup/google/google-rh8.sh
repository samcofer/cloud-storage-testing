uname -a
yum update -y
uname -a
cd /opt || exit
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y make rpm-build wget nfs-utils ioping python3.11 git
mkdir /gfs-basic-ssd-run /gfs-ent-ssd-run /gfs-zonal-ssd-run /local-storage-ssd-persistent-disk

mount -t nfs -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,nconnect=2,vers=4.1,tcp 10.28.197.130:/gfs_ent_ssd_fs /gfs-ent-ssd-run
mount -t nfs -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,nconnect=7,vers=4.1,tcp 10.234.156.194:/gfs_zonal_ssd_fs /gfs-zonal-ssd-run
mount -t nfs -o rw,hard,timeo=600,rsize=262144,wsize=1048576,resvport,async,sec=sys,vers=4.1,tcp 10.104.66.154:/gfs_basic_ssd_fs /gfs-basic-ssd-run
