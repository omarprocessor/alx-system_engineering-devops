# 0x17. Web Stack Debugging #3

## DevOps | SysAdmin | Scripting | Debugging

### Project Details
- **Start Date:** February 25, 2025, 6:00 AM
- **End Date:** February 27, 2025, 6:00 AM
- **Checker Release:** February 26, 2025, 1:12 PM
- **Auto Review:** At the deadline

## Concepts
For this project, you should familiarize yourself with the following concepts:
- Web Server
- Web Stack Debugging

### Background Context
When debugging, logs might not always provide sufficient information. In such cases, deeper investigation is required. The web stack in this project consists of a WordPress website running on a LAMP stack (Linux, Apache, MySQL, PHP). Your task is to identify and fix an issue causing Apache to return a `500 Internal Server Error` using `strace` and automate the solution using Puppet.

## Requirements
### General
- All files will be interpreted on **Ubuntu 14.04 LTS**
- All files should end with a new line
- A **README.md** file at the root of the project folder is **mandatory**
- Puppet manifests must pass `puppet-lint` **v2.1.1** without errors
- Puppet manifests must run **without error**
- Puppet manifests must start with a comment explaining their purpose
- Puppet manifest files must have the `.pp` extension
- Files will be checked with **Puppet v3.4**

### Installing `puppet-lint`
```sh
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```

## Tasks
### 0. Strace is your Friend (Mandatory)
#### Objective
Use `strace` to determine why Apache is returning a `500 Internal Server Error`. Once identified, fix the issue and automate the fix using Puppet.

#### Hints
- `strace` can attach to a currently running process
- You can use `tmux` to run `strace` in one window and `curl` in another

#### Requirements
- **File:** `0-strace_is_your_friend.pp`
- Must contain Puppet code
- Use any Puppet resource type to implement the fix

#### Example
```sh
root@server:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
root@server:~# puppet apply 0-strace_is_your_friend.pp
Notice: Finished catalog run successfully
root@server:~# curl -sI 127.0.0.1
HTTP/1.1 200 OK
```

## Repository Structure
- **GitHub Repository:** `alx-system_engineering-devops`
- **Project Directory:** `0x17-web_stack_debugging_3`
- **Main File:** `0-strace_is_your_friend.pp`

Ensure your Puppet script properly fixes the issue, allowing Apache to serve the WordPress site correctly.
