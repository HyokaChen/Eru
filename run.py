#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 @File       : run.py
 @Time       : 2021/2/12 12:47
 @Author     : Empty Chan
 @Contact    : chen19941018@gmail.com
 @Description:
 @License    : (C) Copyright 2016-2021, iFuture Corporation Limited.
"""
import sys
import asyncio
from envparse import env

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except Exception:
    print("Not support uvloop.")


def read_config():
    print("read configuration")
    env.read_envfile('~/.env')


async def main():
    pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        tasks = list(asyncio.Task.all_tasks(loop))
        pendings = {t for t in tasks if not t.done()}
        for task in pendings:
            task.cancel()
        loop.run_until_complete(
            asyncio.gather(*pendings, loop=loop, return_exceptions=True))

        for task in pendings:
            if task.cancelled():
                continue
            if task.exception() is not None:
                loop.call_exception_handler({
                    'message': 'unhandled exception during asyncio.run() shutdown',
                    'exception': task.exception(),
                    'task': task,
                })

        if sys.version_info >= (3, 6):  # don't use PY_36 to pass mypy
            loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()
        # self.logger.info(Colored.yellow("[Liz2Bird]: Shut down....(@ $ _ $ @)----"))
