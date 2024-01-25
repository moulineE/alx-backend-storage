# Project 0x02. Redis Basic

## Back-end - Redis

**By:** Emmanuel Turlay, Staff Software Engineer at Cruise

**Weight:** 1

**Project Start:** Jan 24, 2024 4:00 AM

**Project End:** Jan 25, 2024 4:00 AM

**Checker Released:** Jan 24, 2024 10:00 AM

**Auto Review:** Will be launched at the deadline

### Resources
- [Redis commands](https://redis.io/commands)
- [Redis python client](https://pypi.org/project/redis/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.tutorialspoint.com/redis/index.htm)

### Learning Objectives
- Learn how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

### Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7).
- All files end with a new line.
- A mandatory README.md file at the root of the project folder.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Code should use the `pycodestyle` style (version 2.5).
- All modules, classes, functions, and methods should have documentation.
- Documentation should be meaningful sentences explaining the purpose of the module, class, or method.
- Functions, coroutines, and methods must be type-annotated.
- Redis should be installed on Ubuntu 18.04 using the provided commands.
- Use Redis in a container by starting it with `service redis-server start`.

### Tasks

#### 0. Writing strings to Redis
- Create a `Cache` class.
- In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`), and flush the instance using `flushdb`.
- Create a `store` method that takes a data argument and returns a string. The method should generate a random key (e.g., using uuid), store the input data in Redis using the random key, and return the key.

Example:

```python
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

#### 1. Reading from Redis and recovering the original type
- Create a `get` method that takes a key string argument and an optional Callable argument named `fn`.
- `fn` is a callable used to convert the data back to the desired format.
- Implement two new methods: `get_str` and `get_int` that automatically parametrize `Cache.get` with the correct conversion function.

Example:

```python
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

#### 2. Incrementing values
- Implement a `count_calls` decorator that takes a single method Callable argument and returns a Callable.
- Use the qualified name of the method using the `__qualname__` dunder method as a key.
- Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.
- Decorate `Cache.store` with `count_calls`.

Example:

```python
Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

#### 3. Storing lists
- Implement a `call_history` decorator to store the history of inputs and outputs for a particular function.
- Use the decorated function’s qualified name to create input and output list keys.
- Decorate `Cache.store` with `call_history`.

Example:

```python
Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

#### 4. Retrieving lists
- Implement a `replay` function to display the history of calls of a particular function.
- Use keys generated in previous tasks to generate the required output.

Example:

```python
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
# Output:
# Cache.store was called 3 times:
# Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
# Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
# Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
```

**GitHub Repository:** [alx-backend-storage](https://github.com/moulineE/alx-backend-storage)

**Directory:** 0x02-redis_basic

**File:** exercise.py