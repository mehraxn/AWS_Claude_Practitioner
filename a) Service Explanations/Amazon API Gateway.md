# Amazon API Gateway

## Simple definition

Amazon API Gateway is a fully managed AWS service that helps you create, publish, secure, monitor, and manage APIs.

In simple words, it is the front door that lets apps, users, or systems send requests to your backend services.

---

## Core idea in plain English

Think of Amazon API Gateway like a receptionist in front of your application.

Clients send requests to API Gateway.
API Gateway then sends those requests to the correct backend, such as

 AWS Lambda
 Amazon EC2
 containers running on Amazon ECS or EKS
 applications behind a load balancer
 other AWS services

It also helps control who can access the API, how many requests are allowed, and how the requests are monitored.

---

## Main use cases

 Create APIs for mobile apps and web apps
 Build serverless applications with AWS Lambda
 Expose backend services securely to customers or internal teams
 Create microservices communication endpoints
 Build real-time applications with WebSocket APIs
 Manage traffic, authentication, and throttling for APIs

---

## Key features

 Fully managed API service
 Supports REST APIs, HTTP APIs, and WebSocket APIs
 Works well with AWS Lambda
 Authentication and authorization support
 Throttling to control request rates
 Monitoring with Amazon CloudWatch
 Request validation for some API types
 Caching for performance improvement
 Stages such as dev, test, and prod
 Custom domain names
 Can connect to public, regional, or private backends depending on setup

---

## How it works

### Basic flow

1. A client sends a request to an API endpoint.
2. Amazon API Gateway receives the request.
3. API Gateway checks things like authentication, authorization, and throttling.
4. It forwards the request to the backend service.
5. The backend processes the request.
6. API Gateway returns the response to the client.

### Example backend targets

 Lambda function
 Application running on EC2
 Containerized service
 AWS service integration

### API types you should know

#### 1. REST API

This is the more feature-rich API type.

Use it when you need advanced API management features such as

 API keys
 usage plans
 request validation
 some advanced controls

#### 2. HTTP API

This is a simpler and lower-cost option for many modern APIs.

Use it when you want

 simple API proxying
 low latency
 serverless integrations
 JWT or basic modern API use cases

#### 3. WebSocket API

Use this for two-way real-time communication.

Examples

 chat applications
 live dashboards
 real-time notifications

---

## Why it is important for the exam

Amazon API Gateway is important because AWS exam questions often test whether you understand

 which AWS service exposes APIs securely
 which service works naturally with Lambda for serverless APIs
 the difference between API Gateway and services like Elastic Load Balancing
 when to use API Gateway for mobile, web, and microservices access
 when WebSocket APIs are needed for real-time communication

For Cloud Practitioner, the exam usually tests the main purpose of API Gateway, not deep developer configuration.

The key exam idea is

API Gateway is used to create, publish, secure, monitor, and manage APIs.

---

## Related AWS services and differences

### AWS Lambda

 Lambda runs the code
 API Gateway receives API requests and sends them to Lambda or other backends

Easy memory line
API Gateway is the front door, Lambda is the worker behind the door.

### Elastic Load Balancing (ELB)

 ELB distributes traffic across servers or targets
 API Gateway is specifically for creating and managing APIs

Exam trap
If the question is about publishing and managing APIs, choose API Gateway, not ELB.

### AWS AppSync

 AppSync is mainly for GraphQL APIs
 API Gateway is for REST, HTTP, and WebSocket APIs

### Amazon CloudFront

 CloudFront is a content delivery network
 API Gateway manages API requests

They can work together, but they are not the same service.

### AWS WAF

 WAF protects web applications and APIs from common web exploits
 API Gateway manages the API itself

### Amazon Cognito

 Cognito helps with user authentication and identity
 API Gateway can use authentication methods and protect access to APIs

---

## Common exam traps

### Trap 1 Confusing API Gateway with Lambda

API Gateway does not replace Lambda.
It often sits in front of Lambda.

### Trap 2 Confusing API Gateway with ELB

If the goal is to route API calls and manage APIs, the answer is API Gateway.
If the goal is to distribute network or application traffic across servers, the answer is ELB.

### Trap 3 Thinking API Gateway is only for serverless

It is strongly used with Lambda, but it can also connect to other backend systems.

### Trap 4 Forgetting WebSocket support

API Gateway is not only for normal request-response APIs.
It can also support real-time two-way communication with WebSocket APIs.

### Trap 5 Mixing REST API and HTTP API

For Cloud Practitioner, remember this simple rule

 REST API = more features
 HTTP API = simpler and usually cheaperlower latency for common use cases

You usually do not need deep detail beyond that for the exam.

---

## Easy real-world example

Imagine a food delivery app.

The mobile app needs to

 log in users
 show restaurants
 place orders
 track order status

The app sends requests to Amazon API Gateway.
API Gateway sends each request to the right backend service or Lambda function.

So

 `restaurants` gets restaurant data
 `orders` creates an order
 `tracking` returns delivery status

API Gateway helps secure the APIs, limit traffic, and monitor usage.

---

## If I were an examiner ...

Here are the kinds of questions I would ask to test your understanding

### Question 1

Which AWS service is used to create, publish, maintain, monitor, and secure APIs

Expected answer Amazon API Gateway

### Question 2

A company wants to build a serverless backend for a mobile application. Which AWS service can expose Lambda functions as API endpoints

Expected answer Amazon API Gateway

### Question 3

Which API Gateway API type is used for real-time two-way communication such as chat apps

Expected answer WebSocket API

### Question 4

A company wants a fully managed service that acts as the front door for backend services and applications. Which AWS service should they choose

Expected answer Amazon API Gateway

### Question 5

What is the main difference between API Gateway and Elastic Load Balancing

Expected answer API Gateway is for creating and managing APIs, while ELB distributes traffic across targets.

### Question 6

A question mentions API keys, usage plans, and advanced API management. Which API Gateway type should you think about first

Expected answer REST API

---

## Final summary

Amazon API Gateway is the AWS service used to build and manage APIs.

It acts like the front door for applications and backend services.
It accepts requests from clients, applies security and traffic controls, sends requests to the correct backend, and returns responses.

For the exam, remember these big ideas

 API Gateway is for APIs
 it is commonly used with Lambda
 it supports REST, HTTP, and WebSocket APIs
 it helps with security, monitoring, and traffic control

---

## Short exam answer

Amazon API Gateway is a fully managed AWS service for creating, publishing, securing, monitoring, and managing APIs at scale.

---

## Memory trick

API Gateway = the gate for API traffic

Or even simpler

Clients knock on the gate. API Gateway decides where the request goes.

---

## One last exam coach tip

When you see words like

 create APIs
 publish APIs
 secure APIs
 monitor APIs
 front door for applications
 expose Lambda through an API
 WebSocket chat app

Your mind should quickly go to

Amazon API Gateway
