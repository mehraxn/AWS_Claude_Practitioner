# Amazon Verified Permissions

## Simple definition

Amazon Verified Permissions is a fully managed AWS service that helps you control who can do what inside the applications you build.

It is used for authorization, especially fine-grained permissions.

---

## Core idea in plain English

Think of it like this

 Authentication answers Who are you
 Authorization answers What are you allowed to do

Amazon Verified Permissions focuses on the second question.

It helps your application decide things like

 Can this user view this document
 Can this manager approve this request
 Can this customer edit only their own data
 Can this tenant admin manage users in their own company only

Instead of hardcoding these rules inside your app, you place them in a central permission system.

---

## Main use cases

### 1. Fine-grained access control in custom applications

Use it when different users need different levels of access inside your app.

Example
A project app where an owner can delete a project, an editor can update it, and a viewer can only read it.

### 2. Multi-tenant SaaS applications

Useful when one application serves many customers and each customer should only access their own data.

### 3. Role-based and attribute-based permissions

You can build permissions based on

 roles like admin, editor, viewer
 attributes like department, region, tenant, document owner, or project status

### 4. API and backend authorization

Your application or API can ask Verified Permissions whether a request should be allowed before completing the action.

---

## Key features

### Fine-grained authorization

It supports detailed permission decisions, not just simple yesno access for the entire app.

### Centralized policy management

You keep permission rules in one place instead of spreading them across application code.

### Uses Cedar policy language

Permissions are written using Cedar, which is AWS’s policy language for application authorization.

### Supports RBAC and ABAC

 RBAC = Role-Based Access Control
 ABAC = Attribute-Based Access Control

This means permissions can be based on roles or on userresource attributes.

### Policy store

Policies are stored in a policy store, which your app can query during authorization.

### Real-time authorization decisions

Your application sends a request and gets back an Allow or Deny decision.

### Works with identity sources

It can work with identity systems such as Amazon Cognito.

---

## How it works

### Step 1 The user signs in

The user is authenticated by some identity system such as Amazon Cognito or another provider.

### Step 2 The app receives a request

Example
Ali wants to edit Document A.

### Step 3 The app asks Verified Permissions

The app sends information such as

 principal = the user
 action = edit
 resource = Document A
 context = extra details like department, owner, tenant, time, or status

### Step 4 Verified Permissions checks the policies

It evaluates the request against the stored Cedar policies.

### Step 5 It returns a decision

The service returns

 Allow
 Deny

### Step 6 The app enforces the result

If the result is Allow, the app continues.
If the result is Deny, the app blocks the action.

---

## Why it is important for the exam

For exam purposes, the biggest lesson is to understand what Amazon Verified Permissions is for.

It is for

 authorization inside custom applications
 fine-grained permission decisions
 centralized permission policies

It is not mainly for

 signing users in
 managing workforce access to AWS accounts
 granting permissions to AWS services like S3 or EC2

### Exam mindset

If a question talks about

 controlling what users can do inside an application
 checking permissions like view, edit, approve, share, delete
 needing fine-grained and centralized authorization

then Amazon Verified Permissions is a strong match.

### Important Cloud Practitioner note

This is a good service to understand at a high level, especially to avoid confusion with IAM and Cognito.
However, it is not one of the main core services usually emphasized for Cloud Practitioner compared with services like IAM, Cognito, KMS, GuardDuty, or AWS Artifact.

---

## Related AWS services and differences

## Amazon Verified Permissions vs IAM

### IAM

IAM controls access to AWS resources such as

 S3 buckets
 EC2 instances
 Lambda functions
 DynamoDB tables

### Verified Permissions

Verified Permissions controls access inside your own application.

So

 IAM = permissions for AWS services and AWS resources
 Verified Permissions = permissions for actions inside custom apps

---

## Amazon Verified Permissions vs Amazon Cognito

### Cognito

Cognito mainly handles user authentication and user identity for applications.

It helps with things like

 sign-up
 sign-in
 user directory
 tokens
 federation

### Verified Permissions

Verified Permissions decides what that signed-in user is allowed to do.

So

 Cognito = who the user is
 Verified Permissions = what the user can do

---

## Amazon Verified Permissions vs AWS IAM Identity Center

### IAM Identity Center

IAM Identity Center is mainly for workforce users like employees who need access to

 multiple AWS accounts
 AWS applications
 third-party business applications

### Verified Permissions

Verified Permissions is for authorization inside custom-built apps.

So

 IAM Identity Center = workforce access across AWS accounts and apps
 Verified Permissions = fine-grained access decisions inside an app

---

## Amazon Verified Permissions vs AWS KMS

### AWS KMS

AWS KMS manages encryption keys.

### Verified Permissions

Verified Permissions manages authorization rules.

So KMS protects data with encryption, while Verified Permissions controls who can perform actions.

---

## Common exam traps

### Trap 1 Confusing authentication with authorization

If the question is about signing in users, think Amazon Cognito.
If the question is about what users can do after sign-in, think Amazon Verified Permissions.

### Trap 2 Thinking it replaces IAM

It does not replace IAM.
IAM is still for access to AWS resources.
Verified Permissions is for application-level permissions.

### Trap 3 Thinking it stores users and passwords

It does not act as your main user directory or sign-in service.

### Trap 4 Thinking it is mainly for AWS account access

That is more related to IAM and IAM Identity Center, not Verified Permissions.

### Trap 5 Missing the phrase “fine-grained permissions”

When AWS says fine-grained authorization, this is a big clue for Verified Permissions.

---

## Easy real-world example

Imagine you build a document-sharing app.

There are four types of users

 Admin
 Manager
 Editor
 Viewer

Rules

 Admin can do everything
 Manager can approve and view documents in their department
 Editor can edit documents they created
 Viewer can only read approved documents

Instead of writing all these rules directly in your application code, you store them in Amazon Verified Permissions.

Whenever a user tries to do something, your app asks

Is this user allowed to do this action on this document

Verified Permissions checks the policies and answers Allow or Deny.

---

## Final summary

Amazon Verified Permissions is an AWS service for fine-grained authorization in custom applications.

It helps developers separate permission logic from application code and manage it in a central place.

It uses Cedar policies and can make real-time decisions like whether a user can view, edit, approve, or delete something inside an app.

Remember the simple distinction

 Cognito = sign in the user
 Verified Permissions = decide what the user can do
 IAM = control access to AWS resources

---

## Short exam answer

Amazon Verified Permissions is a fully managed AWS service that provides fine-grained authorization for custom applications using centralized policies.

---

## Memory trick

Verified Permissions = Verify permission inside the app

Another easy memory line

 Cognito = Who are you
 Verified Permissions = What can you do
 IAM = What can access AWS
