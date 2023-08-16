#!/usr/bin/env python3

import redis
import uuid

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        self.key = str(uuid.uuid4())
        self._redis.store(key, data)
        return self.key
