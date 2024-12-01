#Overview
This README outlines a secured three-server web infrastructure for hosting www.foobar.com. The setup includes firewalls, HTTPS encryption, and monitoring for performance tracking and issue resolution.

Design
Components
Load Balancer: Distributes traffic across servers and terminates SSL.
3 Firewalls: Protect load balancer, web server, and database from unauthorized access.
SSL Certificate: Ensures traffic is encrypted and served over HTTPS for security.
Monitoring Clients: Collects data for analyzing performance and diagnosing issues.
3 Servers:
Web Server (Nginx): Handles HTTP requests and serves static files.
Application Server: Manages dynamic content and queries the database.
Database (MySQL): Stores and retrieves data for the application.
Workflow
User accesses www.foobar.com via HTTPS.
DNS resolves the domain to the load balancer.
The load balancer forwards the encrypted traffic to the web server.
The web server processes requests, interacts with the application server, and queries the database as needed.
Monitoring tools collect performance data.
Explanations
Additional Elements:

Firewalls: Protect each layer of the infrastructure.
SSL: Encrypts traffic, ensuring data security.
Monitoring: Tracks metrics like QPS, CPU usage, and database queries.
Firewalls:

Block unauthorized access and prevent malicious attacks.
HTTPS Traffic:

Encrypts communication between the user and server, ensuring confidentiality and integrity.
Monitoring:

Identifies issues, optimizes performance, and tracks server health.
Data is collected using agents or log shipping to tools like Sumologic.
Web Server QPS Monitoring:

Configure monitoring to track requests per second (QPS) via server logs or load balancer metrics.
Issues
SSL Termination at Load Balancer:

Unencrypted traffic between load balancer and servers can be intercepted.
Single MySQL Server:

A single point of failure for write operations; limits scalability.
Servers with Same Components:

Resource contention; lack of specialization can lead to performance issues.
