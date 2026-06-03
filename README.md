# AWS Network Logic Simulator (Python)

This project simulates AWS networking logic using Python, focusing on **reachability, routing decisions, and Transit Gateway behavior**.

It is designed to mimic **real-world cloud networking challenges** such as:
- Determining if two subnets can communicate
- Evaluating route table decisions
- Understanding Transit Gateway attachment and routing logic
- Troubleshooting network connectivity in distributed cloud environments

---

## 🚀 Why this project matters

In large-scale cloud environments, network engineers must:

- Debug connectivity issues quickly
- Understand complex routing flows
- Automate validation of network paths
- Reduce manual troubleshooting

This repository demonstrates how those problems can be **modeled and solved programmatically**.

---

## 🧠 Key Features

### ✅ Reachability Engine
Simulates whether traffic can flow between subnets based on:
- Route tables
- CIDR matching
- Target resources (IGW, NAT, TGW)

### ✅ Transit Gateway Logic
Evaluates:
- TGW attachments
- Cross-VPC routing
- Inter-VPC connectivity paths

### ✅ Object Search Utilities
Efficient lookup of AWS-like resources using IDs

---

## 🏗️ Architecture Concept

The project models:

- VPCs
- Subnets
- Route Tables
- Transit Gateways
- Attachments

This allows simulation of **multi-VPC communication patterns**, similar to production cloud architectures.

---

## 📂 Project Structure
