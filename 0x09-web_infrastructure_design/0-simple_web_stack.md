0x09. Web Infrastructure Design
Overview
This README outlines a one-server web infrastructure to host www.foobar.com, highlighting its components, functionality, and potential issues.

Design
Components
1 Server: Hosts all services.
Web Server (Nginx): Handles HTTP/HTTPS requests.
Application Server: Processes dynamic requests.
Application Files: Website's codebase.
Database (MySQL): Stores data.
Domain Name: Maps www.foobar.com to IP 8.8.8.8 using an A record.
Workflow
User Request: User enters www.foobar.com in a browser.
DNS Resolution: DNS maps the domain to 8.8.8.8.
Web Server: Nginx serves static files or forwards requests to the application server.
Application Server: Processes logic and queries the database.
Response: Data is returned to the user via Nginx.
Key Points
Server: A computer hosting all services.
Domain Name: Provides a user-friendly address.
DNS Record: A record links the domain to the server’s IP.
Web Server: Handles requests and serves files.
Application Server: Processes requests and interacts with the database.
Database: Manages persistent data.
Communication: Server and user communicate via HTTP/HTTPS.
Issues
Single Point of Failure (SPOF): Server failure makes the website inaccessible.
Downtime: Server restarts cause interruptions.
Scalability: Cannot handle high traffic.
