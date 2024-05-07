# Reddit API Project

This project aims to develop Python scripts that interact with the Reddit API to perform various tasks. Below are the details of the tasks involved, along with the requirements and instructions for each task.


## Background Context

APIs are frequently encountered in interviews and real-world applications. This project focuses on utilizing the Reddit API for practice. The Reddit API offers a range of endpoints, making it suitable for learning how to work with APIs, including handling pagination, parsing JSON responses, making recursive calls, and sorting data.

## Resources

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives

Upon completion of this project, participants should be able to:

- Navigate API documentation to find relevant endpoints
- Utilize APIs with pagination
- Parse JSON responses from APIs
- Implement recursive API calls
- Sort dictionary data by value

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- Files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Libraries must be alphabetically organized
- A `README.md` file at the root of the project folder is mandatory
- Code should adhere to PEP 8 style
- All files must be executable
- File lengths will be tested using `wc`
- Modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use the Requests module for HTTP requests to the Reddit API

## Tasks

### 0. How many subs? (mandatory)

- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0

### 1. Top Ten (mandatory)

- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None

### 2. Recurse it! (mandatory)

- Prototype: `def recurse(subreddit, hot_list=[])`
- If not a valid subreddit, return None

### 3. Count it! (advanced)

- Prototype: `def count_words(subreddit, word_list)`
- If no posts match or the subreddit is invalid, print nothing


