VM Details:
```
Linux RHEL8-0-hostname 4.18.0-477.10.1.el8_8.x86_64 #1 SMP Wed Apr 5 13:35:01 EDT 2023 x86_64 x86_64 x86_64 GNU/Linux
Architecture:        x86_64
Virtualization type: full
              total        used        free      shared  buff/cache   available
Mem:           15Gi       626Mi        14Gi        24Mi       390Mi        14Gi
Swap:            0B          0B          0B
Filesystem                                              Size  Used Avail Use% Mounted on
devtmpfs                                                7.7G     0  7.7G   0% /dev
tmpfs                                                   7.7G     0  7.7G   0% /dev/shm
tmpfs                                                   7.7G   25M  7.7G   1% /run
tmpfs                                                   7.7G     0  7.7G   0% /sys/fs/cgroup
/dev/mapper/rootvg-rootlv                               102G  3.1G   99G   4% /
/dev/mapper/rootvg-usrlv                                 10G  2.3G  7.8G  23% /usr
/dev/mapper/rootvg-tmplv                                102G  1.1G  101G   2% /tmp
/dev/mapper/rootvg-varlv                                8.0G  911M  7.2G  12% /var
tmpfs                                                   1.6G     0  1.6G   0% /run/user/1000

```

![](Pasted%20image%2020230818065559.png)

