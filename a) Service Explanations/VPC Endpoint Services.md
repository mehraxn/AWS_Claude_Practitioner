# VPC Endpoint Services

## Simple definition

A **VPC endpoint service** is a way to **privately share your own service** with other VPCs using **AWS PrivateLink**. It lets consumers connect to your service **without using the public internet**.

## Core idea in plain English

Think of it like this:

* You have an application running in AWS.
* You want other AWS accounts or VPCs to use it.
* But you do **not** want to expose it with a public IP or over the internet.

A VPC endpoint service solves this by letting you publish your service privately. Other VPCs create **interface endpoints** to reach it.

### Important note about the terminology

For exam study, it helps to split the **AWS PrivateLink** model into **two main parts**:

* **VPC endpoint service** = the **provider side**
* **Interface VPC endpoint** = the **consumer side**

So, when people discuss **private VPC endpoint connectivity for custom services**, they often describe it as these two sides working together.

However, remember that **VPC endpoints** in AWS more broadly also include **gateway endpoints** for **Amazon S3** and **Amazon DynamoDB**. So do **not** think that all VPC endpoints are only endpoint services and interface endpoints.

## Main use cases

* Share an internal application privately with another AWS account
* Offer a SaaS service securely to customers
* Keep traffic inside the AWS network
* Reduce exposure to the internet
* Control who can connect to your service

## Key features

* Built on **AWS PrivateLink**
* Provides **private connectivity** between consumer VPCs and your service
* Traffic stays on the **AWS network**
* Usually backed by a **Network Load Balancer (NLB)**
* Can also be used with **Gateway Load Balancer (GWLB)** in special appliance scenarios
* Supports **access control**, so you choose who can connect
* Can require **manual acceptance** of connection requests
* Can use **private DNS names** for easier access

## How it works

### 1. Service provider side

The service owner creates:

* a service running in a VPC
* a **Network Load Balancer** in front of that service
* a **VPC endpoint service** connected to that load balancer

### 2. Service consumer side

The customer or other AWS account creates an:

* **interface VPC endpoint**

This creates elastic network interfaces with private IP addresses inside the consumer VPC.

### 3. Private connection happens

The consumer sends traffic to the interface endpoint.
That traffic is routed privately through **AWS PrivateLink** to the provider’s endpoint service.

### 4. Access is controlled

The provider can:

* allow only specific AWS accounts
* require endpoint connection approval
* monitor and manage the service centrally

## Why it is important for the exam

This topic matters because AWS exams often test whether you understand:

* **private connectivity** vs public internet access
* the difference between **endpoint service** and **VPC endpoint**
* when to use **AWS PrivateLink** instead of other networking options
* how to share services securely across accounts or VPCs

For the exam, remember this:

> **Endpoint service = provider side**
>
> **Interface endpoint = consumer side**

That is one of the most important ideas.

A good way to memorize it is this:

* **PrivateLink setup for your own service** = endpoint service + interface endpoint
* **Gateway endpoint** = separate endpoint type for S3 and DynamoDB

## Related AWS services and differences

### VPC endpoint service vs Interface VPC endpoint

* **VPC endpoint service** = the service being offered privately
* **Interface VPC endpoint** = the private connection a consumer creates to reach that service

Provider publishes. Consumer connects.

### VPC endpoint service vs Gateway endpoint

* **Endpoint service** uses **AWS PrivateLink**
* **Gateway endpoint** is only for **Amazon S3** and **Amazon DynamoDB**
* Gateway endpoints are not used to publish your own service

### VPC endpoint service vs VPC peering

* **Endpoint service / PrivateLink** connects to a specific service
* **VPC peering** connects whole VPCs at the network level
* PrivateLink is more controlled and service-focused

### VPC endpoint service vs Transit Gateway

* **PrivateLink / endpoint service** is for private access to a specific application or service
* **Transit Gateway** is for connecting many networks together, such as multiple VPCs and on-premises networks

### VPC endpoint service vs Internet Gateway / NAT Gateway

* **Endpoint service** keeps traffic private inside AWS
* **Internet Gateway** and **NAT Gateway** are used when resources need internet access

## Common exam traps

### Trap 1: Confusing endpoint service with endpoint

Many questions mix these up.

* **Endpoint service** = provider side
* **Interface endpoint** = consumer side

### Trap 2: Thinking all VPC endpoints are the same

They are not.

* **Interface endpoint** = powered by PrivateLink
* **Gateway endpoint** = for S3 and DynamoDB only
* **Endpoint service** = lets you publish your own service privately

### Trap 3: Choosing VPC peering when only one service needs to be shared

If the goal is to expose **one application privately**, PrivateLink is often the better answer.

### Trap 4: Thinking it uses the public internet

It does not. Traffic stays on the AWS network.

### Trap 5: Forgetting the load balancer

A VPC endpoint service is commonly backed by a **Network Load Balancer**.

## Easy real-world example

A company has a billing application running in a private VPC.
Its partner companies need access to that billing API.

The company does not want to make the API public.
So it:

* places the application behind a **Network Load Balancer**
* creates a **VPC endpoint service**
* allows partner AWS accounts to connect

Each partner creates an **interface VPC endpoint** in its own VPC.
Now the partners can use the billing API privately, without using the internet.

## Final summary

A VPC endpoint service lets you **privately publish your own service** to other VPCs using **AWS PrivateLink**. It is mainly a **provider-side** concept. Consumers access it by creating **interface VPC endpoints**. It is useful when you want **secure, private, service-level connectivity** without exposing services to the public internet.

## Short exam answer

**A VPC endpoint service is a provider-side AWS PrivateLink resource that lets you privately expose a service, usually behind a Network Load Balancer, so other VPCs can connect through interface endpoints without using the public internet.**

## Memory trick

**Service serves, endpoint enters.**

* **Endpoint service** = the service provider shares
* **Interface endpoint** = the consumer enters through it

Another memory line:

**PrivateLink = private path to a service, not full network-to-network access.**
