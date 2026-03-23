# Customer Gateway (CGW)

## Simple definition

A Customer Gateway (CGW) is an AWS resource that represents your side of a Site-to-Site VPN connection.

It tells AWS about your on-premises VPN device, such as its public IP address and routing details.

---

## Core idea in plain English

Think of a Customer Gateway as the AWS record of your company’s router or firewall.

Your real router or firewall stays in your office, data center, or branch location. In AWS, you create a Customer Gateway resource so AWS knows how to connect to that device.

So the big exam idea is

 Customer gateway device = the actual physical or software VPN device on your side
 Customer Gateway (CGW) = the AWS resource that represents that device

This difference is very important in the exam.

---

## Main use cases

A Customer Gateway is mainly used when a company wants to connect its on-premises network to AWS.

Common use cases

 Connect a company office to a VPC
 Connect a data center to AWS securely over the internet
 Build a hybrid cloud setup
 Allow servers in AWS to communicate with on-premises systems
 Extend private networking between AWS and an existing corporate network

---

## Key features

 Used with AWS Site-to-Site VPN
 Represents your side of the VPN connection
 Works with a customer gateway device such as a router or firewall
 Supports static routing or dynamic routing (BGP)
 Requires a public IP address for your VPN device
 Used together with an AWS-side gateway such as a Virtual Private Gateway (VGW) or Transit Gateway (TGW)
 Helps create a secure IPsec VPN tunnel between your network and AWS

---

## How it works

Here is the simple flow

1. You have a routerfirewall in your office or data center.
2. In AWS, you create a Customer Gateway resource that points to that device.
3. On the AWS side, you also create a Virtual Private Gateway or use a Transit Gateway.
4. Then you create a Site-to-Site VPN connection between AWS and your network.
5. AWS gives configuration details for the VPN tunnels.
6. Your network administrator configures the real routerfirewall.
7. Traffic can then move securely between your on-premises network and your VPC.

In simple words

Customer Gateway = your side
Virtual Private Gateway  Transit Gateway = AWS side
Site-to-Site VPN = the secure tunnel between them

---

## Why it is important for the exam

This topic matters because AWS exam questions often test whether you understand hybrid connectivity.

You should know that Customer Gateway is part of Site-to-Site VPN, not Direct Connect by itself.

You should also know that AWS uses different components on each side

 Customer Gateway on the customer side
 Virtual Private Gateway or Transit Gateway on the AWS side

A very common exam trap is confusing the Customer Gateway resource with the actual customer gateway device.

---

## Related AWS services and differences

### Customer Gateway vs Customer Gateway Device

 Customer Gateway = AWS resource
 Customer Gateway Device = your real router, firewall, or software VPN appliance

This is one of the most important distinctions.

### Customer Gateway vs Virtual Private Gateway (VGW)

 Customer Gateway = your side of the VPN
 Virtual Private Gateway = AWS side of the VPN attached to one VPC

### Customer Gateway vs Transit Gateway (TGW)

 Customer Gateway = your side information in AWS
 Transit Gateway = AWS network hub that can connect multiple VPCs and on-premises networks

### Customer Gateway vs Site-to-Site VPN

 Customer Gateway = one component
 Site-to-Site VPN = the full secure connection using tunnels

### Customer Gateway vs AWS Direct Connect

 Customer Gateway is used with VPN connectivity
 Direct Connect is a dedicated private network connection, not internet-based VPN
 Sometimes companies use Direct Connect + VPN together for extra security or backup

### Customer Gateway vs Client VPN

 Customer Gateway  Site-to-Site VPN = connects networks to AWS
 Client VPN = connects individual usersdevices to AWS

---

## Common exam traps

 Thinking Customer Gateway is the VPN tunnel itself
 Thinking Customer Gateway is the AWS side of the connection
 Confusing Customer Gateway with Customer Gateway Device
 Confusing Customer Gateway with Virtual Private Gateway
 Thinking Customer Gateway is used for individual user remote access like Client VPN
 Thinking Direct Connect and Customer Gateway are the same thing

Exam shortcut

 Customer side = Customer Gateway
 AWS side = VGW or TGW
 Connection = Site-to-Site VPN

---

## Easy real-world example

A company has its main office in Rome and its application servers in AWS.

The company wants employees in the office to access private resources in a VPC.

The company already has a firewallrouter in the office.

What happens

 That office routerfirewall is the customer gateway device
 In AWS, the company creates a Customer Gateway resource for it
 AWS uses a Virtual Private Gateway or Transit Gateway on its side
 A Site-to-Site VPN is created between the office and AWS

Now the office network and AWS can communicate securely.

---

## If I were an examiner ...

If I were an examiner, I would ask things like

 Which AWS component represents the customer side of a Site-to-Site VPN connection
 What is the difference between a Customer Gateway and a Virtual Private Gateway
 Is a Customer Gateway the actual physical device or an AWS resource
 Which service is used to securely connect an on-premises network to a VPC over the internet
 Which component is on the AWS side, and which is on the customer side
 What is the difference between Site-to-Site VPN and Client VPN
 When would you use Transit Gateway instead of Virtual Private Gateway

An examiner may try to trick you by mixing these terms together.

---

## Final summary

A Customer Gateway is an AWS resource that represents your on-premises VPN device in a Site-to-Site VPN setup.

It is not the tunnel itself, and it is not the AWS-side gateway.

For the exam, remember this very clearly

 Customer Gateway = customer side in AWS
 Customer Gateway Device = real routerfirewall on-premises
 Virtual Private Gateway  Transit Gateway = AWS side
 Site-to-Site VPN = secure connection between both sides

---

## Short exam answer

A Customer Gateway is an AWS resource that represents the customer’s on-premises VPN device and is used with AWS Site-to-Site VPN to connect an on-premises network to AWS.

---

## Memory trick

Think

C = Customer side
V = VendorAWS side (VGW)

Or even simpler

Customer Gateway = my company’s side
Virtual Private Gateway = AWS side

Another memory trick

CGW tells AWS about your router.

It does not replace your router. It only represents it inside AWS.
