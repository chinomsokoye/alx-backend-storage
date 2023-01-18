Curriculum <br>
**Short Specializations** <br>

# 0x02. Redis basic

`Back-end` `Redis` `Database`

## Resources

**Read or watch:**

* [Redis commands](https://www.redis.io/commands/)
* [Redis python client](https://www.redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://www.realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Requirement

* Files intrepreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `redis` (version 4.0.9)
* Files must end with a new line
* The first line of files should be exactly `#!/usr/bin/env python3`
* Code should use the `pycodestyle` style (Version 2.5.*)
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* All functions and coroutines should be type-annotated
* Mandatory `README.md` file

## Install Redis on Ubuntu 18.04

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Use Redis in a Container

Redis server is stopped by default - when starting a container, you should start with: `service redis-server start` <br>

## Finally...