```
{
  "additionalCapabilities": null,
  "applicationProfile": null,
  "availabilitySet": null,
  "billingProfile": null,
  "capacityReservation": null,
  "diagnosticsProfile": null,
  "evictionPolicy": null,
  "extendedLocation": null,
  "extensionsTimeBudget": null,
  "fqdns": "",
  "hardwareProfile": {
    "vmSize": "Standard_D4s_v5",
    "vmSizeProperties": null
  },
  "host": null,
  "hostGroup": null,
  "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Compute/virtualMachines/RHEL8-0-server-vm2f901d60",
  "identity": null,
  "licenseType": null,
  "location": "eastus2",
  "macAddresses": "60-45-BD-BF-22-97",
  "name": "RHEL8-0-server-vm2f901d60",
  "networkProfile": {
    "networkApiVersion": null,
    "networkInterfaceConfigurations": null,
    "networkInterfaces": [
      {
        "deleteOption": null,
        "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Network/networkInterfaces/RHEL8-0-server-nic95a10122",
        "primary": null,
        "resourceGroup": "sjc_rg369b61f1"
      }
    ]
  },
  "osProfile": {
    "adminPassword": null,
    "adminUsername": "azure-user",
    "allowExtensionOperations": true,
    "computerName": "RHEL8-0-hostname",
    "customData": null,
    "linuxConfiguration": {
      "disablePasswordAuthentication": true,
      "enableVmAgentPlatformUpdates": false,
      "patchSettings": {
        "assessmentMode": "ImageDefault",
        "automaticByPlatformSettings": null,
        "patchMode": "ImageDefault"
      },
      "provisionVmAgent": true,
      "ssh": {
        "publicKeys": [
          {
            "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0VGzZJZvjXQu1WfFJ9bW3UuIrgmXq+VEtKBnSuEc//96jARMYGGCiPvyzLgERHmSWVsyboDVJc426GiTB42mTQl5RtclWpfcfZa0AllpR9AwOQx1DYToo+hhFWsUCPBsgEG9SyVmwUxAA8AAeTM2Rgr12ERgAAPrXTE2vRDUlPZiCYOI9mgpb34El36Hn6BqGFN/Xt8/zaYxCo7xCI+oYmYJ0pfyvuCiOWVGCwhy1HmRGC7wHPMtl+ix2V+b3uQY2xjyY7MRkpV0wOe/+UViXar4xqUIKh1BoHYzTm12kZYYT1X7RWphN7P1G0npv8nLDKvp5Eld+is+JM73tMgHHr1xniyWoyc97KaCW5FO3cfUnGvHnRI3EqO1X0GcXXQ1D09pNFPjGlBINqc+0qNzF7ayiGpo7SPoxFdZTLQ0C6BzWPxIQG7xxy0lXK0gbBCY6Lv2kcpoCadDbXLhY+ZgBISyvCN/OaGnPi/YUJFZDtT71clVYhnW74ojv3m0GTYM= samcofer@DESKTOP-MTUNQ2J",
            "path": "/home/azure-user/.ssh/authorized_keys"
          }
        ]
      }
    },
    "requireGuestProvisionSignal": true,
    "secrets": [],
    "windowsConfiguration": null
  },
  "plan": null,
  "platformFaultDomain": null,
  "powerState": "VM running",
  "priority": null,
  "privateIps": "10.11.10.4",
  "provisioningState": "Succeeded",
  "proximityPlacementGroup": null,
  "publicIps": "20.242.12.33",
  "resourceGroup": "sjc_rg369b61f1",
  "resources": null,
  "scheduledEventsProfile": null,
  "securityProfile": null,
  "storageProfile": {
    "dataDisks": [],
    "diskControllerType": "SCSI",
    "imageReference": {
      "communityGalleryImageId": null,
      "exactVersion": "8.8.2023060919",
      "id": null,
      "offer": "RHEL",
      "publisher": "RedHat",
      "sharedGalleryImageId": null,
      "sku": "8-lvm-gen2",
      "version": "latest"
    },
    "osDisk": {
      "caching": "ReadWrite",
      "createOption": "FromImage",
      "deleteOption": "Detach",
      "diffDiskSettings": null,
      "diskSizeGb": 500,
      "encryptionSettings": null,
      "image": null,
      "managedDisk": {
        "diskEncryptionSet": null,
        "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Compute/disks/RHEL8-0-OSDisk",
        "resourceGroup": "sjc_rg369b61f1",
        "securityProfile": null,
        "storageAccountType": "Premium_LRS"
      },
      "name": "RHEL8-0-OSDisk",
      "osType": "Linux",
      "vhd": null,
      "writeAcceleratorEnabled": null
    }
  },
  "tags": {
    "rs:environment": "infrastructure",
    "rs:owner": "sam.cofer@posit.co",
    "rs:project": "internal"
  },
  "timeCreated": "2023-08-07T22:02:22.977298+00:00",
  "type": "Microsoft.Compute/virtualMachines",
  "userData": null,
  "virtualMachineScaleSet": null,
  "vmId": "f634a53d-4b1a-4fe0-8a04-e102f259211b",
  "zones": null
}
```
Mount Details:
```
10.11.11.4:/sjc-test-ultra-vol on /sjc-test-ultra-vol type nfs4 (rw,relatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.11.10.4,local_lock=none,addr=10.11.11.4)

10.11.11.4:/sjc-test-prem-vol on /sjc-test-prem-vol type nfs4 (rw,relatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.11.10.4,local_lock=none,addr=10.11.11.4)

10.11.11.4:/sjc-test-standard-export on /sjc-test-standard-vol type nfs4 (rw,relatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.11.10.4,local_lock=none,addr=10.11.11.4)   

sjcsatest.file.core.windows.net:/sjcsatest/sjc-test-sa on /sjc-test-sa type nfs4 (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.11.10.4,local_lock=none,addr=10.11.10.6)



```


