# AWS Audit Manager

## Simple definition

AWS Audit Manager is an AWS service that helps you automatically collect and organize audit evidence for compliance and risk assessments.

It reduces the manual work of preparing for audits.

---

## Core idea in plain English

Think of AWS Audit Manager as an audit helper.

Normally, during an audit, teams spend a lot of time collecting screenshots, configuration details, logs, and proof that security controls are working.

AWS Audit Manager helps by automatically gathering evidence from your AWS environment and organizing it based on audit frameworks and controls.

So instead of chasing documents manually, you get a more structured and repeatable audit process.

---

## Main use cases

### 1. Preparing for compliance audits

A company can use Audit Manager to collect evidence for standards such as security and compliance frameworks.

### 2. Reducing manual audit work

Security and compliance teams can save time because evidence is collected automatically from AWS data sources.

### 3. Tracking internal controls

Organizations can review whether their controls, policies, and procedures are being followed.

### 4. Building audit-ready reports

Teams can generate reports and share them with internal reviewers or external auditors.

### 5. Multi-account auditing

Large companies using multiple AWS accounts can centralize evidence collection across accounts.

---

## Key features

### Automated evidence collection

Audit Manager automatically collects evidence from AWS services instead of requiring you to gather everything by hand.

### Prebuilt frameworks

It provides standard frameworks that map controls to common compliance requirements.

### Custom frameworks and controls

You can also create your own frameworks and controls if your company has internal requirements.

### Assessment reports

You can generate audit reports from the collected evidence.

### Evidence review workflow

Teams can review controls, add comments, upload manual evidence, and track progress.

### Multi-account support

It can work across accounts in AWS Organizations, which is useful for enterprise environments.

### Continuous evidence collection

Evidence collection continues while an assessment is active.

---

## How it works

Here is the simple flow

1. You choose a framework.
2. You create an assessment.
3. You define the AWS accounts and services that are in scope.
4. Audit Manager starts collecting evidence automatically.
5. The evidence is mapped to controls.
6. Reviewers can inspect the evidence, add comments, and upload manual files if needed.
7. You generate an assessment report for the audit.

### Important words to know

 Framework = a collection of controls based on a standard or requirement
 Control = a specific requirement that must be checked
 Assessment = the audit project you create in Audit Manager
 Evidence = the proof collected to show a control is being met

---

## Why it is important for the exam

For the Cloud Practitioner exam, the main idea is simple

AWS Audit Manager helps automate evidence collection for audits and compliance reviews.

This matters because exam questions often test whether you can identify the service that

 reduces manual effort during audits
 helps with compliance evidence
 organizes evidence by controls and frameworks
 creates audit-ready reports

You should also remember that Audit Manager is part of the governance, risk, and compliance area of AWS.

---

## Related AWS services and differences

### AWS Audit Manager vs AWS Artifact

 Audit Manager helps you collect evidence about your own AWS usage
 AWS Artifact gives you AWS compliance reports and agreements such as AWS certifications and audit documents

Easy way to remember

 Artifact = documents from AWS
 Audit Manager = evidence about your environment

### AWS Audit Manager vs AWS Config

 AWS Config records and evaluates resource configurations
 Audit Manager uses evidence, including from services like Config, to support audits

Config checks resource settings. Audit Manager organizes evidence for audit work.

### AWS Audit Manager vs AWS CloudTrail

 CloudTrail records API activity and account actions
 Audit Manager can use such information as audit evidence

CloudTrail logs actions. Audit Manager manages evidence.

### AWS Audit Manager vs AWS Security Hub

 Security Hub shows security findings and security posture
 Audit Manager focuses on audit evidence and compliance assessments

Security Hub is for security visibility. Audit Manager is for audit preparation.

---

## Common exam traps

### Trap 1 Thinking Audit Manager proves compliance automatically

This is the biggest trap.

Audit Manager does not certify that you are compliant.

It helps collect and organize evidence, but people still need to review the evidence and make compliance decisions.

### Trap 2 Confusing it with AWS Artifact

If the question asks for downloading AWS compliance reports from AWS, the answer is AWS Artifact, not Audit Manager.

### Trap 3 Confusing it with AWS Config

If the question is about checking whether a resource configuration follows a rule, that is more likely AWS Config.

### Trap 4 Confusing it with CloudTrail

If the question is about logging API calls or user actions, that is AWS CloudTrail.

### Trap 5 Assuming everything is fully automatic

Audit Manager automates a lot, but teams may still need to add manual evidence and review results.

---

## Easy real-world example

Imagine a company is preparing for a security audit.

The auditor asks for proof that

 important AWS resources are configured correctly
 changes are tracked
 certain controls are reviewed regularly

Without Audit Manager, the team might spend days collecting screenshots, logs, spreadsheets, and emails.

With Audit Manager, the company creates an assessment, selects the framework, and lets AWS automatically gather much of the needed evidence. The team then reviews it and generates a report for the auditor.

---

## Final summary

AWS Audit Manager is a service that helps organizations prepare for audits faster by automating evidence collection and organizing that evidence around frameworks, controls, and assessments.

It is useful for compliance teams, security teams, and organizations that want a more structured audit process.

For the exam, remember this key message

Audit Manager helps with audit evidence and compliance readiness, but it does not itself guarantee compliance.

---

## Short exam answer

AWS Audit Manager is a service that automates the collection of audit evidence to help organizations simplify risk and compliance assessments and generate audit-ready reports.

---

## Memory trick

Audit Manager = “Manage my audit evidence.”

Or even shorter

Artifact gives AWS documents. Audit Manager gathers your audit proof.
