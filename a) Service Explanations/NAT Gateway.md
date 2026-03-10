# NAT Gateway

## Simple definition

A NAT Gateway is an AWS managed network service that lets resources in a private subnet send traffic out to the internet or other networks, while stopping the internet from starting a connection in to those resources.

---

## Core idea in plain English

Think of a NAT Gateway as a one-way door for outbound traffic.

Your private EC2 instances can go out to download updates, call APIs, or reach external services. But outside systems cannot directly open a new connection back to those private instances.

That is why NAT Gateway is commonly used when servers must stay private but still need outbound access.

---

## Main use cases

 Private EC2 instances downloading software updates
 App servers in private subnets calling external APIs
 Private workloads pulling packages from the internet
 Sending outbound traffic while keeping instances without public IPs
 Reaching the internet from private subnets in a safer and simpler way than using a NAT instance

---

## Key features

 Managed by AWS
 Used for outbound traffic from private subnets
 Prevents unsolicited inbound internet connections
 Common setup uses a public NAT Gateway
 A public NAT Gateway uses an Elastic IP
 Scales better and needs less administration than a NAT instance
 Commonly used with route tables to send private subnet internet traffic through the NAT Gateway

---

## How it works

### Classic exam setup

1. You create a NAT Gateway in a public subnet.
2. That public subnet has a route to an Internet Gateway.
3. Your private subnet route table sends internet-bound traffic (`0.0.0.00`) to the NAT Gateway.
4. Private instances send outbound traffic through the NAT Gateway.
5. Responses come back through the NAT Gateway.
6. Outside systems still cannot start a connection directly to those private instances.

### Easy picture in words

 Public subnet contains the NAT Gateway
 Private subnet contains your EC2 app servers
 Internet Gateway gives internet access to the NAT Gateway
 Route table tells private subnet traffic to go to the NAT Gateway

---

## Why it is important for the exam

NAT Gateway is one of the most common AWS networking exam topics.

AWS exam questions often test whether you understand this rule

 Private subnet resources need outbound internet access but should not be publicly reachable - use a NAT Gateway.

This is a very common decision point in Cloud Practitioner questions.

---

## Related AWS services and differences

### NAT Gateway vs Internet Gateway

 Internet Gateway allows resources with public IPs in a public subnet to communicate with the internet.
 NAT Gateway is for resources in a private subnet that need outbound-only style internet access.

### NAT Gateway vs NAT Instance

 NAT Gateway is managed by AWS
 NAT Instance is an EC2 instance you manage yourself
 NAT Gateway is usually the better exam answer because it is simpler, more scalable, and requires less maintenance

### NAT Gateway vs Egress-Only Internet Gateway

 NAT Gateway is mainly the answer for IPv4 outbound internet access from private subnets
 Egress-only Internet Gateway is for IPv6 outbound-only internet access

### NAT Gateway vs VPC Endpoint

 NAT Gateway is used for general outbound access to the internet or external networks
 VPC Endpoint lets you privately connect to some AWS services without going through the public internet
 If the question is about private access to S3 or DynamoDB, a VPC endpoint may be the better answer than NAT Gateway

### Public NAT Gateway vs Private NAT Gateway

 Public NAT Gateway used for internet access and has an Elastic IP
 Private NAT Gateway used for private connectivity to other VPCs or on-premises networks, not for internet access

---

## Common exam traps

### Trap 1 Thinking NAT Gateway allows inbound connections

Wrong.

A NAT Gateway helps private resources start outbound connections. It does not make them publicly reachable.

### Trap 2 Putting the NAT Gateway in a private subnet

Wrong for the classic internet access design.

For the usual exam setup, the NAT Gateway is placed in a public subnet.

### Trap 3 Forgetting the Internet Gateway

A NAT Gateway alone is not enough for internet access.

For the normal public NAT design, the VPC also needs an Internet Gateway.

### Trap 4 Confusing NAT Gateway with Bastion Host

 Bastion Host is for administrative access like SSHRDP into private instances
 NAT Gateway is for outbound internet access from private instances

### Trap 5 Using NAT Gateway when the question is really about private AWS service access

If the goal is private access to AWS services like S3, the exam may want VPC Endpoint, not NAT Gateway.

### Trap 6 Missing the route table part

Even if the NAT Gateway exists, private subnet traffic must be routed to it.

---

## Easy real-world example

A company has application servers in a private subnet.

The servers must download operating system updates and call a third-party payment API, but the company does not want those servers exposed directly to the internet.

Solution

 Put the EC2 instances in a private subnet
 Create a NAT Gateway in a public subnet
 Add a route in the private subnet route table to send internet traffic to the NAT Gateway

Now the servers can go out to the internet, but no one on the internet can directly start a connection to them.

---

## Final summary

A NAT Gateway is an AWS managed service used mainly to give private subnet resources outbound internet access.

It is the standard answer when workloads must stay private but still need to reach the internet.

Remember the classic pattern

 NAT Gateway in a public subnet
 Private subnet route table points to the NAT Gateway
 Internet Gateway attached to the VPC

This is one of the most important basic VPC ideas for the Cloud Practitioner exam.

---

## Short exam answer

NAT Gateway lets instances in a private subnet access the internet outbound, without allowing unsolicited inbound internet connections.

---

## Memory trick

NAT = Not Available To the internet from outside

Or even simpler

Private servers go OUT through NAT. The internet cannot come IN through NAT.
