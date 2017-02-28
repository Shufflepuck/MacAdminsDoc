Storage Structure
=================


Partition Schemes
-----------------


- **Apple Partition Map (APM)**: This is the traditional Apple partitioning scheme used to start up a PowerPC-based Macintosh computer, to use the disk as a non-startup disk with any Mac, or to create a multiplatform compatible startup disk. 
- **Master Boot Record (MBR)**: This is the DOS/Windows-compatible partitioning scheme.
- **GUID Partitioning Table (GPT)**: This is the partitioning scheme used to start up an Intel-based Macintosh Computer.

+---------+-------------------------+-------------------------------------------------------------------------+
| Acronym | Name                    | Description                                                             |
+---------+-------------------------+-------------------------------------------------------------------------+
| APM     | Apple Partition Map     | This is the traditional Apple partitioning scheme used to start up a    |
|         |                         | PowerPC-based Macintosh computer, to use the disk as a non-startup disk |
|         |                         | with any Mac, or to create a multiplatform compatible startup disk.     |
+---------+-------------------------+-------------------------------------------------------------------------+
| MBR     | Master Boot Record      | This is the DOS/Windows-compatible partitioning scheme.                 |
+---------+-------------------------+-------------------------------------------------------------------------+
| GPT     | GUID Partitioning Table | This is the partitioning scheme used to start up an Intel-based         |
|         |                         | Macintosh computer.                                                     |
+---------+-------------------------+-------------------------------------------------------------------------+

Source: [diskutil(8)](x-man-page://8/diskutil)

Filesystems
-----------

========================================	==============================================	===========
Acronym										Name											Description
========================================	==============================================	===========
APFS 										APFS                                            
ExFAT										ExFAT                                           
Free Space (or free)						Free Space                                      
MS-DOS										MS-DOS (FAT)                                    
MS-DOS FAT12								MS-DOS (FAT12)                                  
MS-DOS FAT16								MS-DOS (FAT16)                                  
MS-DOS FAT32 (or fat32)						MS-DOS (FAT)
HFS+										Mac OS Extended                                 
Case-sensitive HFS+ (or hfsx)				Mac OS Extended (Case-sensitive)
Case-sensitive Journaled HFS+ (or jhfsx)	Mac OS Extended (Case-sensitive, Journaled)
Journaled HFS+ (or jhfs+)					Mac OS Extended (Journaled)

Source: `diskutil(8) <x-man-page://8/diskutil>`

APFS
^^^^

APFS is the new FileSystem that was announced at WWDC '16. It will be available on all Mac and iOS devices in 2017.

It features awesome new and improved features such as:

- Clones
- Snapshots
- Space Sharing
- Encryption
- Crash Protection
- Sparse Files
- Fast Directory Sizing
- Atomic Safe-Save


Rich Trouton did a very interesting talk at MacAdUk. Grab it [here](https://drive.google.com/file/d/0B7Ptn5b5q2FLMUdsLTdUMjBHVzQ/edit).

Source: `APFS Guide <https://developer.apple.com/library/prerelease/content/documentation/FileManagement/Conceptual/APFS_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40016999-CH1-DontLinkElementID_18>`

CoreStorage
-----------

+-------+----+-----------+
|Acronym|Name|Description|

|LVG|Logical Volume Group||
+-------+----+-----------+
|PV|Physical Volume||
+-------+----+-----------+
|LVF|Logical Volume Family||
+-------+----+-----------+
|LV|Logical Volume||
+-------+----+-----------+

Source: `diskutil(8) <x-man-page://8/diskutil>`
