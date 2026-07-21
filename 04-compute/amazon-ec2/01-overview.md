# Amazon EC2 — AWS Cloud Practitioner Study Note

## Simple definition

Amazon EC2 stands for Amazon Elastic Compute Cloud. It is an AWS service that gives you virtual servers in the cloud.

You can use EC2 when you need a computer that runs applications, websites, databases, scripts, or backend systems.

---

## Core idea in plain English

Think of EC2 like renting a computer on the internet.

Instead of buying a physical server, AWS lets you launch a virtual machine in minutes. You choose the CPU, memory, storage, operating system, and networking settings.

It is called elastic because you can increase or decrease resources when needed.

---

## Main use cases

EC2 is commonly used for

 Hosting websites and web applications
 Running backend business applications
 Testing and development environments
 Running batch jobs or scripts
 Hosting game servers
 Running lift-and-shift workloads moved from on-premises

For the exam, remember that EC2 is the main AWS service when you need more control over a server.

---

## Key features

### 1. Virtual servers

EC2 gives you virtual machines called instances.

### 2. Choice of instance types

You can choose different instance types based on workload needs such as

 General purpose
 Compute optimized
 Memory optimized
 Storage optimized

### 3. Elastic scaling

You can add or remove instances depending on traffic and demand.

### 4. Pay-as-you-go pricing

You usually pay only for what you use.

### 5. Different purchasing options

AWS offers several pricing models, such as

 On-Demand
 Reserved Instances
 Spot Instances
 Savings Plans

For Cloud Practitioner, you do not need deep pricing math, but you should know the basic difference.

### 6. Full operating system control

You can choose Linux or Windows and manage the software yourself.

### 7. Security controls

You can control network access using security groups.

### 8. Storage support

EC2 can use

 EBS for persistent block storage
 Instance store for temporary storage
 EFS for shared file storage in some cases

---

## How it works

Here is the basic flow

1. You choose an Amazon Machine Image (AMI)
2. You choose an instance type
3. You configure storage, networking, and security
4. You launch the EC2 instance
5. AWS starts the virtual server
6. You connect to it and install or run your application

### Important terms

#### AMI

An Amazon Machine Image is a template used to launch an instance. It includes things like the operating system and sometimes preinstalled software.

#### Instance type

This defines how much CPU, memory, and networking power the instance has.

#### Security group

A security group is like a virtual firewall for the instance.

#### Key pair

A key pair is used to securely connect to some EC2 instances, especially Linux instances.

#### EBS

Amazon EBS provides storage that stays even if the instance stops.

---

## Why it is important for the exam

EC2 is one of the most important AWS services for the Cloud Practitioner exam because it teaches core cloud ideas

 Compute in the cloud
 Elasticity
 Pay for usage instead of buying hardware
 Scalability
 Shared responsibility model

You should be able to recognize that EC2 is the right answer when the question describes

 A virtual server
 A need to install custom software
 Full OS control
 Traditional server workloads moved to AWS

---

## Related AWS services and differences

### EC2 vs Lambda

 EC2 You manage the server
 Lambda Serverless, AWS manages the infrastructure

Use EC2 when you need long-running servers or full control.
Use Lambda when you want to run code without managing servers.

### EC2 vs Elastic Beanstalk

 EC2 You manage the infrastructure yourself
 Elastic Beanstalk Easier deployment platform that can use EC2 underneath

Elastic Beanstalk is higher-level. EC2 is lower-level and gives more control.

### EC2 vs ECS  EKS

 EC2 Virtual machines
 ECS  EKS Container management services

Containers may run on EC2, but the services are not the same.

### EC2 vs Lightsail

 EC2 Flexible, powerful, more detailed control
 Lightsail Simpler, beginner-friendly, fixed-price virtual private server option

### EC2 vs AWS Fargate

 EC2 You manage the server
 Fargate Serverless compute for containers

### EC2 vs On-premises server

 EC2 No need to buy hardware, flexible, scalable, pay-as-you-go
 On-premises You buy and maintain physical servers yourself

---

## Common exam traps

### Trap 1 Confusing EC2 with serverless services

If the question says you do not want to manage servers, EC2 is usually not the best answer.

### Trap 2 Confusing EC2 with storage services

EC2 is compute, not storage.

 S3 = object storage
 EBS = block storage for EC2
 EFS = shared file storage

### Trap 3 Thinking EC2 is fully managed

EC2 is not a fully managed service. AWS manages the physical hardware, but you manage the guest OS, patches, apps, and many configurations.

### Trap 4 Forgetting elasticity

If traffic increases, you can scale EC2 using services like Auto Scaling and load balancing.

### Trap 5 Mixing up pricing options

 On-Demand = flexible, no long commitment
 Reserved = lower cost for steady usage commitment
 Spot = cheapest, but can be interrupted

### Trap 6 Assuming instance store is permanent

Instance store is temporary. If the instance stops, fails, or is terminated, that data may be lost.

---

## Easy real-world example

Imagine you are opening an online T-shirt store.

You need a server to host your website and run your custom application.
Instead of buying a real machine, you launch an EC2 instance.

You choose

 A Linux operating system
 Enough CPU and memory
 An EBS volume for storage
 A security group to allow web traffic

When more customers visit during a holiday sale, you can add more EC2 instances using Auto Scaling.

This is why EC2 is powerful it gives you a flexible server that can grow with your business.

---

## Final summary

Amazon EC2 is AWS’s main virtual server service.

It lets you run applications in the cloud with control over the operating system, compute power, storage, and networking.

For the exam, remember this simple rule

If the question needs a virtual machine or server with full control, think EC2.

---

## Short exam answer

Amazon EC2 is a cloud compute service that provides resizable virtual servers called instances. It is used when customers need control over the operating system and server environment.

---

## Memory trick

### EC2 = Easy Computer in the Cloud

This is not the official meaning, but it helps you remember.

 E = Elastic
 C2 = Cloud computer

So when you hear EC2, think

A flexible virtual computer on AWS.

---

## Quick exam coach note

For Cloud Practitioner, do not go too deep into advanced EC2 administration.

Focus on these ideas

 EC2 = virtual server
 You manage the OS and applications
 It is elastic and scalable
 It uses pricing models like On-Demand, Reserved, and Spot
 It often works with EBS, Auto Scaling, and Elastic Load Balancing

If you remember those points, you will answer most EC2 questions correctly.
