# Remote Desktop Protocol (RDP) Connection

## Simple definition

Remote Desktop Protocol (RDP) is a Microsoft protocol that lets you connect to and control a Windows computer from another computer over a network.

In AWS, RDP is mainly used to connect to Windows Amazon EC2 instances.

## Core idea in plain English

Think of RDP like opening the screen of a remote Windows machine.

You are not just sending commands. You are seeing and using the full Windows desktop as if you were sitting in front of that server.

For the AWS Cloud Practitioner exam, the big idea is simple

 Use RDP to connect to Windows EC2 instances
 Default RDP port is 3389
 SSH is usually for Linux, RDP is for Windows

## Main use cases

RDP is commonly used when you need to

 Log in to a Windows EC2 instance
 Manage Windows settings with a graphical interface
 Install software on a Windows server
 Troubleshoot a Windows-based application
 Access tools like IIS Manager, Event Viewer, or Server Manager

## Key features

RDP connection has several important features

 Gives you a graphical desktop session
 Designed mainly for Windows systems
 Uses TCP port 3389 by default
 Lets administrators manage remote Windows servers
 Works over a network, including the internet if allowed
 On AWS, it is typically protected by security groups, usernames, and passwords

## How it works

Here is the basic flow in AWS

1. You launch a Windows EC2 instance.
2. The EC2 instance gets network access through a public IP, Elastic IP, VPN, Direct Connect, or private network path.
3. The instance's security group must allow inbound RDP traffic on port 3389 from your IP address.
4. You retrieve the Windows administrator password, usually by using the EC2 key pair you selected at launch.
5. You open an RDP client on your local computer.
6. You connect to the EC2 instance using its public DNS name or IP address.
7. You log in and see the Windows desktop remotely.

## Why it is important for the exam

RDP matters because AWS exam questions often test how to connect to an EC2 instance.

You need to remember these common rules

 Windows EC2 instance → use RDP
 Linux EC2 instance → use SSH
 RDP default port = 3389
 Security groups control whether the connection is allowed

This is a very common exam topic because it mixes together

 EC2
 Security groups
 Operating systems
 Basic network access

## Related AWS services and differences

### Amazon EC2

EC2 gives you the virtual server.

RDP is one way to connect to a Windows EC2 server after it is launched.

### Security Groups

Security groups act like a virtual firewall for the EC2 instance.

To use RDP, the security group must allow inbound TCP 3389 from an approved source.

### Key Pair

For Windows EC2, the key pair is often used to decrypt or retrieve the initial administrator password.

For Linux EC2, the key pair is usually used directly with SSH authentication.

### SSH

SSH is used mainly for Linux instances.

 SSH = command-line remote access
 RDP = full graphical remote desktop access

### AWS Systems Manager Session Manager

Session Manager can connect to instances without opening inbound ports in security groups.

This is different from traditional RDP, which usually requires opening port 3389.

For the Cloud Practitioner exam, Session Manager is often seen as a more secure management option because it can reduce the need for open administrative ports.

### EC2 Instance Connect

EC2 Instance Connect is mainly associated with Linux SSH access, not standard Windows RDP access.

## Common exam traps

Here are the mistakes AWS exam questions often try to make you choose

### Trap 1 Mixing up RDP and SSH

A very common mistake is choosing SSH for Windows or RDP for Linux.

Remember

 Windows = RDP
 Linux = SSH

### Trap 2 Forgetting the port number

Many exam questions test port numbers.

 RDP = 3389
 SSH = 22
 HTTP = 80
 HTTPS = 443

### Trap 3 Ignoring the security group

Even if the instance is running, you still cannot connect unless the security group allows the traffic.

### Trap 4 Allowing RDP from everywhere

Opening port 3389 to 0.0.0.00 means anyone on the internet can try to reach that port.

In real life, this is risky. In exam questions, the better answer is usually to allow RDP only from a trusted IP range.

### Trap 5 Forgetting network reachability

A Windows instance in a private subnet may not be reachable directly from your laptop unless there is a VPN, bastion host, or another private connection path.

## Easy real-world example

A company launches a Windows EC2 instance to run a .NET application.

The administrator needs to install software and check logs on the server.

They do the following

 Launch the Windows EC2 instance
 Allow RDP on port 3389 in the security group from the office IP address
 Retrieve the Administrator password
 Open Microsoft Remote Desktop
 Connect to the server and manage it through the Windows desktop

That is a classic AWS example of using RDP.

## Final summary

RDP is the standard remote desktop method for connecting to Windows servers.

In AWS, it is most commonly used to connect to a Windows EC2 instance.

For the exam, remember the three biggest points

 RDP is for Windows
 Port 3389 is used by default
 Security groups must allow the connection

If you remember those three facts, you will answer most basic RDP exam questions correctly.

## Short exam answer

RDP is a protocol used to remotely connect to a Windows EC2 instance using a graphical desktop session, usually over TCP port 3389.

## Memory trick

Think

RDP = Remote Desktop = Windows screen
SSH = Secure Shell = Linux terminal

Another easy memory trick

 RDP = 33-89 → the “desktop door” for Windows
 SSH = 22 → the “terminal door” for Linux
