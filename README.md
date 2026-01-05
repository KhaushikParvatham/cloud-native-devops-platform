# Cloud-Native DevOps Platform (AWS, EKS)

## Overview
This project implements an end-to-end **cloud-native DevOps platform** that demonstrates how modern applications are provisioned, deployed, and operated on AWS using **containerization, Kubernetes, CI/CD, and Infrastructure as Code**.

The objective of this project is to design a **reproducible, automated, and production-aligned deployment workflow**, rather than simply deploying an application.

---

## Problem Statement
Traditional application deployments often suffer from:

- Manual and error-prone infrastructure provisioning
- Inconsistent environments across development and production
- Deployment downtime during releases
- Tight coupling between infrastructure and application changes
- Limited reproducibility and auditability

This project addresses these challenges by building a **fully automated DevOps pipeline** that provisions infrastructure, builds container images, deploys applications to Kubernetes, and supports **safe, zero-downtime updates**.

---

## Architecture Overview
The platform is built using the following high-level components:

### Cloud Infrastructure
- AWS Virtual Private Cloud (VPC) for isolated networking
- Amazon EKS as the managed Kubernetes control plane
- Amazon ECR for container image storage

### Application Runtime
- Containerized application running on Kubernetes
- Kubernetes Deployment for lifecycle management
- Kubernetes Service for internal traffic routing

### CI/CD Pipeline
- GitHub Actions for continuous integration and delivery
- Automated build, image tagging, and deployment workflow

### Infrastructure as Code
- Terraform used to provision and manage AWS infrastructure

---

## Key Design Decisions

### Infrastructure as Code with Terraform
**Why**
- Manual infrastructure setup is not repeatable or auditable.
- Infrastructure should be version-controlled and reproducible.

**What was implemented**
- AWS resources including VPC, subnets, security groups, and EKS cluster were provisioned using Terraform.
- Infrastructure can be created or destroyed consistently using declarative configuration.

---

### Containerization and Kubernetes (Amazon EKS)
**Why**
- Containers ensure application consistency across environments.
- Kubernetes provides scalability, resilience, and controlled deployments.

**What was implemented**
- Application packaged as a Docker image.
- Amazon EKS used to orchestrate containerized workloads.
- Kubernetes Deployments and Services manage application lifecycle and networking.

---

### CI/CD with GitHub Actions
**Why**
- Manual deployments increase risk and slow down delivery.
- CI/CD ensures repeatable and automated deployments.

**What was implemented**
- GitHub Actions pipeline that:
  - Builds Docker images on every change
  - Pushes images to Amazon ECR
  - Deploys updated images to the EKS cluster

---

### Zero-Downtime Deployment Strategy
**Why**
- Production services should remain available during deployments.
- Downtime during releases impacts reliability and user experience.

**What was implemented**
- Kubernetes rolling updates were used.
- New pods are created and become healthy before old pods are terminated.
- At least one healthy replica remains available at all times.

This provides **practical zero-downtime deployments** without complex traffic routing mechanisms.

---

## Deployment Flow
1. Code is pushed to the GitHub repository.
2. GitHub Actions pipeline is triggered.
3. Docker image is built and tagged.
4. Image is pushed to Amazon ECR.
5. Kubernetes Deployment updates the running application on EKS.
6. Rolling update ensures uninterrupted service availability.

---

## Technologies Used
- AWS: EKS, ECR, VPC, IAM
- Infrastructure as Code: Terraform
- Containers: Docker
- Orchestration: Kubernetes
- CI/CD: GitHub Actions

---

## What This Project Demonstrates
- Designing cloud infrastructure using Infrastructure as Code
- Running containerized workloads on a managed Kubernetes service
- Building automated CI/CD pipelines
- Deploying applications with zero downtime
- Applying production-oriented DevOps practices

---

## Future Improvements
- Introduce GitOps-based deployments using Argo CD
- Add observability using Prometheus and Grafana
- Implement blue-green or canary deployment strategies
- Integrate security scanning into the CI/CD pipeline
