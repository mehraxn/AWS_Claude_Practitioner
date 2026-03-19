# Aurora Provisioned

## Simple definition

Aurora provisioned means you run Amazon Aurora with fixed database instances that you choose ahead of time.

You pick the DB instance class, such as how much CPU and memory you want, and Aurora runs your database on that capacity until you change it.

---

## Core idea in plain English

Think of Aurora provisioned like renting a car of a specific size.

You choose the size first, pay for that size, and keep using it until you decide to switch to a bigger or smaller one.

This is different from a serverless model, where capacity can scale more automatically based on demand.

---

## Main use cases

Aurora provisioned is a good choice when

 You want predictable performance
 Your database workload is steady or easy to forecast
 You need full control over instance size
 Your application is business-critical and needs high availability
 You want to use reader instances to scale reads
 You want a relational database that is compatible with MySQL or PostgreSQL

---

## Key features

### 1. Managed relational database

Aurora is a fully managed database service from AWS.

AWS handles many operational tasks like backups, patching support, monitoring integration, and recovery features.

### 2. Provisioned compute capacity

You choose the database instance size yourself.

This gives you fixed, planned compute capacity instead of automatic serverless-style scaling.

### 3. Shared cluster storage

Aurora separates compute from storage.

Your DB instances use a shared cluster storage volume, and Aurora automatically grows storage as needed.

### 4. High availability

Aurora stores data across multiple Availability Zones.

This improves durability and helps with failover.

### 5. Read scaling

You can add Aurora Replicas to handle read traffic.

This is useful for read-heavy applications.

### 6. Fast failover support

If the primary instance fails, Aurora can promote a replica.

This helps reduce downtime.

### 7. MySQL and PostgreSQL compatibility

Aurora works with engines that are compatible with

 Aurora MySQL
 Aurora PostgreSQL

---

## How it works

An Aurora provisioned cluster usually has

 One writer instance for read and write operations
 Optional reader instances for read-only traffic
 Shared storage used by all instances in the cluster

Here is the simple flow

1. You create an Aurora DB cluster.
2. You choose provisioned DB instances.
3. One instance becomes the primary writer.
4. You can add replicas for more read capacity.
5. Aurora stores the data across multiple Availability Zones.
6. If the writer fails, Aurora can fail over to a replica.

Important idea for the exam

Storage and compute are separate in Aurora.

You size the instances for compute, while Aurora storage grows automatically behind the scenes.

---

## Why it is important for the exam

Aurora provisioned matters because the Cloud Practitioner exam often checks whether you can

 Recognize managed database services
 Understand the difference between provisioned and serverless
 Know when AWS handles infrastructure for you
 Identify services designed for high availability, scalability, and relational data

For the exam, remember this

 Aurora is a relational database
 Aurora is part of the Amazon RDS family
 Provisioned means you choose the instance capacity yourself
 Aurora is designed for performance, availability, and managed operations

---

## Related AWS services and differences

## Amazon RDS for MySQLPostgreSQL vs Aurora Provisioned

Amazon RDS supports common database engines like MySQL and PostgreSQL.

Aurora is AWS’s cloud-native relational database built for higher performance and availability.

Simple difference

 RDS MySQLPostgreSQL = managed traditional database engines
 Aurora provisioned = managed AWS-built relational engine with Aurora architecture

## Aurora Provisioned vs Aurora Serverless v2

This is a very important exam comparison.

### Aurora Provisioned

 You choose the DB instance size
 Capacity is more fixed until you modify it
 Good for predictable workloads

### Aurora Serverless v2

 Capacity adjusts more automatically based on demand
 Billing is based on Aurora capacity usage instead of fixed instance hours
 Good for variable or unpredictable workloads

Easy comparison

 Provisioned = choose size yourself
 Serverless = AWS adjusts compute capacity within limits you set

## Aurora vs DynamoDB

 Aurora = relational database, SQL, structured data, joins
 DynamoDB = NoSQL key-valuedocument database, very high scale, different access pattern

If the question says relational database, think Aurora or RDS, not DynamoDB.

## Aurora vs Redshift

 Aurora = transactional relational database for application workloads
 Redshift = data warehouse for analytics and large-scale reporting

If the question is about running an application database, Aurora fits better.

---

## Common exam traps

### Trap 1 Confusing Aurora with DynamoDB

Aurora is relational.

DynamoDB is NoSQL.

### Trap 2 Thinking “provisioned” means on-premises style self-management

No.

Aurora provisioned is still fully managed by AWS.

You choose the instance size, but AWS still manages much of the heavy operational work.

### Trap 3 Forgetting that Aurora storage is separate from compute

In Aurora, storage is part of the cluster design and grows automatically.

Provisioned mainly refers to the compute instances you choose.

### Trap 4 Mixing up Aurora Provisioned and Aurora Serverless

 Provisioned = fixed instance class you select
 Serverless = capacity adjusts automatically

### Trap 5 Choosing Aurora for non-relational use cases

If the exam asks for a NoSQL database with key-value access at huge scale, the better answer is usually DynamoDB.

---

## Easy real-world example

A company runs an online shopping website.

It has steady traffic every day and wants a fast relational database for orders, customers, and payments.

The company chooses Aurora provisioned because

 It wants predictable database performance
 It knows roughly how much capacity it needs
 It wants high availability
 It wants read replicas for reporting and read-heavy traffic

This is a classic Aurora provisioned use case.

---

## Final summary

Aurora provisioned is Amazon Aurora running on database instances that you size and choose yourself.

It is a managed relational database designed for high performance, high availability, and read scaling.

The biggest exam idea is this

Provisioned means fixed chosen compute capacity, while Aurora still gives you managed operations and shared, automatically growing storage.

---

## Short exam answer

Aurora provisioned is a fully managed relational database deployment model for Amazon Aurora where you choose fixed DB instance capacity in advance, making it a good fit for predictable workloads that need performance, availability, and read scaling.

---

## Memory trick

### “Provisioned = Pre-picked power”

Use this memory trick

Provisioned = you pre-pick the database size.

So if the exam says the company wants a relational database and wants to choose a known database size for predictable usage, think

Aurora Provisioned.
