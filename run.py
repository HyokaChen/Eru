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
from asyncio.events import AbstractEventLoop
from watchdog.observers import Observer
from configs.constant import TEMPLATE_PATH
from core.engine import Eru

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except Exception:
    print("Not support uvloop.")


async def main():
    pass


if __name__ == '__main__':
    loop: AbstractEventLoop = asyncio.get_event_loop()
    # 监听文件变动
    ob = Observer()
    try:
        eru = Eru()
        ob.schedule(eru, TEMPLATE_PATH, True)
        ob.start()
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
        ob.stop()
        ob.join()
    finally:
        loop.close()
        ob.join()
        # self.logger.info(Colored.yellow("[Liz2Bird]: Shut down....(@ $ _ $ @)----"))
