from typing import Any, Callable, Awaitable, Dict
import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from core.utils.dbconnect import Request

class Dbsession(BaseMiddleware):
    def __init__(self, connector: asyncpg.pool.Pool):
        super().__init__()
        self.connector = connector

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                data['request'] = Request(conn)
                return await handler(event, data)