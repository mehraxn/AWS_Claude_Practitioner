# Amazon Elastic Block Store (Amazon EBS)

## Simple AWS exam explanation

**Amazon EBS** is a **block storage service** in AWS.

The easiest way to remember it is this:

* **Amazon EC2** = the virtual server
* **Amazon EBS** = the virtual hard disk attached to that server

So when you launch an EC2 instance, the operating system, applications, and files can be stored on an **EBS volume**.

---

## 1) What EBS really is

Amazon EBS provides **persistent block storage** for EC2 instances.

Let’s break that down:

### Persistent

This means the data **stays there even if the EC2 instance stops**.

That is very important for the exam.

* If an EC2 instance is **stopped**, EBS data normally remains.
* If an EC2 instance is **restarted**, EBS data remains.
* If an EC2 instance is **terminated**, the EBS volume may be deleted or kept depending on the settings.

### Block storage

Block storage means the storage is presented to the operating system like a **raw disk drive**.

The OS can then:

* create a file system on it
* format it
* mount it
* use it like a normal disk

This is different from:

* **object storage** like Amazon S3
* **file storage** like Amazon EFS

---

## 2) The main idea for the exam

Think of EBS as:

**durable storage for one EC2 instance at a time**

That sentence helps a lot in AWS questions.

### Why?

Because EBS is designed mainly to be attached to **a single EC2 instance** in the same Availability Zone.

So if the question is about:

* a boot disk for EC2
* a database disk for one server
* persistent storage for a virtual machine

then **EBS is often the correct answer**.

---

## 3) Where EBS is used

Amazon EBS is commonly used for:

### Boot volumes

The root volume of an EC2 instance is often an EBS volume.

That means:

* the operating system can be stored on EBS
* the instance can boot from EBS

### Application storage

Applications running on EC2 can store files and data on EBS.

### Databases

Databases need storage with good performance and low latency.
EBS is commonly used for databases running on EC2.

### Long-term persistent data for one server

If a server needs data to survive stop/start, EBS is a strong choice.

---

## 4) EBS vs instance store

This is a very common exam comparison.

### EBS

* persistent
* data survives stop/start
* network-attached storage for EC2
* can be snapshotted
* good for important data

### Instance store

* temporary storage
* data is lost if the instance stops, terminates, or underlying host changes
* physically attached to the host machine
* good for buffers, caches, temporary files, scratch data

### Exam shortcut

* Need **persistent** storage? → **EBS**
* Need **temporary** very short-lived storage? → **Instance store**

---

## 5) EBS vs S3 vs EFS

Another popular exam area.

### EBS

* block storage
* attached to EC2
* usually one instance at a time
* great for boot volumes and databases

### S3

* object storage
* accessed through APIs, not mounted like a normal block disk by default
* ideal for backups, files, media, logs, static website assets

### EFS

* file storage
* shared file system
* multiple EC2 instances can access it at the same time
* ideal when many servers need the same files

### Exam shortcut

* One server needs a disk → **EBS**
* Shared file system for many servers → **EFS**
* Store objects/files at massive scale → **S3**

---

## 6) Important characteristics of EBS

## a) EBS is tied to an Availability Zone

An EBS volume is created in **one Availability Zone (AZ)**.

That means:

* the volume and the EC2 instance must be in the **same AZ** to attach directly
* you cannot directly attach an EBS volume from one AZ to an instance in another AZ

This is very testable.

---

## b) EBS is replicated within its Availability Zone

EBS is designed to be highly available and durable **within the same AZ**.

So AWS protects the volume inside that AZ.

But remember:

* EBS is **not automatically a cross-region service**
* EBS is **not automatically multi-AZ storage**

If you want backup or copy outside the AZ, snapshots are important.

---

## c) EBS supports snapshots

A snapshot is a **backup of an EBS volume** stored in Amazon S3.

Snapshots are very important in the exam.

You can use them to:

* back up a volume
* restore a volume
* create a new volume
* copy data to another AZ or another Region

### Key exam point

**Snapshots are incremental**.
This means after the first full snapshot, later snapshots save only the changed blocks.

---

## d) EBS volumes can be resized

You can modify many EBS volumes without rebuilding everything.

For example, you can often change:

* size
* performance characteristics
* volume type

This gives flexibility when your workload grows.

---

## e) Encryption is supported

