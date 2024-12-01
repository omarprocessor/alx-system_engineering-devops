#Overview
This README outlines a three-server web infrastructure for hosting www.foobar.com, highlighting its components, functionality, and potential issues.

Design
Components
Load Balancer (HAProxy): Distributes traffic between servers.
Algorithm: Round-robin for balanced request distribution.
Setup: Active-Active for load-sharing.
2 Servers:
Web Server (Nginx): Serves static content and proxies dynamic requests.
Application Server: Processes dynamic requests and queries the database.
Database (MySQL):
Primary-Replica Cluster: Primary node handles writes; Replica node syncs and handles reads.
Application Files: Shared codebase across servers.
Workflow
User requests www.foobar.com via the domain.
DNS resolves the domain to the load balancer.
Load balancer distributes requests to servers.
Web and application servers handle logic and database queries.
Database returns data, served back to the user.
Issues
SPOF: Load balancer is critical.
Security: No HTTPS or firewalls.
No Monitoring: Lack of performance insights.

