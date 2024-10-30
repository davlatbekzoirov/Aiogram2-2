from typing import Any, Callable, Awaitable, Dict
import asyncpg
from asyncpg import Record

class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector