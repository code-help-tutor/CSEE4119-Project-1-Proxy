# CSEE4119 F24 Project 1 Preliminary Stage

## 0. Deadlines and Updates
- Preliminary Stage Due: October 9th, 11:59pm

## 1. Overview
### 1.1 In the Real World
- Clients issue DNS query to resolve domain name to IP address of content server in a CDN.
- CDN's DNS server selects best content server based on client's IP and server load.
- Client requests video chunks encoded at multiple bitrates and selects bitrate based on throughput and buffer.
### 1.2 Your System
- Entire system runs on one host with a network simulator (netsim).
- Use a VM for development and testing.
- Components:
  - Browser: Use an off-the-shelf web browser to play videos.
  - Proxy: Implement adaptive bitrate selection in an HTTP proxy.
  - Web Server: Video content served from an off-the-shelf web server (Apache).
### 1.3 Groups and collaboration policy
- Individual project.
- Can discuss at a conceptual level with others and consult Internet material (except Python proxy implementations).
- Final code and configuration must be your own.

## 2. Preliminary stage
### 2.1 Requirements
- Implement a proxy that forwards messages between client and server.
- VM is required for final stage but not preliminary stage.
### 2.2 Get your connections right
- Accept connections from clients and open a connection with a server.
- Steps:
  - Establish a connection with a client: Listen on a specified port for client connections.
  - Establish a connection with a server: Connect to the server using the provided IP and port 8080.
### 2.3 Forwarding protocol
- Messages have a body and an End Of Message (EOM) symbol (\n).
- Proxy waits for a message from the client and then a response from the server before forwarding.
### 2.4 Running the proxy
- Create an executable Python script called `proxy` in the proxy directory.
- Invoke it with `listen-port`, `fake-ip`, and `server-ip` as arguments.
### 2.5 Test it out!
- Use the netcat tool to test the proxy implementation.
### 2.6 Final result
- Proxy should forward messages of any length and support back-and-forth messages until connection is closed.
### 2.7 What to Submit for preliminary stage
- Submit a zipped file named `<yourUNI>.zip` with a `handin` directory containing:
  - `proxy` directory with source code and an executable named `proxy`.
### 2.8 Where to Submit
- Submit to Gradescope.

## 3. Final stage: Video Bitrate Adaptation
- Details to be released later.

## 4. Development Environment
### 4.1 Virtual Machine
- Provided on GCP.
- Follow tutorial to set up and do testing.
- Options for moving files between VM and computer.
### 4.2 Starter Files (for final stage)
- Details to be released later.
### 4.3 Network Simulation (for final stage)
- Details to be released later.
### 4.4 Apache
- Details to be released later.
### 4.5 Programming Language and Packages
- Use Python 3 (version 3.10.12 on VM).
- Allowed packages: `sys`, `socket`, `threading`, `select`, `time`, `re`, `numpy`, `subprocess`.

## 5. Grading
### Components:
- Proxy (70 points):
  - Preliminary stage proxying [15 pts]
  - Final stage proxying runs on browser [10 pts]
  - Final stage proxy - implementing EWMA throughput estimator & bitrate adaptation [35 pts]
  - DNS Server - correct responses and implementation of web server selection [10 pts]
  - Code executes as instructed [-10 pts if we have to manually debug things]
- Writeup (20 points):
  - Plots of utilization, fairness, and smoothness for [10 pts] α ∈ {0.1, 0.5, 0.9}
  - Discussion of tradeoffs for varying [10 pts] α
- Style (10 points):
  - Code thoroughly commented
  - Code organized and modular
  - README listing your files and what they contain

## Academic integrity
- Zero tolerance on plagiarism.
- Follow Columbia University and department policies.
- Individual assignment, no sharing or using external code without permission.
- No use of AI-assisted coding tools.

# CSEE4119 Project 1 Proxy

# CS Tutor | 计算机编程辅导 | Code Help | Programming Help

# WeChat: cstutorcs

# Email: tutorcs@163.com

# QQ: 749389476

# 非中介, 直接联系程序员本人
