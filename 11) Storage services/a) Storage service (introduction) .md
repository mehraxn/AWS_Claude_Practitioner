# Storage Services (AWS) — README

This README summarizes the **main AWS storage services** you should know for hands-on use and for the **AWS Cloud Practitioner** exam. It focuses on *what each service is*, *when to use it*, and *how to choose the right one*.

## Contents

* [Types of Storage Services](#types-of-storage-services)
* [Introduction to Amazon S3](#introduction-to-amazon-s3)
* [S3 Storage Classes](#s3-storage-classes)
* [AWS Snow Family](#aws-snow-family)
* [Other Core Storage Services](#other-core-storage-services)
* [Quick Comparison Cheat Sheet](#quick-comparison-cheat-sheet)
* [Security, Durability, and Best Practices](#security-durability-and-best-practices)

---

## Types of Storage Services

AWS storage commonly falls into three core models:

### 1) Object storage

**Best for:** files, media, backups, data lakes, logs, static websites.

* Data is stored as **objects** (data + metadata + unique key).
* Highly scalable, accessed over HTTP/HTTPS.
* Example: **Amazon S3**.

### 2) Block storage

**Best for:** operating system disks, databases, low-latency transactional apps.

* Storage is presented as **raw blocks** that a server formats as a file system.
* Usually attached to a compute instance (like a virtual hard drive).
* Example: **Amazon EBS** (Elastic Block Store).

### 3) File storage

**Best for:** shared folders, content management, lift-and-shift apps, POSIX-style access.

* Provides a **shared file system** with directories and file permissions.
* Multiple servers can mount the same file system.
* Example: **Amazon EFS** (Elastic File System).

> **Rule of thumb**
>
> * If you want “store files at internet scale” → **S3 (object)**
> * If you want “a disk for my server/database” → **EBS (block)**
> * If you want “a shared network drive for many servers” → **EFS (file)**

---

## Introduction to Amazon S3

**Amazon S3 (Simple Storage Service)** is AWS’s flagship **object storage** service.

### Key concepts

* **Bucket**: a top-level container for objects.
* **Object**: the actual stored data (file) + metadata.
* **Key**: the object’s “name/path” inside the bucket.

### Bucket vs Object (common exam question)

* **Bucket** = the container (like a folder at the top level).
* **Object** = the file stored inside (like `photo.jpg`).
* Buckets hold **many objects**; objects live **inside exactly one bucket**.

### What S3 is used for

* Backups and archival
* Static website hosting
* Media storage (images, videos)
* Data lakes and analytics storage
* Application assets (logs, exports, uploads)

### Important properties

* **Durability**: designed for extremely high durability (think “very unlikely to lose data”).
* **Scalability**: can store virtually unlimited objects.
* **Access**: typically via **API**, **CLI**, **SDK**, or AWS Console.
* **Consistency**: S3 provides **strong read-after-write consistency** for PUTs and DELETEs.

### Common S3 features to know

* **Versioning**: keep multiple versions of an object (protects against accidental deletion/overwrite).
* **Lifecycle policies**: automatically transition objects to cheaper storage classes or expire them.
* **Replication**:

  * **SRR** (Same-Region Replication)
  * **CRR** (Cross-Region Replication)
* **Static website hosting**: host simple sites from a bucket (often paired with CloudFront).

---

## S3 Storage Classes

S3 storage classes trade off **cost** vs **retrieval speed** vs **minimum storage duration**.

### Frequently used classes

* **S3 Standard**: default, general-purpose, frequent access.
* **S3 Intelligent-Tiering**: automatically moves objects between access tiers based on usage.
* **S3 Standard-IA (Infrequent Access)**: cheaper storage, higher retrieval cost; good for long-lived but occasionally accessed data.
* **S3 One Zone-IA**: like Standard-IA but stored in a single AZ; cheaper, less resilient.
* **S3 Glacier Instant Retrieval**: archival with very fast access when needed.
* **S3 Glacier Flexible Retrieval**: archival with minutes-to-hours retrieval options.
* **S3 Glacier Deep Archive**: lowest cost for long-term archiving; slowest retrieval.

### How to pick (simple)

* **Frequent access** → Standard
* **Unknown access patterns** → Intelligent-Tiering
* **Rare access but need it quickly** → Standard-IA / Glacier Instant
* **Archive/compliance** → Glacier Flexible / Deep Archive

---

## AWS Snow Family

The **AWS Snow Family** is for moving data in/out of AWS when the network is too slow, too expensive, or unreliable.

### Why it exists

If you need to transfer **tens of TB to PB** of data, shipping a device can be faster than transferring over the internet.

### Devices (high level)

* **Snowcone**: small, portable, edge/field use.
* **Snowball**: larger capacity for bulk transfer.
* **Snowmobile**: massive-scale transfer (shipping-container sized) for extreme volumes.

### Common use cases

* Large data migrations to S3
* Disaster recovery seed transfers
* Edge computing in remote locations (limited connectivity)

---

## Other Core Storage Services

These services often appear alongside S3 in real architectures.

### Amazon EBS (Elastic Block Store)

**Type:** Block storage

* Attaches to **EC2** like a virtual hard disk.
* Great for **boot volumes**, **databases**, and **low-latency** workloads.
* Typically tied to a specific **Availability Zone**.
* Supports snapshots (backup/restore).

### Amazon EFS (Elastic File System)

**Type:** Managed file storage

* Shared file system for Linux workloads.
* Multiple EC2 instances can mount it concurrently.
* Scales automatically.

### Amazon FSx

**Type:** Managed file systems for specific use cases

* **FSx for Windows File Server** (Windows/SMB)
* **FSx for Lustre** (high-performance computing)
* Other variants exist for specialized workloads.

### AWS Storage Gateway

**Purpose:** Hybrid storage integration (on-prem ↔ AWS)

* Connects on-prem applications to cloud storage.
* Common modes include file, volume, and tape integrations.

### AWS DataSync

**Purpose:** Online data transfer service

* Automates and accelerates data movement between on-prem, AWS storage, and some cloud endpoints.

### AWS Transfer Family

**Purpose:** Managed file transfer

* Supports protocols like SFTP/FTPS/FTP to move data into/out of S3 or EFS.

### AWS Backup

**Purpose:** Centralized backup management

* Helps manage backups across services (policies, retention, compliance).

---

## Quick Comparison Cheat Sheet

| Service             | Storage Type  | Typical Scope                                   | Best For                   | Simple mental model               |
| ------------------- | ------------- | ----------------------------------------------- | -------------------------- | --------------------------------- |
| **S3**              | Object        | Regional service (global namespace for buckets) | files, backups, data lakes | “Internet-scale file cabinet”     |
| **EBS**             | Block         | AZ-scoped (attached to EC2)                     | disks, databases           | “Hard drive for one server”       |
| **EFS**             | File          | Regional (multi-AZ)                             | shared folders             | “Network shared drive”            |
| **FSx**             | File          | Regional                                        | Windows/HPC file systems   | “Specialized managed file server” |
| **Snow**            | Transfer/Edge | Physical device                                 | huge migrations            | “Ship your data”                  |
| **Storage Gateway** | Hybrid        | On-prem + AWS                                   | hybrid integration         | “Bridge to the cloud”             |
| **DataSync**        | Transfer      | Online                                          | fast copying               | “Managed copy job”                |

---

## Security, Durability, and Best Practices

### Access control

* **IAM policies**: control who can access which resources.
* **Bucket policies (S3)**: resource-based access control at the bucket level.
* **ACLs**: legacy object-level access control (know it exists; avoid unless needed).

### Encryption

* **At rest**: use SSE (S3-managed keys) or KMS where required.
* **In transit**: use HTTPS/TLS.

### Data protection & recovery

* Enable **versioning** for important S3 buckets.
* Use **lifecycle rules** to control cost (transition to colder tiers, expire old data).
* Use **replication** for cross-region resiliency.
* Use **snapshots** for EBS backup and recovery.

### Cost tips (exam-friendly)

* Storage is cheaper than retrieval in many “cold” tiers.
* Use **Intelligent-Tiering** when access patterns are unknown.
* Use **Glacier/Deep Archive** for compliance and long-term archival.

---

## Mini Decision Guide

* “I need to store a lot of files and access them via web/API” → **S3**
* “I need a disk for my EC2 instance or database” → **EBS**
* “Many EC2 instances must share the same files” → **EFS**
* “I have Windows file sharing requirements” → **FSx for Windows**
* “My internet transfer will take weeks” → **Snow Family**
* “I need hybrid on-prem + cloud storage” → **Storage Gateway**

---

### Suggested next steps

* Practice identifying the right storage type (object vs block vs file) from a scenario.
* Memorize the *core purpose* of S3, EBS, EFS, and Snow Family — these appear often in foundational exams.
