# AWS IAM (Identity and Access Management)

## Simple definition

AWS IAM is the AWS service that helps you control who can access AWS resources and what they are allowed to do.

## Core idea in plain English

Think of IAM as the security guard and permission system for your AWS account.

It answers two big questions

 Who are you
 What are you allowed to do

With IAM, you can create users, groups, and roles, then give them the right permissions.

## Main use cases

IAM is commonly used for

 Giving employees their own AWS login
 Controlling access to services like S3, EC2, and RDS
 Giving applications permission to use AWS services securely
 Allowing temporary access instead of sharing passwords
 Applying security best practices like least privilege
 Managing access for admins, developers, and auditors

## Key features

### 1. Users

An IAM user represents one person or application that needs long-term access to AWS.

A user can have

 A password for the AWS Management Console
 Access keys for the AWS CLI or API

### 2. Groups

A group is a collection of IAM users.

Instead of giving permissions to each user one by one, you can place users in a group and assign permissions to the group.

Example

 Admins group
 Developers group
 ReadOnly group

### 3. Policies

Policies are JSON documents that define permissions.

They say what actions are allowed or denied on which AWS resources.

Example ideas

 Allow reading an S3 bucket
 Allow starting EC2 instances
 Deny deleting databases

### 4. Roles

An IAM role is an identity that AWS services, applications, or users can assume temporarily.

Roles are very important in AWS.

Examples

 An EC2 instance uses a role to access S3
 A Lambda function uses a role to write logs to CloudWatch
 One AWS account can assume a role in another AWS account

### 5. Multi-Factor Authentication (MFA)

IAM supports MFA for extra security.

This means users need a second step when signing in, such as a code from an authenticator app.

### 6. Temporary credentials

IAM roles usually provide temporary credentials instead of permanent access keys.

This is safer and is a common AWS best practice.

## How it works

Here is the simple flow

1. You create an identity in IAM, such as a user or role.
2. You attach permissions using policies.
3. The identity tries to access an AWS resource.
4. AWS checks the policy.
5. AWS allows or denies the action.

IAM follows the idea of authentication and authorization

 Authentication = proving who you are
 Authorization = deciding what you can do

By default, new IAM users have no permissions until permissions are granted.

## Why it is important for the exam

IAM is one of the most important topics in the AWS Certified Cloud Practitioner exam.

You need to understand that

 IAM controls access in AWS
 IAM is a global service, not tied to one Region
 Users are for people or apps needing direct access
 Groups are for organizing users
 Roles are for temporary access
 Policies define permissions
 Root user should not be used for everyday tasks
 MFA should be enabled, especially for the root user

## Related AWS services and differences

### IAM vs Root user

 Root user = the original account owner with full access
 IAM user = a separate identity with limited permissions

Use the root user only for a few account-level tasks. Use IAM users or roles for daily work.

### IAM vs IAM Identity Center

 IAM manages users, groups, roles, and permissions inside AWS
 IAM Identity Center helps provide centralized access to multiple AWS accounts and applications

Identity Center is better for workforce access across many accounts.

### IAM vs Resource-based policies

 IAM policies are attached to users, groups, or roles
 Resource-based policies are attached directly to resources like S3 buckets

Both control access, but they are attached in different places.

### IAM vs Security Groups

 IAM controls who can do actions in AWS
 Security Groups control network traffic to resources like EC2

IAM is about identity and permissions. Security Groups are about network access.

## Common exam traps

### Trap 1 Thinking IAM is regional

Wrong. IAM is a global service.

### Trap 2 Confusing users and roles

 Users usually have long-term credentials
 Roles usually provide temporary credentials

### Trap 3 Using the root user for normal work

This is bad practice. The exam often expects you to choose IAM users or roles instead.

### Trap 4 Thinking groups can contain other groups

IAM groups contain users, not other groups.

### Trap 5 Forgetting least privilege

AWS recommends giving only the permissions needed to do a job, nothing more.

### Trap 6 Confusing authentication with authorization

 Authentication = sign in
 Authorization = permissions after sign-in

## Easy real-world example

A company has three employees

 Anna is an admin
 Ben is a developer
 Carla only needs to view reports

The company creates

 An Admins group with full admin permissions
 A Developers group with EC2 and S3 access
 A ReadOnly group for viewing resources only

Each employee gets their own IAM user and is placed into the correct group.

Later, the company launches an EC2 instance that needs to read files from S3. Instead of storing access keys on the server, they attach an IAM role to the EC2 instance.

That is the AWS best-practice approach.

## Final summary

AWS IAM is the main service for controlling access in AWS.

It helps you securely manage identities and permissions by using

 Users
 Groups
 Roles
 Policies
 MFA

For the exam, remember that IAM is global, root user access should be limited, and roles are commonly used for temporary and secure access.

## Short exam answer

AWS IAM is a global AWS service that controls authentication and authorization by letting you manage users, groups, roles, and permissions through policies.

## Memory trick

IAM = Identity And Management of access

An easy memory line

“IAM decides who gets in and what they can do.”