PyTorch Script
Python Version: 3.11.4
```
rm -rf /sjc-test-standard-vol/testuser/.cache
rm -rf /sjc-test-prem-vol/testuser/.cache
rm -rf /sjc-test-ultra-vol/testuser/.cache
rm -rf /sjc-test-sa/testuser/.cache


usermod -d /sjc-test-standard-vol/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/standard-run1
rm -rf ~/.cache
./pytorch.sh > ~/standard-run2
rm -rf ~/.cache
./pytorch.sh > ~/standard-run3
rm -rf ~/.cache
exit
usermod -d /sjc-test-prem-vol/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/prem-run1
rm -rf ~/.cache
./pytorch.sh > ~/prem-run2
rm -rf ~/.cache
./pytorch.sh > ~/prem-run3
rm -rf ~/.cache
exit
usermod -d /sjc-test-ultra-vol/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/ultra-run1
rm -rf ~/.cache
./pytorch.sh > ~/ultra-run2
rm -rf ~/.cache
./pytorch.sh > ~/ultra-run3
rm -rf ~/.cache
exit
usermod -d /sjc-test-sa/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/sa-run1
rm -rf ~/.cache
./pytorch.sh > ~/sa-run2
rm -rf ~/.cache
./pytorch.sh > ~/sa-run3
rm -rf ~/.cache
exit

usermod -d /sjc-test-nfs-vol/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/nfs-run1
rm -rf ~/.cache
./pytorch.sh > ~/nfs-run2
rm -rf ~/.cache
./pytorch.sh > ~/nfs-run3
rm -rf ~/.cache
exit

usermod -d /sjc-test-local-vol/testuser testuser
su - testuser
export PATH=/opt/python/3.11.4/bin:$PATH
./pytorch.sh > ~/local-run1
rm -rf ~/.cache
./pytorch.sh > ~/local-run2
rm -rf ~/.cache
./pytorch.sh > ~/local-run3
rm -rf ~/.cache
exit
```

Ultra Results:
```
BEGIN - Running in /sjc-test-ultra-vol/testuser
VENV REMOVE: Run duration = 00:00:13
VENV CREATE: Run duration = 00:00:09
PIP UPDATE: Run duration = 00:00:11
PYTORCH INSTALL: Run duration = 00:02:03
CLEANUP: Run duration = 00:00:15
END
BEGIN - Running in /sjc-test-ultra-vol/testuser
VENV CREATE: Run duration = 00:00:08
PIP UPDATE: Run duration = 00:00:12
PYTORCH INSTALL: Run duration = 00:02:14
CLEANUP: Run duration = 00:00:15
END
BEGIN - Running in /sjc-test-ultra-vol/testuser
VENV CREATE: Run duration = 00:00:09
PIP UPDATE: Run duration = 00:00:11
PYTORCH INSTALL: Run duration = 00:02:16
CLEANUP: Run duration = 00:00:15
END

```

Premium Results:

```
BEGIN - Running in /sjc-test-prem-vol/testuser
VENV CREATE: Run duration = 00:00:07
PIP UPDATE: Run duration = 00:00:09
PYTORCH INSTALL: Run duration = 00:02:17
CLEANUP: Run duration = 00:00:10
END
BEGIN - Running in /sjc-test-prem-vol/testuser
VENV CREATE: Run duration = 00:00:07
PIP UPDATE: Run duration = 00:00:09
PYTORCH INSTALL: Run duration = 00:02:18
CLEANUP: Run duration = 00:00:11
END
BEGIN - Running in /sjc-test-prem-vol/testuser
VENV CREATE: Run duration = 00:00:08
PIP UPDATE: Run duration = 00:00:09
PYTORCH INSTALL: Run duration = 00:02:19
CLEANUP: Run duration = 00:00:10
END
```

Standard Results:

```
BEGIN - Running in /sjc-test-standard-vol/testuser
VENV CREATE: Run duration = 00:00:09
PIP UPDATE: Run duration = 00:00:12
PYTORCH INSTALL: Run duration = 00:05:02
CLEANUP: Run duration = 00:00:15
END
BEGIN - Running in /sjc-test-standard-vol/testuser
VENV CREATE: Run duration = 00:00:08
PIP UPDATE: Run duration = 00:00:12
PYTORCH INSTALL: Run duration = 00:04:58
CLEANUP: Run duration = 00:00:15
END
BEGIN - Running in /sjc-test-standard-vol/testuser
VENV CREATE: Run duration = 00:00:09
PIP UPDATE: Run duration = 00:00:11
PYTORCH INSTALL: Run duration = 00:05:39
CLEANUP: Run duration = 00:00:16
END
```

premium storage account