EBS supports encryption for data:

* at rest
* in transit between EC2 and EBS (in supported scenarios)
* in snapshots

For the exam, remember this simple idea:

**If security of stored disk data is required, EBS encryption is a common answer.**

---

## 7) Volume types you should know

AWS offers different EBS volume types. For the exam, focus on the idea that some are for **general use**, some for **high performance**, and some for **throughput-heavy HDD workloads**.

## a) SSD-based volumes

These are best when you need fast access and low latency.

### General Purpose SSD

Usually the default choice for many workloads.
Good balance of:

* price
* performance
* flexibility

Use cases:

* boot volumes
* small and medium databases
* development environments
* general application servers

### Provisioned IOPS SSD

Used when you need very high performance and predictable IOPS.

Use cases:

* critical databases
* I/O-intensive applications
* workloads that need consistent performance

---

## b) HDD-based volumes

These are more focused on throughput than low-latency random I/O.

### Throughput Optimized HDD

Good for large sequential workloads.

Use cases:

* big data
* log processing
* streaming workloads

### Cold HDD

Lower-cost option for less frequently accessed data.

Use cases:

* infrequently accessed large datasets
* lower-cost throughput workloads

---

## 8) What EBS is best for

EBS is best when you need:

* a disk for an EC2 instance
* persistent storage
* a boot volume
* low-latency storage for one server
* database storage on EC2
* snapshots and restore capability

---

## 9) What EBS is NOT best for

EBS is usually **not** the best answer when you need:

### Shared storage for many EC2 instances at once

That usually points more to **Amazon EFS**.

### Internet-scale object storage

That usually points to **Amazon S3**.

### Storage that disappears with the instance and is okay to lose

That may point to **instance store**.

### A managed database service

If the question is really asking for the database service itself, that may point to **Amazon RDS**, not EBS.

---

## 10) Common AWS exam traps

## Trap 1: “Persistent storage” vs “temporary storage”

* Persistent → EBS
* Temporary → Instance store

## Trap 2: “Shared by many instances”

* Shared file system → EFS
* Single server disk → EBS

## Trap 3: “Backup of EBS”

* Backup mechanism → Snapshot

## Trap 4: “Across Regions”

EBS volume itself is not a global storage service.
To move or copy, snapshots are commonly used.

## Trap 5: “Boot volume for EC2”

This often points directly to **EBS**.

---

## 11) Easy real-world example

Imagine you launch an EC2 virtual machine for a web application.

You may use:

* one EBS volume for the operating system
* another EBS volume for the application data
* snapshots to back them up

If the server stops and starts again, the data on EBS is still there.

That is why EBS is very useful.

---

## 12) Simple memory trick

Remember this line:

**EBS = Elastic Block Store = EC2 disk**

And another one:

**EBS is to EC2 like a hard drive is to a computer.**

These memory tricks work very well in the AWS exam.

---

## 13) Mini comparison table

| Service        | Storage type            | Main use                                  |
| -------------- | ----------------------- | ----------------------------------------- |
| Amazon EBS     | Block storage           | Disk for one EC2 instance                 |
| Amazon EFS     | File storage            | Shared file system for many EC2 instances |
| Amazon S3      | Object storage          | Scalable object/file storage              |
| Instance store | Temporary block storage | Scratch, cache, buffer                    |

---

## 14) Exam-style summary

If the exam says:

* “persistent block storage for EC2” → **Amazon EBS**
* “boot volume for EC2” → **Amazon EBS**
* “database disk attached to EC2” → **Amazon EBS**
* “backup of an EBS volume” → **snapshot**
* “shared file storage for multiple instances” → **Amazon EFS**
* “temporary storage that can be lost” → **instance store**

---

## 15) Final one-paragraph answer

**Amazon Elastic Block Store (Amazon EBS)** is an AWS service that provides **persistent block storage for Amazon EC2 instances**. It acts like a **virtual hard drive** for a server in the cloud. EBS is commonly used for **boot volumes, application data, and databases**, and it supports **snapshots, resizing, and encryption**. It is usually attached to **one EC2 instance at a time** in the **same Availability Zone**, which makes it a very common answer in AWS exam questions about **persistent disk storage for EC2**.

---

## 16) Super short exam answer

**Amazon EBS is persistent block storage for EC2, like a hard disk attached to a virtual server.**
