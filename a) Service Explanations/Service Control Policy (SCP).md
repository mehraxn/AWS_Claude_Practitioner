# Service Control Policy (SCP)

## Simple definition

A Service Control Policy (SCP) is a policy in AWS Organizations that sets the maximum permissions available in AWS accounts inside an organization.

It is a guardrail, not a permission grant.

---

## Core idea in plain English

Think of an SCP like a company-wide rulebook for AWS accounts.

Even if someone inside an account has an IAM policy that says Allow, they still cannot do something if the SCP blocks it.

So SCPs do not give access. They only say

 what accounts are allowed to use
 what accounts are not allowed to use
 what actions are limited across many accounts at once

A good memory sentence is

IAM gives permissions. SCP limits permissions.

---

## Main use cases

### 1. Blocking dangerous services or actions

A company can use SCPs to stop member accounts from using certain AWS services or performing risky actions.

Example block deleting CloudTrail logs or block turning off security services.

### 2. Restricting AWS Regions

A company may want workloads to run only in approved Regions for compliance or cost reasons.

### 3. Enforcing company-wide security rules

SCPs help security teams apply central restrictions across many AWS accounts.

### 4. Preventing accidental changes

An SCP can stop admins in member accounts from changing sensitive settings.

### 5. Keeping sandbox or junior-admin accounts under control

Organizations can limit what test accounts or less trusted teams are able to do.

---

## Key features

 Works with AWS Organizations
 Applies to organization roots, OUs, and accounts
 Sets the maximum available permissions
 Uses JSON policy syntax similar to IAM policies
 Can use Allow and Deny statements
 Helps manage permissions centrally across multiple accounts
 Affects member accounts, including their root users
 Inherits through the organization structure

---

## How it works

### Step 1 Create an organization

You use AWS Organizations to manage multiple AWS accounts.

### Step 2 Organize accounts

You can group accounts into Organizational Units (OUs), such as

 Production
 Development
 Security
 Sandbox

### Step 3 Attach an SCP

You attach the SCP to

 the root of the organization
 an OU
 or a specific account

### Step 4 AWS evaluates permissions

When a user or role in a member account tries to perform an action, AWS checks

 the IAM permissions in that account
 and the SCP guardrails from AWS Organizations

The action is allowed only if it is allowed by IAM and not blocked by the SCP.

### Very important rule

An SCP never grants permission by itself.

That means this is wrong

 “I attached an SCP, so now the user can access S3.”

No. The user still needs IAM permissions.

---

## Why it is important for the exam

SCP is important because AWS exam questions often test whether you understand the difference between

 granting permissions
 and limiting permissions

This is one of the most common AWS exam traps.

You should remember these points very clearly

 SCPs are part of AWS Organizations
 SCPs are used for multi-account governance
 SCPs do not grant permissions
 SCPs define the maximum allowed permissions
 IAM permissions inside the account are still needed
 SCPs are mainly for central control at scale

---

## Related AWS services and differences

### 1. AWS Organizations vs SCP

AWS Organizations is the service used to manage multiple AWS accounts.

SCP is one of the policy types used inside AWS Organizations.

So

 Organizations = the overall multi-account management service
 SCP = the permission guardrail policy used inside it

### 2. IAM policies vs SCP

This is the most important comparison.

IAM policies

 grant or deny permissions to users, groups, or roles in one account
 are used for day-to-day access control

SCPs

 do not grant permissions
 set the outer permission boundary for accounts in an organization
 are used for central governance across accounts

Easy way to remember

 IAM = what a principal can do
 SCP = the maximum that account principals are allowed to do

### 3. Permission boundaries vs SCP

Both are limits, so students mix them up.

Permission boundaries

 limit a specific IAM user or role
 work inside one account

SCPs

 limit all principals in member accounts
 work at the organization, OU, or account level

### 4. IAM Identity Center vs SCP

IAM Identity Center helps users sign in and get access to AWS accounts and applications.

SCP does not manage sign-in. It only limits what actions are allowed after access exists.

### 5. AWS Control Tower vs SCP

AWS Control Tower helps set up and govern a multi-account AWS environment.

It often uses AWS Organizations and organization guardrails in the background.

SCPs are one way to enforce permission restrictions. Control Tower is broader and helps build the whole landing zone.

### 6. AWS Config vs SCP

AWS Config checks and records resource configurations.

SCP prevents certain actions from being performed.

So

 Config = detect and assess compliance
 SCP = prevent certain actions at the permissions level

---

## Common exam traps

### Trap 1 Thinking SCP grants permissions

This is the biggest trap.

SCPs do not grant access.

### Trap 2 Confusing SCP with IAM policy

IAM policies are attached to users, groups, or roles.

SCPs are attached to the organization root, OUs, or accounts.

### Trap 3 Thinking SCP is for one user only

No. SCP affects the account level inside AWS Organizations, not just one user.

### Trap 4 Forgetting multi-account context

If the question talks about controlling many AWS accounts centrally, think

AWS Organizations + SCP

### Trap 5 Thinking SCP replaces IAM

It does not.

Even with an SCP in place, you still need IAM policies to actually allow access.