```

[root@RHEL8-0-hostname testuser]# cat *run*
BEGIN - Running in /sjc-test-sa/testuser
VENV CREATE: Run duration = 00:00:45
PIP UPDATE: Run duration = 00:01:07
PYTORCH INSTALL: Run duration = 00:09:22
CLEANUP: Run duration = 00:01:44
END
BEGIN - Running in /sjc-test-sa/testuser
VENV CREATE: Run duration = 00:00:53
PIP UPDATE: Run duration = 00:01:09
PYTORCH INSTALL: Run duration = 00:09:26
CLEANUP: Run duration = 00:01:36
END
BEGIN - Running in /sjc-test-sa/testuser
VENV CREATE: Run duration = 00:00:48
PIP UPDATE: Run duration = 00:01:06
PYTORCH INSTALL: Run duration = 00:09:57
CLEANUP: Run duration = 00:02:00
END

```

fsbench Results: Checked into github.com/samcofer/pulumi_pieces_azure
R: 4.0.2
```
git clone https://github.com/rstudio/fsbench
#Updated renv.lock to use binaries
vi ./fsbench/renv.lock
export TARGET_DIR=/pathtotargetdir/
make setup

make
```

Azure Netapp Details:

```
PS C:\Users\samco> az netappfiles account show --account-name sjc-test --resource-group sjc_rg369b61f1
{
  "activeDirectories": null,
  "disableShowmount": null,
  "encryption": {
    "identity": null,
    "keySource": "Microsoft.NetApp",
    "keyVaultProperties": null
  },
  "etag": "W/\"datetime'2023-08-14T15%3A07%3A05.7743811Z'\"",
  "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test",
  "identity": null,
  "location": "eastus2",
  "name": "sjc-test",
  "provisioningState": "Succeeded",
  "resourceGroup": "sjc_rg369b61f1",
  "systemData": {
    "createdAt": "2023-08-14T15:07:05.609284+00:00",
    "createdBy": "sam.cofer@rstudio.com",
    "createdByType": "User",
    "lastModifiedAt": "2023-08-14T15:07:05.609284+00:00",
    "lastModifiedBy": "sam.cofer@rstudio.com",
    "lastModifiedByType": "User"
  },
  "tags": null,
  "type": "Microsoft.NetApp/netAppAccounts"
}
PS C:\Users\samco> az netappfiles pool list --account-name sjc-test --resource-group sjc_rg369b61f1
[
  {
    "coolAccess": false,
    "encryptionType": "Single",
    "etag": "W/\"datetime'2023-08-14T16%3A06%3A51.5285364Z'\"",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-prem",
    "location": "eastus2",
    "name": "sjc-test/sjc-test-prem",
    "poolId": "69a40238-1335-e01a-c2dc-bbe9b354de96",
    "provisioningState": "Succeeded",
    "qosType": "Auto",
    "resourceGroup": "sjc_rg369b61f1",
    "serviceLevel": "Premium",
    "size": 2199023255552,
    "systemData": {
      "createdAt": "2023-08-14T15:14:36.785748+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-14T15:14:36.785748+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "tags": null,
    "totalThroughputMibps": 128.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools",
    "utilizedThroughputMibps": 128.0
  },
  {
    "coolAccess": false,
    "encryptionType": "Single",
    "etag": "W/\"datetime'2023-08-17T13%3A18%3A54.7822426Z'\"",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-standard",
    "location": "eastus2",
    "name": "sjc-test/sjc-test-standard",
    "poolId": "ea56e993-346b-6fcc-58bd-285471b8bd20",
    "provisioningState": "Succeeded",
    "qosType": "Auto",
    "resourceGroup": "sjc_rg369b61f1",
    "serviceLevel": "Standard",
    "size": 2199023255552,
    "systemData": {
      "createdAt": "2023-08-17T13:17:46.426776+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-17T13:17:46.426776+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "tags": null,
    "totalThroughputMibps": 32.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools",
    "utilizedThroughputMibps": 32.0
  },
  {
    "coolAccess": false,
    "encryptionType": "Single",
    "etag": "W/\"datetime'2023-08-17T17%3A25%3A29.7754123Z'\"",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-ultra",
    "location": "eastus2",
    "name": "sjc-test/sjc-test-ultra",
    "poolId": "20231564-ea4e-f1b8-e66c-5539ff52091f",
    "provisioningState": "Succeeded",
    "qosType": "Auto",
    "resourceGroup": "sjc_rg369b61f1",
    "serviceLevel": "Ultra",
    "size": 2199023255552,
    "systemData": {
      "createdAt": "2023-08-17T17:11:50.516979+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-17T17:11:50.516979+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "tags": null,
    "totalThroughputMibps": 256.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools",
    "utilizedThroughputMibps": 256.0
  }
]

PS C:\Users\samco> az netappfiles volume list --account-name sjc-test --resource-group sjc_rg369b61f1 --pool-name "sjc-test-ultra"
[
  {
    "avsDataStore": "Disabled",
    "backupId": null,
    "baremetalTenantId": "baremetalTenant_svm_5e08749d4f9047fc9caa1285bc868b77_453add3c",
    "capacityPoolResourceId": null,
    "cloneProgress": null,
    "coolAccess": false,
    "coolnessPeriod": null,
    "creationToken": "sjc-test-ultra-vol",
    "dataProtection": null,
    "defaultGroupQuotaInKiBs": 0,
    "defaultUserQuotaInKiBs": 0,
    "deleteBaseSnapshot": false,
    "enableSubvolumes": "Disabled",
    "encrypted": null,
    "encryptionKeySource": "Microsoft.NetApp",
    "etag": "W/\"datetime'2023-08-17T17%3A25%3A29.9526342Z'\"",
    "exportPolicy": {
      "rules": [
        {
          "allowedClients": "0.0.0.0/0",
          "chownMode": "Restricted",
          "cifs": false,
          "hasRootAccess": true,
          "kerberos5IReadOnly": false,
          "kerberos5IReadWrite": false,
          "kerberos5PReadOnly": false,
          "kerberos5PReadWrite": false,
          "kerberos5ReadOnly": false,
          "kerberos5ReadWrite": false,
          "nfsv3": false,
          "nfsv41": true,
          "ruleIndex": 1,
          "unixReadOnly": false,
          "unixReadWrite": true
        }
      ]
    },
    "fileSystemId": "bda56eee-fc8e-fa7e-ed1d-b3de5ebea1f2",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-ultra/volumes/sjc-test-ultra-vol",
    "isDefaultQuotaEnabled": false,
    "isRestoring": null,
    "kerberosEnabled": false,
    "keyVaultPrivateEndpointResourceId": null,
    "ldapEnabled": false,
    "location": "eastus2",
    "maximumNumberOfFiles": 100000000,
    "mountTargets": [
      {
        "fileSystemId": "bda56eee-fc8e-fa7e-ed1d-b3de5ebea1f2",
        "ipAddress": "10.11.11.4",
        "mountTargetId": "bda56eee-fc8e-fa7e-ed1d-b3de5ebea1f2",
        "smbServerFqdn": null
      }
    ],
    "name": "sjc-test/sjc-test-ultra/sjc-test-ultra-vol",
    "networkFeatures": "Standard",
    "networkSiblingSetId": "6565af0b-1a44-326b-26a8-785e25c35ff0",
    "placementRules": null,
    "protocolTypes": [
      "NFSv4.1"
    ],
    "provisioningState": "Succeeded",
    "proximityPlacementGroup": null,
    "resourceGroup": "sjc_rg369b61f1",
    "securityStyle": "Unix",
    "serviceLevel": "Ultra",
    "smbAccessBasedEnumeration": "Disabled",
    "smbContinuouslyAvailable": false,
    "smbEncryption": false,
    "smbNonBrowsable": "Disabled",
    "snapshotDirectoryVisible": true,
    "snapshotId": null,
    "storageToNetworkProximity": "T2",
    "subnetId": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Network/virtualNetworks/sjc-server-networkf258e8ed/subnets/netapp-test",
    "systemData": {
      "createdAt": "2023-08-17T17:25:23.503962+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-17T17:25:23.503962+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "t2Network": null,
    "tags": {},
    "throughputMibps": 256.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools/volumes",
    "unixPermissions": "0770",
    "usageThreshold": 2199023255552,
    "volumeGroupName": null,
    "volumeSpecName": null,
    "volumeType": "",
    "zones": []
  }
]
PS C:\Users\samco> az netappfiles volume list --account-name sjc-test --resource-group sjc_rg369b61f1 --pool-name "sjc-test-prem"
[
  {
    "avsDataStore": "Disabled",
    "backupId": null,
    "baremetalTenantId": "baremetalTenant_svm_5e08749d4f9047fc9caa1285bc868b77_453add3c",
    "capacityPoolResourceId": null,
    "cloneProgress": null,
    "coolAccess": false,
    "coolnessPeriod": null,
    "creationToken": "sjc-test-prem-vol",
    "dataProtection": null,
    "defaultGroupQuotaInKiBs": 0,
    "defaultUserQuotaInKiBs": 0,
    "deleteBaseSnapshot": false,
    "enableSubvolumes": "Disabled",
    "encrypted": null,
    "encryptionKeySource": "Microsoft.NetApp",
    "etag": "W/\"datetime'2023-08-14T16%3A06%3A51.657969Z'\"",
    "exportPolicy": {
      "rules": [
        {
          "allowedClients": "0.0.0.0/0",
          "chownMode": "Restricted",
          "cifs": false,
          "hasRootAccess": true,
          "kerberos5IReadOnly": false,
          "kerberos5IReadWrite": false,
          "kerberos5PReadOnly": false,
          "kerberos5PReadWrite": false,
          "kerberos5ReadOnly": false,
          "kerberos5ReadWrite": false,
          "nfsv3": false,
          "nfsv41": true,
          "ruleIndex": 1,
          "unixReadOnly": false,
          "unixReadWrite": true
        }
      ]
    },
    "fileSystemId": "2ac75f53-41ae-9daf-58a3-6477be39e7ef",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-prem/volumes/sjc-test-prem-vol",
    "isDefaultQuotaEnabled": false,
    "isRestoring": null,
    "kerberosEnabled": false,
    "keyVaultPrivateEndpointResourceId": null,
    "ldapEnabled": false,
    "location": "eastus2",
    "maximumNumberOfFiles": 100000000,
    "mountTargets": [
      {
        "fileSystemId": "2ac75f53-41ae-9daf-58a3-6477be39e7ef",
        "ipAddress": "10.11.11.4",
        "mountTargetId": "2ac75f53-41ae-9daf-58a3-6477be39e7ef",
        "smbServerFqdn": null
      }
    ],
    "name": "sjc-test/sjc-test-prem/sjc-test-prem-vol",
    "networkFeatures": "Standard",
    "networkSiblingSetId": "6565af0b-1a44-326b-26a8-785e25c35ff0",
    "placementRules": null,
    "protocolTypes": [
      "NFSv4.1"
    ],
    "provisioningState": "Succeeded",
    "proximityPlacementGroup": null,
    "resourceGroup": "sjc_rg369b61f1",
    "securityStyle": "Unix",
    "serviceLevel": "Premium",
    "smbAccessBasedEnumeration": "Disabled",
    "smbContinuouslyAvailable": false,
    "smbEncryption": false,
    "smbNonBrowsable": "Disabled",
    "snapshotDirectoryVisible": true,
    "snapshotId": null,
    "storageToNetworkProximity": "T2",
    "subnetId": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Network/virtualNetworks/sjc-server-networkf258e8ed/subnets/netapp-test",
    "systemData": {
      "createdAt": "2023-08-14T16:02:49.674522+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-14T16:02:49.674522+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "t2Network": null,
    "tags": {},
    "throughputMibps": 128.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools/volumes",
    "unixPermissions": "0770",
    "usageThreshold": 2199023255552,
    "volumeGroupName": null,
    "volumeSpecName": null,
    "volumeType": "",
    "zones": []
  }
]
PS C:\Users\samco> az netappfiles volume list --account-name sjc-test --resource-group sjc_rg369b61f1 --pool-name "sjc-test-standard"
[
  {
    "avsDataStore": "Disabled",
    "backupId": null,
    "baremetalTenantId": "baremetalTenant_svm_5e08749d4f9047fc9caa1285bc868b77_453add3c",
    "capacityPoolResourceId": null,
    "cloneProgress": null,
    "coolAccess": false,
    "coolnessPeriod": null,
    "creationToken": "sjc-test-standard-export",
    "dataProtection": null,
    "defaultGroupQuotaInKiBs": 0,
    "defaultUserQuotaInKiBs": 0,
    "deleteBaseSnapshot": false,
    "enableSubvolumes": "Disabled",
    "encrypted": null,
    "encryptionKeySource": "Microsoft.NetApp",
    "etag": "W/\"datetime'2023-08-17T13%3A18%3A54.8927571Z'\"",
    "exportPolicy": {
      "rules": [
        {
          "allowedClients": "0.0.0.0/0",
          "chownMode": "Restricted",
          "cifs": false,
          "hasRootAccess": true,
          "kerberos5IReadOnly": false,
          "kerberos5IReadWrite": false,
          "kerberos5PReadOnly": false,
          "kerberos5PReadWrite": false,
          "kerberos5ReadOnly": false,
          "kerberos5ReadWrite": false,
          "nfsv3": false,
          "nfsv41": true,
          "ruleIndex": 1,
          "unixReadOnly": false,
          "unixReadWrite": true
        }
      ]
    },
    "fileSystemId": "7872a6a0-e297-b7dc-3552-9a4b9cd0d770",
    "id": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.NetApp/netAppAccounts/sjc-test/capacityPools/sjc-test-standard/volumes/sjc-test-standard-vol",
    "isDefaultQuotaEnabled": false,
    "isRestoring": null,
    "kerberosEnabled": false,
    "keyVaultPrivateEndpointResourceId": null,
    "ldapEnabled": false,
    "location": "eastus2",
    "maximumNumberOfFiles": 100000000,
    "mountTargets": [
      {
        "fileSystemId": "7872a6a0-e297-b7dc-3552-9a4b9cd0d770",
        "ipAddress": "10.11.11.4",
        "mountTargetId": "7872a6a0-e297-b7dc-3552-9a4b9cd0d770",
        "smbServerFqdn": null
      }
    ],
    "name": "sjc-test/sjc-test-standard/sjc-test-standard-vol",
    "networkFeatures": "Standard",
    "networkSiblingSetId": "6565af0b-1a44-326b-26a8-785e25c35ff0",
    "placementRules": null,
    "protocolTypes": [
      "NFSv4.1"
    ],
    "provisioningState": "Succeeded",
    "proximityPlacementGroup": null,
    "resourceGroup": "sjc_rg369b61f1",
    "securityStyle": "Unix",
    "serviceLevel": "Standard",
    "smbAccessBasedEnumeration": "Disabled",
    "smbContinuouslyAvailable": false,
    "smbEncryption": false,
    "smbNonBrowsable": "Disabled",
    "snapshotDirectoryVisible": true,
    "snapshotId": null,
    "storageToNetworkProximity": "T2",
    "subnetId": "/subscriptions/cdc5ba7c-38d0-43f9-9670-7b37680ad295/resourceGroups/sjc_rg369b61f1/providers/Microsoft.Network/virtualNetworks/sjc-server-networkf258e8ed/subnets/netapp-test",
    "systemData": {
      "createdAt": "2023-08-17T13:18:44.649076+00:00",
      "createdBy": "sam.cofer@rstudio.com",
      "createdByType": "User",
      "lastModifiedAt": "2023-08-17T13:18:44.649076+00:00",
      "lastModifiedBy": "sam.cofer@rstudio.com",
      "lastModifiedByType": "User"
    },
    "t2Network": null,
    "tags": {},
    "throughputMibps": 32.0,
    "type": "Microsoft.NetApp/netAppAccounts/capacityPools/volumes",
    "unixPermissions": "0770",
    "usageThreshold": 2199023255552,
    "volumeGroupName": null,
    "volumeSpecName": null,
    "volumeType": "",
    "zones": []
  }
]
```