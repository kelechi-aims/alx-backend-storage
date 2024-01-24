# 0x02. Redis basic

- **Category:** Back-end
- **By** Emmanuel Turlay, Staff Software Engineer at Cruise
- **Weight:** 1

## Resources

### Read or watch:

- [Redis commands](https://intranet.alxswe.com/rltoken/lQ8ANhVfxDTxDr2UDSyQRA)
- [Redis python client](https://intranet.alxswe.com/rltoken/imfgFhAZPlg7YMZ_tHvFZw)
- [How to Use Redis With Python](https://intranet.alxswe.com/rltoken/7SluvFvgckwVgsvrfOf1CQ)
- [Redis Crash Course Tutorial](https://intranet.alxswe.com/rltoken/hJVo3XwMMFFoApyX8zPXvA)

## Learning Objectives

- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
