uname -a
yum update -y
uname -a
cd /opt || exit
yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install -y make rpm-build wget nfs-utils ioping iscsi-initiator-utils device-mapper-multipath python3.11
mpathconf --enable

vi multipath.conf
systemctl restart multipathd
vi connect.py
chmod 700 connect.py
rpm --import https://packages.microsoft.com/keys/microsoft.asc
dnf install -y https://packages.microsoft.com/config/rhel/8/packages-microsoft-prod.rpm
dnf install azure-cli
az extension add -n elastic-san
az login
python3.11 connect.py --subscription cdc5ba7c-38d0-43f9-9670-7b37680ad295 -g sjc_rgf7fc489b -e sjc-perf-test-san -v sjc-perf-test-san-vg -n sjc-elastic-san-run -s 32
pvcreate /dev/mapper/mpathb
vgcreate azureSANvg /dev/mapper/mpathb
lvcreate -n azureSANvol -L4500G /dev/azureSANvg
mkfs.ext4 /dev/azureSANvg/azureSANvol
mount /dev/azureSANvg/azureSANvol /elastic-san-same-zone-run/
mkdir /netapp-standard-run /netapp-premium-run /netapp-ultra-run /storage-acct-azure-files-run /elastic-san-same-zone-run /local-storage-premium-ssd-lrs-run
mount -t nfs -o rw,hard,rsize=262144,wsize=262144,sec=sys,vers=4.1,tcp 10.11.11.4:/sjc-netapp-standard-vol /netapp-standard-run
mount -t nfs -o rw,hard,rsize=262144,wsize=262144,sec=sys,vers=4.1,tcp 10.11.11.5:/sjc-netapp-premium-vol /netapp-premium-run
mount -t nfs -o rw,hard,rsize=262144,wsize=262144,sec=sys,vers=4.1,tcp 10.11.11.5:/sjc-netapp-ultra-vol /netapp-ultra-run
mount -t nfs sjcperftestaz.file.core.windows.net:/sjcperftestaz/sjc-perf-test-nfs-sa /storage-acct-azure-files-run -o vers=4,minorversion=1,sec=sys,nconnect=4


df -h
cd /opt || exit
git clone https://github.com/samcofer/cloud-storage-testing
cd cloud-storage-testing/scripts/
./load-test.sh