### Trap 6 Thinking SCP only affects normal IAM users

SCPs also affect member-account principals broadly, including the member account root user.

### Trap 7 Thinking SCP controls the management account the same way

For exam thinking, remember that SCPs are mainly about member accounts in the organization.

### Trap 8 Mixing SCP with service-linked roles or resource compliance tools

SCP is about permission guardrails, not general auditing, login, or configuration tracking.

---

## Easy real-world example

A company has 50 AWS accounts.

The security team wants to make sure nobody in the development accounts can disable security monitoring or launch resources in unapproved Regions.

They create an OU called Development and attach an SCP to that OU.

Now, even if a developer has an IAM policy with broad permissions inside one dev account, AWS still blocks the actions that the SCP does not allow.

This gives the company one central security control across many accounts.

---

## If I were an examiner ...

Here are the kinds of things I would ask about SCP in the exam

### 1. Do you know what SCP really does

I may ask which service sets the maximum available permissions for accounts in AWS Organizations.

### 2. Do you know that SCP does not grant permissions

I may give a question where a user still cannot access a service even though an SCP exists.
The correct idea is that the user also needs IAM permission.

### 3. Can you choose between IAM and SCP

If the question is about one user in one account, IAM is usually the answer.
If the question is about many accounts with central governance, SCP is usually the answer.

### 4. Can you identify the multi-account governance use case

If the company wants one policy applied across many accounts, I would expect you to think of AWS Organizations with SCPs.

### 5. Do you understand central restriction versus compliance checking

If the question is about preventing actions, SCP may fit.
If the question is about recording, auditing, or checking configuration, another service such as AWS Config may fit better.

### 6. Can you spot the wording trap

If the option says “grant permissions across all accounts,” that is suspicious.
SCP does not grant. It restricts.

---

## Final summary

A Service Control Policy (SCP) is a central permission guardrail used with AWS Organizations.

It helps companies control what AWS accounts in the organization are allowed to do.

It is especially useful in multi-account environments where a central team wants to apply security or compliance restrictions across many accounts.

The most important thing to remember is this

SCP does not grant permissions. It only limits the maximum permissions.

IAM policies are still needed to actually allow actions.

---

## Short exam answer

A Service Control Policy (SCP) is an AWS Organizations policy that sets the maximum permissions for member accounts in an organization. It is used for central governance across multiple accounts and does not grant permissions by itself.

---

## Memory trick

Remember this

SCP = Security Ceiling Policy

It acts like a ceiling above the account.

Even if IAM says yes, the principal cannot go above the ceiling.

Another simple memory line

IAM gives. SCP limits.
# Service Control Policy (SCP)

## Simple definition

A Service Control Policy (SCP) is a policy in AWS Organizations that sets the maximum permissions available in AWS accounts inside an organization.

It is a guardrail, not a permission grant.

---

## Core idea in plain English

Think of an SCP like a company-wide rulebook for AWS accounts.

Even if someone inside an account has an IAM policy that says Allow, they still cannot do something if the SCP blocks it.

So SCPs do not give access. They only say

 what accounts are allowed to use
 what accounts are not allowed to use
 what actions are limited across many accounts at once

A good memory sentence is

IAM gives permissions. SCP limits permissions.

---

## Main use cases

### 1. Blocking dangerous services or actions

A company can use SCPs to stop member accounts from using certain AWS services or performing risky actions.

Example block deleting CloudTrail logs or block turning off security services.

### 2. Restricting AWS Regions

A company may want workloads to run only in approved Regions for compliance or cost reasons.

### 3. Enforcing company-wide security rules

SCPs help security teams apply central restrictions across many AWS accounts.

### 4. Preventing accidental changes

An SCP can stop admins in member accounts from changing sensitive settings.

### 5. Keeping sandbox or junior-admin accounts under control

Organizations can limit what test accounts or less trusted teams are able to do.

---

## Key features

 Works with AWS Organizations
 Applies to organization roots, OUs, and accounts
 Sets the maximum available permissions
 Uses JSON policy syntax similar to IAM policies
 Can use Allow and Deny statements
 Helps manage permissions centrally across multiple accounts
 Affects member accounts, including their root users
 Inherits through the organization structure

---

## How it works

### Step 1 Create an organization

You use AWS Organizations to manage multiple AWS accounts.

### Step 2 Organize accounts

You can group accounts into Organizational Units (OUs), such as

 Production
 Development
 Security
 Sandbox

### Step 3 Attach an SCP

You attach the SCP to

 the root of the organization
 an OU
 or a specific account

### Step 4 AWS evaluates permissions

When a user or role in a member account tries to perform an action, AWS checks

 the IAM permissions in that account
 and the SCP guardrails from AWS Organizations

The action is allowed only if it is allowed by IAM and not blocked by the SCP.

### Very important rule

An SCP never grants permission by itself.

That means this is wrong

 “I attached an SCP, so now the user can access S3.”

No. The user still needs IAM permissions.

---

## Why it is important for the exam

SCP is important because AWS exam questions often test whether you understand the difference between

 granting permissions
 and limiting permissions

