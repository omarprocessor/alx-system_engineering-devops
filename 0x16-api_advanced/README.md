0x16. API Advanced

Description

This project focuses on making advanced API requests using Python, specifically with the Reddit API. The goal is to practice working with RESTful APIs, handling JSON responses, and implementing recursive functions for pagination. These skills are useful in technical interviews and real-world applications.

Learning Objectives

By the end of this project, you should be able to:

Read and interpret API documentation to find relevant endpoints.

Use an API with pagination effectively.

Parse and manipulate JSON results from an API response.

Implement recursive API calls.

Sort dictionary values efficiently.


Requirements

Allowed editors: vi, vim, emacs

Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)

Files must end with a new line

First line of all scripts: #!/usr/bin/python3

Imported libraries must be alphabetically ordered

Follow PEP 8 style

All files must be executable

Files will be tested with wc

Modules must have documentation (python3 -c 'print(__import__("module_name").__doc__)')

Use the Requests module for making HTTP requests


Tasks

0. How many subs?

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, return 0.

Prototype: def number_of_subscribers(subreddit)

Invalid subreddits should return 0

Do not follow redirects

File: 0-subs.py


Example:

$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0


---

1. Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

Prototype: def top_ten(subreddit)

If invalid subreddit, print None

Do not follow redirects

File: 1-top_ten.py


Example:

$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
...


---

2. Recurse it!

Write a recursive function that queries the Reddit API and returns a list of all hot post titles for a given subreddit.

Prototype: def recurse(subreddit, hot_list=[])

If invalid subreddit, return None

Must use recursion (loops are not allowed)

Do not follow redirects

File: 2-recurse.py


Example:

$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None

Repository Structure

alx-system_engineering-devops
└── 0x16-api_advanced
    ├── 0-subs.py
    ├── 1-top_ten.py
    ├── 2-recurse.py
    ├── README.md

Author

# Omar Abdirashid  Mohumed
