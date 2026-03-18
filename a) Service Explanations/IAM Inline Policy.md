# IAM Inline Policy

## Simple definition

An IAM inline policy is a policy written directly inside one IAM user, group, or role.

It gives permissions only to that single identity and stays attached only to that identity.

---

## Core idea in plain English

Think of an inline policy like a special note glued to one person’s file.

It is made for one specific user, group, or role.
You do not reuse it somewhere else.
If that identity is deleted, the inline policy is deleted too.

Important inline policy does not mean “one-time use.” It can be used again and again by that same identity until you remove or change it.

---

## Main use cases

IAM inline policies are mainly used when you want unique permissions for only one identity.

Common use cases

 Give a single IAM role a very specific permission
 Give one user a custom exception
 Add one special permission to one group only
 Keep a strict one-to-one relationship between the policy and the identity

In real life, AWS usually prefers managed policies for reusable permissions, but inline policies are useful for special cases.

---

## Key features

 Attached to only one IAM identity
 Can be used with an IAM user, group, or role
 Not reusable across multiple identities
 Deleted automatically if the identity is deleted
 Written in JSON like other IAM policies
 Used for identity-based permissions

---

## How it works

An inline policy contains JSON that defines

 Effect → Allow or Deny
 Action → what the identity can do
 Resource → which AWS resource it can access
 sometimes Condition → when access is allowed

AWS checks this policy when the IAM user, group, or role tries to do something.

If the policy allows the action, and no other policy blocks it, the request can succeed.

### Simple example

A role could have an inline policy that allows

 `s3GetObject`
 on one specific S3 bucket

That means the role can read objects from that bucket only.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, the big idea is this

 Inline policy = one identity only

You should recognize that inline policies are different from managed policies because

 they are not shared
 they are not centrally reused
 they are best for special one-off permissions

This difference appears often in AWS exam questions.

---

## Related AWS services and differences

### IAM Inline Policy vs Customer Managed Policy

Inline policy

 belongs to one user, group, or role
 cannot be reused across identities
 deleted with the identity

Customer managed policy

 created as a separate policy object in IAM
 can be attached to many users, groups, and roles
 easier to manage at scale

### IAM Inline Policy vs AWS Managed Policy

Inline policy

 created by you
 embedded directly into one identity
 for special custom permissions

AWS managed policy

 created and maintained by AWS
 reusable
 good for common job roles and common AWS access patterns

### IAM Inline Policy vs Resource-based Policy

Inline policy

 attached to an identity
 says what that identity can do

Resource-based policy

 attached to a resource like an S3 bucket
 says who can access that resource

### IAM Inline Policy vs Permissions Boundary

Inline policy

 grants permissions

Permissions boundary

 sets the maximum permissions an identity can have
 uses a managed policy, not an inline policy

---

## Common exam traps

### Trap 1 Thinking inline policies are one-time use

Wrong.
They are not one-time use.
They continue working for that same identity until removed or changed.

### Trap 2 Thinking inline policies are reusable

They are not reusable.
They are attached to only one identity.

### Trap 3 Confusing inline policies with managed policies

Managed policies are separate IAM objects.
Inline policies live directly inside the identity.

### Trap 4 Thinking inline means stronger security by default

Inline does not automatically mean more secure.
It simply means the policy is tied to one identity.

### Trap 5 Forgetting deletion behavior

If you delete the IAM user, group, or role, the inline policy is deleted too.

### Trap 6 Using inline policies for many identities

If many users or roles need the same permissions, the better answer is usually customer managed policy, not inline policy.

---

## Easy real-world example

A company has one special admin role called BillingAuditRole.

This role needs permission to view billing reports and one specific S3 folder.
No other role needs this exact permission set.

Instead of making a reusable policy for many identities, the company adds an inline policy directly to that role.

That is a good inline policy use case because the permission is unique to one identity.

---

## Final summary

IAM inline policies are identity-based policies that are embedded directly into one IAM user, group, or role.

They are not shared across many identities.
They are best for special, unique permissions.

Remember

 one identity
 not reusable
 deleted with the identity
 not one-time use

---

## Short exam answer

An IAM inline policy is a policy embedded directly in a single IAM user, group, or role. It is used for one specific identity, is not reusable across multiple identities, and is deleted when that identity is deleted.

---

## Memory trick

Inline = in the line of one identity

So remember

 Inline = inside one identity
 Managed = shared and reusable
