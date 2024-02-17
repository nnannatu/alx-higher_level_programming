**Field,Value**
**Project Dates**,Feb 14, 2024, 6:00 AM, to Feb 15, 2024, 6:00 AM
**Auto QA Review**,0.0/96 mandatory & 0.0/24 optional
**Resources**,Refer to the provided list for detailed readings and tutorials.
**Allowed Editors**,vi, vim, emacs
**Environment**,Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
**File Endings**,All files should end with a new line.
**SQL Queries**,Include comments just before each query.
**SQL Keywords**,Should be in uppercase (SELECT, WHERE, etc.)
**README.md**,Mandatory at the root, describing the tasks.
**Setup Instructions**,"1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
$ sudo apt update
$ sudo apt install mysql-server

2. Connect to MySQL server:
$ sudo mysql

3. Start MySQL in a container:
$ service mysql start

4. To list databases in the container:
$ cat 0-list_databases.sql | mysql -uroot -p

5. Import a SQL dump example:
$ echo ""CREATE DATABASE hbtn_0d_tvshows;"" | mysql -uroot -p
$ curl ""https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql"" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo ""SELECT * FROM tv_genres"" | mysql -uroot -p hbtn_0d_tvshows"

**Learning Objectives**,"- Create a new MySQL user.
- Manage privileges for a user on a database or table.
- Understand and use PRIMARY KEY and FOREIGN KEY.
- Implement NOT NULL and UNIQUE constraints.
- Retrieve data from multiple tables in a single query.
- Work with subqueries, JOIN, and UNION operations."

