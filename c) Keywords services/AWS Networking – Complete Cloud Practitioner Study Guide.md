# AWS Networking – Complete Cloud Practitioner Study Guide

 How to use this file Read top-to-bottom once to build mental models. Then use the
 Exam Trap and Quick-Mapping sections before your test. Every section answers three questions
 What is it What is fixed vs variable When do you pick it

---

## TABLE OF CONTENTS

1. [Mental Model The Six Connectivity Situations](#1-mental-model-the-six-connectivity-situations)
2. [VPC to the Internet](#2-vpc-to-the-internet)
   - Internet Gateway (IGW)
   - NAT Gateway
   - Egress-only Internet Gateway
3. [Private Access from a VPC to AWS Services](#3-private-access-from-a-vpc-to-aws-services)
   - VPC Endpoints (Gateway type)
   - AWS PrivateLink  Interface VPC Endpoints
4. [VPC to VPC Inside AWS](#4-vpc-to-vpc-inside-aws)
   - VPC Peering
   - AWS Transit Gateway
5. [On-Premises Network to AWS](#5-on-premises-network-to-aws)
   - AWS Site-to-Site VPN
   - AWS Direct Connect
   - Direct Connect + VPN (Combined)
6. [End Users to AWS](#6-end-users-to-aws)
   - AWS Client VPN
7. [Supporting Concepts (Not the Main Answer but Always in the Design)](#7-supporting-concepts-not-the-main-answer-but-always-in-the-design)
8. [What the Exam Images Covered vs What Was Missing](#8-what-the-exam-images-covered-vs-what-was-missing)
9. [The Fastest Exam Mapping Cheat Sheet](#9-the-fastest-exam-mapping-cheat-sheet)
10. [Every Exam Trap Catalogued](#10-every-exam-trap-catalogued)
11. [Memory Anchors and Mnemonics](#11-memory-anchors-and-mnemonics)

---

## 1. MENTAL MODEL THE SIX CONNECTIVITY SITUATIONS

Before memorising individual services, burn this map into your head. Every AWS networking
question falls into exactly one of six buckets

```
SITUATION                         SERVICE(S) TO USE
─────────────────────────────────────────────────────────────────────
VPC ──► Public Internet           Internet Gateway (IGW)
VPC private subnet ──► Internet   NAT Gateway (outbound only)
VPC ──► S3  DynamoDB privately   Gateway VPC Endpoint
VPC ──► other AWS services priv.  Interface VPC Endpoint  PrivateLink
VPC ──► another VPC               VPC Peering (2 VPCs) or Transit Gateway (many)
On-prem ──► AWS (encryptedcheap) Site-to-Site VPN
On-prem ──► AWS (fastdedicated)  AWS Direct Connect
Laptopemployee ──► AWS           AWS Client VPN
```

---

## 2. VPC TO THE INTERNET

### 2A. Internet Gateway (IGW)

#### What it is
A horizontally scaled, redundant, highly available VPC component that allows communication
between resources in your VPC and the public internet. It performs NAT for instances that
have public IPv4 addresses.

#### What is FIXED (never changes, exam-safe facts)
- One IGW attaches to exactly one VPC at a time.
- An IGW is not a physical device — it is a logical, managed, AWS-run component.
- It is horizontally scaled — you never worry about throughput limits or bandwidth on the IGW itself.
- It is free — there is no per-hour charge for the IGW itself.
- Making a subnet public requires both an IGW attachment AND a route in the subnet's
  route table pointing `0.0.0.00` to the IGW.
- The resource inside the VPC must also have a public IP (Elastic IP or auto-assigned).

#### What is VARIABLE (changes per deployment)
- Which VPC it is attached to.
- Whether you use it for IPv4, IPv6, or both.
- Which subnets have routes pointing to it.

#### Real-world examples
- An EC2 web server in `us-east-1` needs to serve HTTPHTTPS to users on the internet → attach
  an IGW to the VPC, put the EC2 in a public subnet (route table has `0.0.0.00 → igw-xxxxx`),
  assign the EC2 a public IP.
- A public-facing Application Load Balancer needs to receive traffic from anywhere → the ALB
  must sit in a public subnet behind an IGW.
- An RDS database should never use an IGW — databases stay in private subnets.

#### Exam traps
- Trap 1 – Subnet confusion Attaching an IGW to a VPC does NOT automatically make any
  subnet public. You still need a route in the route table pointing `0.0.0.00` to the IGW.
  A subnet becomes public by route table + IGW combination, not by a checkbox.
- Trap 2 – No public IP, no internet Even with an IGW and correct routes, an EC2 instance
  in a public subnet with NO public IP cannot be reached from the internet.
- Trap 3 – IGW is not a firewall The IGW itself does not filter traffic. Security Groups
  and NACLs do. The question which service blocks inbound traffic is never answered with IGW.
- Trap 4 – One IGW per VPC You cannot attach two IGWs to one VPC. If the question implies
  dual-IGW redundancy, that is a wrong answer.

---

### 2B. NAT Gateway

#### What it is
A Network Address Translation (NAT) device that lets instances in a private subnet initiate
outbound connections to the internet (or other AWS services) while preventing the internet from
initiating inbound connections to those instances.

#### What is FIXED (exam-safe facts)
- A NAT Gateway lives in a public subnet — it must have a path to the internet (via IGW).
- It has an Elastic IP address attached.
- Traffic flow is always private subnet instance → NAT Gateway (in public subnet) → IGW → internet.
- It is a managed service — AWS handles availability and scaling. You do not patch it.
- NAT Gateway is not free — you pay per hour and per GB of data processed.
- A NAT Gateway serves one AZ — for high availability across AZs, deploy one per AZ.
- Inbound connections from the internet to your private instances are blocked by design.

#### What is VARIABLE
- Which AZ it is deployed in.
- How much traffic passes through it (determines cost).
- Whether you use it for private IPv4 (standard) or for public access (public NAT Gateway type).

#### Real-world examples
- An EC2 in a private subnet needs to download OS patches from the internet → NAT Gateway
  in the public subnet, route table for private subnet points `0.0.0.00` to the NAT Gateway.
- A Lambda function in a VPC needs to call an external third-party API (e.g., Stripe) → place
  the Lambda in a private subnet, route outbound through NAT Gateway.
- An RDS database must NOT have outbound internet access at all (compliance requirement) →
  do NOT put a NAT Gateway route in its subnet.

#### Architecture pattern (memorise the three-layer flow)
```
[Private EC2] → route table → [NAT Gateway in public subnet] → route table → [IGW] → Internet
```

#### Exam traps
- Trap 1 – IGW is still required NAT Gateway does NOT replace the IGW. The NAT Gateway
  itself needs a route to the IGW to reach the internet. Both must exist.
- Trap 2 – NAT Gateway vs NAT Instance In modern AWS the answer is almost always NAT Gateway
  (managed). NAT Instance is a legacy EC2-based option. Exam questions about high availability
  and no maintenance overhead → NAT Gateway wins.
- Trap 3 – Direction matters NAT Gateway allows OUTBOUND only from private instances.
  If the question asks about inbound connectivity TO private instances, NAT Gateway is wrong.
- Trap 4 – Cross-AZ cost A NAT Gateway in AZ-A serving instances in AZ-B incurs cross-AZ
  data transfer charges. Best practice is one NAT Gateway per AZ.
- Trap 5 – Not for IPv6 NAT Gateway handles IPv4 only. For IPv6, use the Egress-only
  Internet Gateway (below).

---

### 2C. Egress-only Internet Gateway

#### What it is
An IGW variant designed exclusively for IPv6 traffic that allows outbound communication
from instances in your VPC to the internet but prevents the internet from initiating inbound
IPv6 connections.

#### What is FIXED
- Works only with IPv6.
- Outbound only — mirrors NAT Gateway behaviour but for IPv6.
- Managed and horizontally scaled, like the regular IGW.

#### What is VARIABLE
- Which VPC it is associated with.
- Which subnets route through it.

#### Real-world example
- Your VPC is dual-stack (IPv4 + IPv6). EC2 instances have IPv6 addresses and need to reach
  the internet outbound but should not be reachable inbound on IPv6 → use Egress-only IGW.

#### Exam trap
- Trap 1 – Not for IPv4 The name says egress-only but people confuse it with NAT Gateway.
  NAT Gateway = IPv4 private outbound. Egress-only IGW = IPv6 outbound. They are not
  interchangeable.

---

## 3. PRIVATE ACCESS FROM A VPC TO AWS SERVICES

 The core idea you want to call AWS APIs (S3, DynamoDB, SQS, etc.) from inside your VPC
 without sending traffic through the public internet. VPC Endpoints solve this.

### 3A. Gateway VPC Endpoints

#### What it is
A special VPC endpoint type used only for Amazon S3 and Amazon DynamoDB. A gateway endpoint
is a route-table target — you add it to your route table and traffic destined for S3 or DynamoDB
is routed privately through the AWS network instead of over the internet.

#### What is FIXED
- Supports only S3 and DynamoDB — these are the only two services that use Gateway Endpoints.
- Works by adding an entry to the route table — no ENI (Elastic Network Interface) is created.
- It is free — no per-hour or per-GB charge for Gateway Endpoints.
- Traffic does not leave the AWS network.
- No Elastic IP needed, no NAT Gateway needed for S3DynamoDB access.

#### What is VARIABLE
- Which VPC and which subnets use it.
- Which S3 bucket(s) or DynamoDB table(s) are accessible through it (controlled via endpoint policy).

#### Real-world examples
- An EC2 in a private subnet (no NAT Gateway) needs to readwrite to S3 → create a Gateway
  Endpoint for S3, add it to the private subnet's route table. Done, no internet path needed.
- A compliance requirement says S3 traffic must never traverse the public internet → Gateway
  Endpoint is the answer.
- An EMR cluster in a private VPC must access DynamoDB → Gateway Endpoint for DynamoDB.

#### Exam traps
- Trap 1 – Only S3 and DynamoDB Every other AWS service uses Interface Endpoints, not
  Gateway Endpoints. If the question says privately access SQS → Interface Endpoint, not
  Gateway Endpoint.
- Trap 2 – Free vs paid Gateway Endpoints are free. Interface Endpoints cost money
  (per hour, per GB). Exam may ask for the cost-effective option → Gateway Endpoint (where
  applicable).
- Trap 3 – No ENI Gateway Endpoints do not appear in your VPC as a network interface.
  They are route-table entries only. Do not confuse with Interface Endpoints (which DO create ENIs).

---

### 3B. Interface VPC Endpoints (AWS PrivateLink)

#### What it is
A network interface (ENI) that is placed in your subnet and gives your VPC a private IP address
that maps to a supported AWS service endpoint. You connect to the service via this private IP,
so all traffic stays within the AWS network. PrivateLink is the underlying technology.

#### What is FIXED
- Creates an ENI in your subnet with a private IP address.
- Works with a wide range of AWS services (EC2 API, SNS, SQS, Kinesis, SSM, Secrets Manager,
  CloudWatch, and hundreds more).
- Also works for services from other AWS accounts or AWS Marketplace services.
- You are charged per hour per AZ and per GB of data processed.
- No internet gateway, NAT device, VPN, or Direct Connect needed for the service communication.
- Access is controlled via VPC endpoint policies and standard security groups on the ENI.

#### What is VARIABLE
- Which service(s) the endpoint connects to.
- Which subnets and AZs the ENI is placed in.
- Whether DNS hostnames are configured to resolve to the private IP.

#### Real-world examples
- Your EC2 in a locked-down VPC (no internet) needs to call the SSM API to use Systems Manager
  → create an Interface Endpoint for `com.amazonaws.us-east-1.ssm`.
- SaaS vendor hosts their service in their own AWS account. You want private connectivity to it
  without peering VPCs → vendor exposes it as a PrivateLink service; you create an Interface
  Endpoint to connect to it.
- Lambda in a VPC needs to write to SQS without internet → Interface Endpoint for SQS.

#### Exam traps
- Trap 1 – PrivateLink ≠ VPC Peering PrivateLink provides one-way private access to a
  service. VPC Peering provides full bidirectional network connectivity between two VPCs.
  These are not the same.
- Trap 2 – It is not free Unlike Gateway Endpoints, Interface Endpoints charge per hour.
- Trap 3 – DNS resolution Interface Endpoints have their own DNS names. Enable private
  DNS must be turned on if you want the existing AWS service hostname (e.g.,
  `s3.amazonaws.com`) to resolve to your private endpoint IP automatically.

---

## 4. VPC TO VPC INSIDE AWS

### 4A. VPC Peering

#### What it is
A networking connection between two VPCs that enables traffic to be routed between them
using private IP addresses. Works like those VPCs are in the same network.

#### What is FIXED
- Connects exactly two VPCs per peering connection.
- Works between VPCs in the same account, different accounts, or different regions.
- Traffic is private and does not traverse the public internet.
- Not transitive — this is the biggest exam trap. If VPC-A peers with VPC-B and VPC-B
  peers with VPC-C, VPC-A cannot reach VPC-C through VPC-B.
- IP address ranges (CIDR blocks) of the two VPCs must not overlap.
- Relatively low cost — you pay for data transfer, not an hourly service fee.

#### What is VARIABLE
- Which two VPCs are peered.
- Route table entries in both VPCs (must be added manually — peering alone does not route traffic).
- Whether the peering is intra-region or inter-region.

#### Real-world examples
- Two teams each have their own VPC. Team A's app must talk to Team B's database → VPC peering.
- Production VPC must access a shared services VPC (e.g., for Active Directory) → VPC peering
  between prod and shared-services.
- Company has 3 VPCs (A, B, C) and all three need full connectivity → you need 3 peering
  connections (A-B, B-C, A-C). NOT 2.

#### The Non-Transitivity Trap (most common exam scenario)
```
     VPC-A ←—peered—→ VPC-B ←—peered—→ VPC-C

     VPC-A CANNOT reach VPC-C via VPC-B. Traffic does not pass through.
     If you need A ↔ B ↔ C all talking use Transit Gateway OR create A-C peering.
```

#### Exam traps
- Trap 1 – Not transitive Repeated above because it is #1 most-tested peering fact.
- Trap 2 – Overlapping CIDRs If both VPCs use `10.0.0.016`, peering is impossible.
  You must plan non-overlapping CIDRs.
- Trap 3 – Route tables are manual Accepting a peering request does not automatically
  route traffic. You must update route tables in both VPCs.
- Trap 4 – Scaling Peering 10 VPCs fully-connected requires 45 peering connections
  (n(n-1)2 formula). This is the signal that Transit Gateway is the better answer.

---

### 4B. AWS Transit Gateway

#### What it is
A network transit hub that you can use to interconnect multiple VPCs and on-premises networks
through a single, centrally managed gateway. Think of it as a cloud-based router and network hub.

#### What is FIXED
- Operates as a hub-and-spoke model — all VPCs attach to the Transit Gateway, which routes
  between them.
- Transitive routing IS supported — unlike VPC Peering. VPC-A can reach VPC-C through
  the Transit Gateway.
- Can connect VPCs across multiple accounts (via Resource Access Manager).
- Can attach to VPNs and Direct Connect gateways — making it a unified hub for hybrid networks.
- Is a regional service but supports inter-region peering (TGW to TGW across regions).
- You are charged per attachment per hour and per GB of data processed.

#### What is VARIABLE
- Number of VPCs attached.
- Routing tables within the TGW (you can create segmented routing for multi-tenant isolation).
- Whether Direct Connect andor VPN are attached.
- Whether inter-region TGW peering is configured.

#### Real-world examples
- Company has 50 VPCs across multiple accounts. All need to talk to a shared DNS VPC and
  an on-premises data centre → Transit Gateway connects all 50 VPCs + Direct Connect attachment.
- Multi-account AWS Organizations setup where spoke accounts (dev, staging, prod) need shared
  services (centralised logging, DNS) → Transit Gateway hub-and-spoke.
- You need transitive routing App VPC → Data VPC → Analytics VPC in a chain → Transit Gateway.

#### VPC Peering vs Transit Gateway Decision

 Factor                         VPC Peering              Transit Gateway         
---------------------------------------------------------------------------------
 Number of VPCs                 2–5 (manageable)         5+ (or growing)         
 Transitive routing needed      No (use TGW instead)     Yes                     
 On-premises integration        No                       Yes (VPNDX attachment) 
 Cost model                     Data transfer only       Hourly per attachment + data 
 Centralized management         No (mesh of connections) Yes (single hub)        

#### Exam traps
- Trap 1 – Not cheap Transit Gateway has an hourly cost per attachment. For 2 VPCs with
  simple requirements, VPC Peering is cheaper.
- Trap 2 – Regional service A Transit Gateway is regional. Cross-region connectivity
  requires TGW-to-TGW peering (a separate connection).
- Trap 3 – TGW ≠ automatically routes You must create route tables within TGW and
  associate VPC attachments. It is not plug-and-play.

---

## 5. ON-PREMISES NETWORK TO AWS

### 5A. AWS Site-to-Site VPN

#### What it is
An encrypted IPSec VPN tunnel over the public internet that connects your on-premises
network (or data centre) to your AWS VPC.

#### What is FIXED
- Traffic travels over the public internet (but is encrypted via IPSec).
- Each VPN connection includes two tunnels for high availability.
- Requires a Customer Gateway (a physical or software appliance on your side) and a
  Virtual Private Gateway (VGW) or Transit Gateway on the AWS side.
- Setup is relatively fast — can be done in hours to days.
- Bandwidth is subject to internet conditions — not guaranteed.
- Lower cost than Direct Connect.

#### What is VARIABLE
- The internet service provider and path the traffic takes (variable latencythroughput).
- Which on-premises network range is advertised.
- Whether routing is static or dynamic (BGP).
- Whether attached to VGW or Transit Gateway.

#### Real-world examples
- A small business has an on-premises server and needs secure access to AWS resources overnight
  for backups → Site-to-Site VPN, quick to set up, cheap.
- Disaster recovery site needs connectivity to AWS but only as a failover path → Site-to-Site
  VPN as backup to Direct Connect.
- Devtest environment needs connection to corporate network resources in AWS → Site-to-Site VPN.

#### Exam traps
- Trap 1 – Encrypted does not mean dedicated VPN is encrypted but still travels the
  public internet. If the question asks for a dedicated private connection, VPN is wrong —
  Direct Connect is the answer.
- Trap 2 – Two tunnels are automatic Every Site-to-Site VPN has two IPSec tunnels for
  redundancy. The question how do you make the VPN highly available is answered two tunnels
  are already provided.
- Trap 3 – Customer Gateway is your device The Customer Gateway represents your on-premises
  routerfirewall. It is not an AWS service — it is a configuration object in AWS representing
  your equipment.
- Trap 4 – Virtual Private Gateway vs Transit Gateway If the VPN connects to only one VPC,
  attach it to a Virtual Private Gateway. If it connects to many VPCs, attach it to a Transit
  Gateway — this is the scalable pattern.

---

### 5B. AWS Direct Connect

#### What it is
A dedicated, private physical network connection from your on-premises location (office,
data centre, or colocation facility) directly to AWS. Traffic does NOT travel over the public
internet.

#### What is FIXED
- Provides a physically dedicated network connection — your data does not mix with other
  internet traffic.
- Offers consistent, low-latency performance because the path is fixed and private.
- Available in 1 Gbps and 10 Gbps standard speeds (hosted connections allow sub-1 Gbps).
- Setup takes weeks to months — physical fibre must be provisioned.
- Higher cost than VPN — you pay for the port, the cross-connect, and data transfer.
- Traffic is private but NOT encrypted by default — the physical line is yours, but data
  is not encrypted unless you add encryption on top.
- Provides access to both public AWS services (like S3) and private VPC resources.

#### What is VARIABLE
- Connection speed (1 Gbps or 10 Gbps for dedicated; smaller for hosted).
- Which AWS Direct Connect location (POP) you connect to.
- Whether you use a dedicated connection or a hosted connection through a partner.

#### Real-world examples
- A financial services firm processes terabytes of market data daily and cannot afford internet
  latency or variability → Direct Connect for consistent performance.
- A media company transfers 50 TB of video files to S3 every week → Direct Connect is cheaper
  than internet data transfer at scale.
- Healthcare company has regulatory requirements that PHI data must not traverse the public
  internet → Direct Connect.

#### Exam traps
- Trap 1 – Not encrypted by default Direct Connect is private (physical) but data is NOT
  encrypted unless you layer a VPN on top or use MACsec. A question asking for a private and
  encrypted connection → Direct Connect + VPN combination.
- Trap 2 – Not instant Direct Connect takes weeks to provision. If the question says
  immediately or within days, VPN is the answer.
- Trap 3 – Not redundant by default One Direct Connect connection is a single point of
  failure. For resilience, you need a second connection or a backup VPN.
- Trap 4 – Still need VGW or TGW Direct Connect does not attach directly to a VPC. It
  connects to a Direct Connect Gateway or Virtual Interface, which then connects to a VGW or TGW.

---

### 5C. Direct Connect + VPN (Combined Architecture)

#### What it is
Using Direct Connect as the primary path and Site-to-Site VPN as a backup (failover) path,
OR using VPN on top of Direct Connect for end-to-end encryption.

#### Two distinct use cases
1. Hybrid resilience Direct Connect = primary (fast, private). VPN = failover (if DX fails).
2. Encrypted Direct Connect VPN tunnel over the Direct Connect path — adds IPSec
   encryption to what is otherwise an unencrypted private line.

#### When the exam asks for this
- Private, encrypted, and dedicated → Direct Connect + VPN.
- Reliable hybrid connectivity with automatic failover → Direct Connect primary + VPN backup.

#### Exam trap
- Trap 1 – Understand which use case Combine DX and VPN means different things.
  Adding a VPN for encryption is different from adding a VPN as a backup path. The exam will
  make the use case clear — read carefully.

---

## 6. END USERS TO AWS

### 6A. AWS Client VPN

#### What it is
A managed, client-based VPN service that enables individual users or devices (laptops,
phones, remote employees) to securely access AWS resources and on-premises resources using
an OpenVPN-based client.

#### What is FIXED
- Designed for individual usersdevices, not network-to-network connectivity.
- Uses the OpenVPN protocol.
- Managed service — AWS handles availability of the VPN endpoint.
- Works from anywhere — a user connects from their home, coffee shop, airport, etc.
- Provides access to both VPC resources and on-premises resources (if you have a
  VPN or Direct Connect in place too).
- Authenticates users via Active Directory, certificate-based auth, or SAML.

#### What is VARIABLE
- Number of concurrent users.
- Authentication method used.
- Split tunneling on or off (whether all traffic or only AWS-destined traffic goes through the VPN).

#### Real-world examples
- Remote developer needs to SSH into EC2 instances in a private VPC while working from home
  → AWS Client VPN on their laptop.
- Finance team's laptops need access to an internal payroll application running on EC2 in a
  private subnet → Client VPN for each finance employee.
- COVID-19 scenario entire company suddenly remote, need secure access to AWS resources
  → roll out Client VPN endpoint.

#### The critical distinction

 Service           Connects...                     Use when...                     
-----------------------------------------------------------------------------------
 Client VPN        Individual users  devices      Remote employees needing access 
 Site-to-Site VPN  Two NETWORKS (on-prem to VPC)   OfficeDC connecting to AWS     

#### Exam traps
- Trap 1 – Client VPN vs Site-to-Site VPN The word user or employee or remote
  device → Client VPN. The word network, office, data centre, on-premises →
  Site-to-Site VPN. These are completely different services.
- Trap 2 – Not free Client VPN has an hourly charge per endpoint and per active connection.

---

## 7. SUPPORTING CONCEPTS (NOT THE MAIN ANSWER BUT ALWAYS IN THE DESIGN)

These appear in exam questions as distractors or as parts of a correct solution, but they
are never the main answer to a connectivity question.

### 7A. Subnets (Public vs Private)
- Public subnet has a route to an IGW. Resources here CAN have public IPs.
- Private subnet has NO route to an IGW. Resources here are not directly internet-accessible.
- The exam never asks which service is a subnet — but subnets appear in every multi-VPC
  architecture question. Know where to place each resource (databases → private, web servers → public or behind ALB).

### 7B. Route Tables
- Every subnet is associated with exactly one route table.
- Route tables determine where traffic is sent.
- Common exam pattern After creating a NAT Gateway  VPC Endpoint  Peering connection,
  what do you still need to do → Update the route table.
- Route tables are infrastructure glue — they are never the main connectivity service.

### 7C. Security Groups
- Stateful virtual firewalls at the instanceENI level.
- Default deny all inbound, allow all outbound.
- You add allow rules only. There are no explicit deny rules in Security Groups.
- Changes take effect immediately.

### 7D. Network ACLs (NACLs)
- Stateless firewalls at the subnet level.
- Support both allow and deny rules.
- Rules are evaluated in order (lowest number first).
- Because stateless if you allow inbound traffic on port 80, you must also explicitly allow
  the return traffic (ephemeral ports 1024–65535 outbound).
- Default NACL allows all traffic. Custom NACLs deny all traffic by default.

### 7E. Customer Gateway and Virtual Private Gateway
- Customer Gateway an AWS resource that represents your on-premises device in a VPN setup.
  It is NOT a physical device — it is a configuration object.
- Virtual Private Gateway (VGW) the AWS-side VPN concentrator attached to a VPC.
  It is a required component for Site-to-Site VPN, but the answer to how do I connect
  my office to AWS is Site-to-Site VPN — not Virtual Private Gateway.

### 7F. Elastic IP (EIP)
- A static public IPv4 address that you can allocate and attach to resources.
- Required for resources in a public subnet that need a permanent public IP.
- A NAT Gateway always requires an EIP.
- Free if in use; charged if allocated but not attached (to discourage waste).

---

## 8. WHAT THE EXAM IMAGES COVERED VS WHAT WAS MISSING

### Covered in the images (complete for CCP exam)
- Internet Gateway
- NAT Gateway
- Egress-only Internet Gateway
- VPC Endpoints (Gateway type – S3 and DynamoDB)
- AWS PrivateLink  Interface VPC Endpoints
- VPC Peering
- AWS Transit Gateway
- AWS Site-to-Site VPN
- AWS Direct Connect
- Direct Connect + VPN
- AWS Client VPN

### Supplemental topics not in the images (still CCP-relevant)
- Security Groups vs NACLs — both can appear in questions about how to restrict traffic
- Public vs Private Subnets — fundamental to every architecture scenario
- Route Tables — always the missing piece in a why doesn't my connection work question
- VPC Flow Logs — used for monitoring and troubleshooting VPC network traffic
- Elastic IP — attached to NAT Gateway and public-facing EC2 instances
- AWS Network Firewall — advanced VPC traffic inspection (rare at CCP level)

---

## 9. THE FASTEST EXAM MAPPING CHEAT SHEET

Use this for last-minute review. Read the keyword → immediately think of the service.

### By keyword in the question

 Question contains this phrase...                         Think...                        
------------------------------------------------------------------------------------------
 public internet access for a VPC  public subnet        Internet Gateway            
 private subnet needs outbound internet                  NAT Gateway                 
 instances need internet, NO inbound connections         NAT Gateway                 
 IPv6 outbound only                                      Egress-only Internet Gateway
 private access to S3 without internet                   Gateway VPC Endpoint        
 private access to DynamoDB without internet             Gateway VPC Endpoint        
 private access to AWS services (not S3DynamoDB)        Interface VPC Endpoint  PrivateLink 
 connect two VPCs privately                              VPC Peering                 
 peering is not transitive  can't reach VPC-C via VPC-B  Transit Gateway           
 connect many VPCs centrally  hub-and-spoke             Transit Gateway             
 connect on-premises network to AWS  encrypted tunnel   Site-to-Site VPN            
 dedicated physical private connection  low latency     Direct Connect              
 private AND encrypted dedicated connection              Direct Connect + VPN        
 remote employees  individual users  work from home    Client VPN                  
 fast setup, connecting on-premises, weeks too long      Site-to-Site VPN            
 consistent performance, large data transfer, months OK  Direct Connect              

### By elimination (when unsure)
1. Is traffic going to the public internet → IGW or NAT Gateway
2. Is traffic going to another AWS VPC → Peering or Transit Gateway
3. Is traffic going to AWS services (S3, SQS, etc.) → VPC Endpoint (Gateway or Interface)
4. Is traffic coming from on-premises network → Site-to-Site VPN or Direct Connect
5. Is it an individual user connecting → Client VPN

---

## 10. EVERY EXAM TRAP CATALOGUED

This is a master list of all traps you can face on the Cloud Practitioner exam for networking.

### Trap Category 1 Confusion Between Similar Services

A) Client VPN vs Site-to-Site VPN
- CLIENT VPN = individual users → AWS
- SITE-TO-SITE VPN = entire network (officeDC) → AWS
- Giveaway words employees, remote users, laptops → Client VPN
- Giveaway words corporate network, data centre, on-premises → Site-to-Site VPN

B) NAT Gateway vs Internet Gateway
- IGW allows TWO-WAY traffic (inbound AND outbound) for public subnet resources
- NAT Gateway allows OUTBOUND-ONLY traffic for PRIVATE subnet resources
- If question says inbound connections from internet to private subnet → neither is correct
  (NACLsSecurity Groups control inbound; private instances are not reachable directly)

C) VPC Peering vs Transit Gateway vs PrivateLink
- VPC Peering 2 VPCs, bilateral, full network access, not transitive
- Transit Gateway many VPCs, hub model, transitive routing, supports on-premises
- PrivateLink one-way service access, not full network connectivity

D) VPN vs Direct Connect
- VPN encrypted, internet-based, fast to set up, variable performance
- Direct Connect unencrypted (by default), dedicated fibre, slow to set up, consistent performance

E) Gateway Endpoint vs Interface Endpoint
- Gateway Endpoint S3 + DynamoDB only, free, route-table entry
- Interface Endpoint all other services, paid, creates ENI in your subnet

### Trap Category 2 It's Not Enough By Itself

A) IGW alone doesn't make a subnet public
Also need route table entry (`0.0.0.00 → IGW`) + public IP on the resource.

B) VPC Peering alone doesn't route traffic
Also need route table entries in BOTH VPCs pointing to the peering connection.

C) Creating a NAT Gateway alone doesn't enable internet for private instances
Also need private subnet route table updated with `0.0.0.00 → NAT Gateway`.
AND the NAT Gateway needs to be in a PUBLIC subnet (which has `0.0.0.00 → IGW`).

D) Direct Connect alone isn't redundant
Also need a second DX connection or a Site-to-Site VPN backup for high availability.

E) Direct Connect alone isn't encrypted
Also need a VPN tunnel over it (or MACsec) if encryption is required.

### Trap Category 3 Transitivity

VPC Peering is NOT transitive — this is the most-tested networking fact at CCP level.

If you see VPC A is peered with VPC B. VPC B is peered with VPC C. Can VPC A reach VPC C
Answer No. VPC A must have a direct peering connection to VPC C, OR all three must connect
through a Transit Gateway.

### Trap Category 4 Supporting Components are Not the Answer

When the question asks which service connects your on-premises network to AWS the answer
is Site-to-Site VPN — NOT Virtual Private Gateway and NOT Customer Gateway.

VGW, Customer Gateway, Route Tables, Subnets, NACLs, and Security Groups are components
within a solution. They are never the top-level answer to which AWS service provides X connectivity.

### Trap Category 5 Cost Assumptions

 Service               Free 
-----------------------------
 Internet Gateway      Yes (free, you pay for data transfer) 
 NAT Gateway           No (hourly + per-GB) 
 Gateway VPC Endpoint  Yes (free) 
 Interface VPC Endpoint  No (hourly per AZ + per-GB) 
 VPC Peering           No (data transfer cost) 
 Transit Gateway       No (hourly per attachment + per-GB) 
 Site-to-Site VPN      No (hourly per VPN connection) 
 Direct Connect        No (port fee + data transfer) 
 Client VPN            No (hourly per endpoint + per connection) 

If the question includes most cost-effective way to access S3 from a private subnet →
Gateway VPC Endpoint (free).

### Trap Category 6 Setup Time

 Fast (hours–days)        Slow (weeks–months)   
------------------------------------------------
 Site-to-Site VPN         Direct Connect        
 Client VPN                                     
 VPC Peering                                    
 NAT Gateway                                    
 IGW                                            

If the question says immediately or as soon as possible for on-premises connectivity →
VPN, not Direct Connect.

### Trap Category 7 IP Version Specifics

- NAT Gateway → IPv4 only
- Egress-only Internet Gateway → IPv6 only
- Regular Internet Gateway → works with both IPv4 and IPv6

---

## 11. MEMORY ANCHORS AND MNEMONICS

### The Who Is Talking To Whom Framework
Every time you see a networking question, ask yourself
1. What is the source (EC2, on-prem server, employee laptop, VPC)
2. What is the destination (internet, another VPC, an AWS service, on-prem)
3. What constraints apply (must be private, must be encrypted, must be dedicated, must be fast)

### Mnemonics

NAT is a ONE-WAY DOOR
NAT Gateway only lets traffic OUT from private subnets. Nothing gets IN through NAT.

Peering is like a HANDSHAKE — direct between two people, no middleman
VPC Peering is point-to-point. A handshake between A and B does not mean B and C can talk to A.

Transit Gateway is the AIRPORT HUB
Many flights (VPCs) converge at one hub (TGW). You can fly from any city to any other city
through the hub. The hub routes everything.

Direct Connect is FIRST CLASS on a PRIVATE JET
Expensive. Takes time to arrange. But once you're on it, it's smooth, consistent, and private.

VPN is ECONOMY over a SHARED PLANE
Encrypted (secure), but you're on the public internet (shared infrastructure). Turbulence
(latency spikes) possible. Quick to book (fast to set up).

S3 and DynamoDB are GATEWAY buddies
The only two services that use Gateway (free) VPC Endpoints. Everything else is an Interface Endpoint.

PrivateLink = Private LINK to a service, not to a network
PrivateLink provides access to a specific service. VPC Peering provides full network access.

Client VPN = PERSONAL tunnel. Site-to-Site VPN = TUNNEL between BUILDINGS
Client VPN is for humans on devices. Site-to-Site is for connecting entire network ranges.

### The Shortlist to Memorise (CCP highest-value list)
1. Internet Gateway
2. NAT Gateway
3. Gateway VPC Endpoint (S3 + DynamoDB only)
4. Interface VPC Endpoint  AWS PrivateLink
5. VPC Peering
6. AWS Transit Gateway
7. AWS Site-to-Site VPN
8. AWS Direct Connect
9. AWS Client VPN

---

## QUICK REFERENCE ONE-LINE SUMMARY PER SERVICE

 Service                      One-line purpose                                                              
------------------------------------------------------------------------------------------------------------
 Internet Gateway             Bidirectional internet access for public subnet resources                     
 NAT Gateway                  Outbound-only internet for private subnet resources (IPv4)                    
 Egress-only Internet GW      Outbound-only internet for private subnet resources (IPv6)                    
 Gateway VPC Endpoint         Free private access to S3 and DynamoDB, no internet needed                   
 Interface VPC Endpoint       Private access (via ENI) to any supported AWS service, no internet needed     
 VPC Peering                  Private, direct, bilateral networking between exactly two VPCs                
 Transit Gateway              Central hub for connecting many VPCs and on-premises networks                 
 Site-to-Site VPN             Encrypted IPSec tunnel from on-premises network to AWS over the internet      
 Direct Connect               Dedicated physical private line from on-premises to AWS, no internet          
 Direct Connect + VPN         Encrypted traffic over a dedicated physical line, OR DX with VPN backup       
 Client VPN                   Managed VPN for individual remote users to access AWS and on-prem resources   

---

Last updated for AWS Cloud Practitioner CLF-C02 exam objectives.
All service descriptions sourced from official AWS documentation.