This is one of the most common AWS exam traps.

You should remember these points very clearly

 SCPs are part of AWS Organizations
 SCPs are used for multi-account governance
 SCPs do not grant permissions
 SCPs define the maximum allowed permissions
 IAM permissions inside the account are still needed
 SCPs are mainly for central control at scale

---

## Related AWS services and differences

### 1. AWS Organizations vs SCP

AWS Organizations is the service used to manage multiple AWS accounts.

SCP is one of the policy types used inside AWS Organizations.

So

 Organizations = the overall multi-account management service
 SCP = the permission guardrail policy used inside it

### 2. IAM policies vs SCP

This is the most important comparison.

IAM policies

 grant or deny permissions to users, groups, or roles in one account
 are used for day-to-day access control

SCPs

 do not grant permissions
 set the outer permission boundary for accounts in an organization
 are used for central governance across accounts

Easy way to remember

 IAM = what a principal can do
 SCP = the maximum that account principals are allowed to do

### 3. Permission boundaries vs SCP

Both are limits, so students mix them up.

Permission boundaries

 limit a specific IAM user or role
 work inside one account

SCPs

 limit all principals in member accounts
 work at the organization, OU, or account level

### 4. IAM Identity Center vs SCP

IAM Identity Center helps users sign in and get access to AWS accounts and applications.

SCP does not manage sign-in. It only limits what actions are allowed after access exists.

### 5. AWS Control Tower vs SCP

AWS Control Tower helps set up and govern a multi-account AWS environment.

It often uses AWS Organizations and organization guardrails in the background.

SCPs are one way to enforce permission restrictions. Control Tower is broader and helps build the whole landing zone.

### 6. AWS Config vs SCP

AWS Config checks and records resource configurations.

SCP prevents certain actions from being performed.

So

 Config = detect and assess compliance
 SCP = prevent certain actions at the permissions level

---

## Common exam traps

### Trap 1 Thinking SCP grants permissions

This is the biggest trap.

SCPs do not grant access.

### Trap 2 Confusing SCP with IAM policy

IAM policies are attached to users, groups, or roles.

SCPs are attached to the organization root, OUs, or accounts.

### Trap 3 Thinking SCP is for one user only

No. SCP affects the account level inside AWS Organizations, not just one user.

### Trap 4 Forgetting multi-account context

If the question talks about controlling many AWS accounts centrally, think

AWS Organizations + SCP

### Trap 5 Thinking SCP replaces IAM

It does not.

Even with an SCP in place, you still need IAM policies to actually allow access.

### Trap 6 Thinking SCP only affects normal IAM users

SCPs also affect member-account principals broadly, including the member account root user.

### Trap 7 Thinking SCP controls the management account the same way

For exam thinking, remember that SCPs are mainly about member accounts in the organization.

### Trap 8 Mixing SCP with service-linked roles or resource compliance tools

SCP is about permission guardrails, not general auditing, login, or configuration tracking.

---

## Easy real-world example

A company has 50 AWS accounts.

The security team wants to make sure nobody in the development accounts can disable security monitoring or launch resources in unapproved Regions.

They create an OU called Development and attach an SCP to that OU.

Now, even if a developer has an IAM policy with broad permissions inside one dev account, AWS still blocks the actions that the SCP does not allow.

This gives the company one central security control across many accounts.

---

## If I were an examiner ...

Here are the kinds of things I would ask about SCP in the exam

### 1. Do you know what SCP really does

I may ask which service sets the maximum available permissions for accounts in AWS Organizations.

### 2. Do you know that SCP does not grant permissions

I may give a question where a user still cannot access a service even though an SCP exists.
The correct idea is that the user also needs IAM permission.

### 3. Can you choose between IAM and SCP

If the question is about one user in one account, IAM is usually the answer.
If the question is about many accounts with central governance, SCP is usually the answer.

### 4. Can you identify the multi-account governance use case

If the company wants one policy applied across many accounts, I would expect you to think of AWS Organizations with SCPs.

### 5. Do you understand central restriction versus compliance checking

If the question is about preventing actions, SCP may fit.
If the question is about recording, auditing, or checking configuration, another service such as AWS Config may fit better.

### 6. Can you spot the wording trap

If the option says “grant permissions across all accounts,” that is suspicious.
SCP does not grant. It restricts.

---

## Final summary

A Service Control Policy (SCP) is a central permission guardrail used with AWS Organizations.

It helps companies control what AWS accounts in the organization are allowed to do.

It is especially useful in multi-account environments where a central team wants to apply security or compliance restrictions across many accounts.

The most important thing to remember is this

SCP does not grant permissions. It only limits the maximum permissions.

IAM policies are still needed to actually allow actions.

---

## Short exam answer

A Service Control Policy (SCP) is an AWS Organizations policy that sets the maximum permissions for member accounts in an organization. It is used for central governance across multiple accounts and does not grant permissions by itself.

---

## Memory trick

Remember this

SCP = Security Ceiling Policy

It acts like a ceiling above the account.

Even if IAM says yes, the principal cannot go above the ceiling.

Another simple memory line

IAM gives. SCP limits.
