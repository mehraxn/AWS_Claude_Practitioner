# AWS Storage Services — README (Independent Notes)

This README explains the **three fundamental storage models** commonly used in AWS and in general IT:

* **Block storage** (Amazon **EBS**)
* **File storage** (Amazon **EFS**)
* **Object storage** (Amazon **S3**)

It is written as standalone notes (not tied to any diagram) and includes the key points you should remember for practice and the AWS Cloud Practitioner exam.

---

## 1) Block Storage — Amazon EBS

### Core idea

Block storage splits data into **evenly sized blocks** and presents the storage to an operating system as a **disk device**.

### Key points

* **Data format:** evenly split **blocks**
* **Access method:** **directly accessed by the Operating System** (OS builds a file system on top)
* **Common protocols (conceptual):** FC, iSCSI (classic enterprise block access concepts)
* **Write behavior:** commonly treated as a **single-writer volume** (typical pattern is one instance writing to the volume)

### When to use

Use block storage when you need a **virtual hard drive attached to a server/VM**.

### Typical workloads

* Boot/OS disks
* Databases and other low-latency, high-IOPS applications
* Any application that expects disk + filesystem semantics

---

## 2) File Storage — Amazon EFS

### Core idea

File storage stores data as **files** with **metadata** and provides a **shared network file system** that multiple clients can mount.

### Key points

* **Data format:** files with **data + metadata**
* **Access method:** **multiple connections via a network share**
* **Common protocols (conceptual):** NFS, SMB (NFS is the typical Linux network file system protocol; SMB is common for Windows file sharing)
* **Concurrency:** supports **multiple reads**; when writing, the system may use **file locking** to coordinate access

### When to use

Use file storage when you need a **shared file share** where **multiple users or servers/VMs** must access the **same drive**.

### Typical workloads

* Shared web content across many servers
* User home directories
* Content management systems and shared application data

---

## 3) Object Storage — Amazon S3

### Core idea

Object storage stores data as **objects** where each object includes the data, metadata, and a **unique identifier** (object key). Access is typically via **HTTP/HTTPS APIs**.

### Key points

* **Data format:** objects with **data + metadata + unique ID**
* **Scale:** designed to scale massively (effectively no practical storage limit from the user perspective)
* **Access method:** **HTTPS / API** (commonly over the internet or private AWS networking)
* **Concurrency:** supports **multiple reads and writes** without traditional file locks
* **Performance note:** **not intended for high IOPS** disk-style workloads

### When to use

Use object storage when you want to **upload/store files** without managing disks, servers, or file systems.

### Typical workloads

* Backups and archival
* Media storage (images/video)
* Logs and analytics storage
* Static website assets

---

## Quick Decision Guide

* Need a **disk** for one server/VM (OS-level access) → **Block (EBS)**
* Need a **shared folder** mounted by many servers/users → **File (EFS)**
* Need to **store files as objects** accessed via API at huge scale → **Object (S3)**

---

## Summary Table

| Storage Type | AWS Example | Stored As               | Accessed Via   | Sharing               | Best For                     |
| ------------ | ----------- | ----------------------- | -------------- | --------------------- | ---------------------------- |
| Block        | EBS         | Blocks                  | OS/disk device | Usually single-writer | boot volumes, databases      |
| File         | EFS         | Files + metadata        | Network share  | Many clients          | shared folders               |
| Object       | S3          | Objects + metadata + ID | HTTPS/API      | Many clients          | uploads, backups, data lakes |
