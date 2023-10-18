import asyncio
from functools import wraps, partial


def async_wrap(func):
    """
    异步装饰器，用于把同步方法转为异步
    :param func:
    :return:
    """
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        func_ = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, func_)

    return run
