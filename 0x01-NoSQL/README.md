# Project: NoSQL

### Overview

This project focuses on NoSQL databases, specifically MongoDB, within the context of back-end development. The project is developed by Emmanuel Turlay, Staff Software Engineer at Cruise, and Guillaume, CTO at Holberton School.

**Weight:** 1

**Project Duration:** January 22, 2024, 6:00 AM - January 24, 2024, 6:00 AM

**Checker Release:** January 22, 2024, 6:00 PM

**Auto Review Deadline:** Deadline


## Learning Resources

- [NoSQL Databases Explained](https://intranet.alxswe.com/rltoken/wweK7dOY4pf8haCqv9Iv6Q)
- [What is NoSQL?](https://intranet.alxswe.com/rltoken/QqqNmgzgwopHBv305ki6bg)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://intranet.alxswe.com/rltoken/RyyP9OH1EMBWWYpTs4TqoA)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://intranet.alxswe.com/rltoken/9__3tR-NimgXlmjPQwTF-Q)
- [Aggregation](https://intranet.alxswe.com/rltoken/ziEDeniRobC6owPE1_avAQ)
- [Introduction to MongoDB and Python](https://intranet.alxswe.com/rltoken/axwwF4CjO7FnK8Ecochqnw)
- [mongo Shell Methods](https://intranet.alxswe.com/rltoken/lUqnLwOHbbp9FK39ijNmDQ)
- [The mongo Shell](https://intranet.alxswe.com/rltoken/ZKAjSTq5ScfsUVhk_8DeFA)

## Learning Objectives

Upon completing this project, you should be able to explain the following concepts without relying on external resources:

### General

1. What NoSQL means
2. Difference between SQL and NoSQL
3. ACID principles
4. Document storage
5. NoSQL types
6. Benefits of a NoSQL database
7. Querying information from a NoSQL database
8. Inserting, updating, and deleting information from a NoSQL database
9. Using MongoDB

## Installation Guide: MongoDB 4.2 in Ubuntu 18.04

Follow these steps to install MongoDB 4.2 on Ubuntu 18.04:

```bash
# Import MongoDB GPG Key
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -

# Add MongoDB Repository
echo "deb [arch=amd64,arm64] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list

# Update Package List
sudo apt-get update

# Install MongoDB
sudo apt-get install -y mongodb-org

# Check MongoDB Status
sudo service mongod status

# Verify MongoDB Shell Version
mongo --version

# Install pymongo
pip3 install pymongo

# Verify pymongo Version
python3
import pymongo
print(pymongo.__version__)

# Potential Issue Resolution (Data directory not found)
sudo mkdir -p /data/db
