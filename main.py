import asyncio

from utils.parse_tool import parse_data
from utils.request_tools import get_data, async_get_data


def main_do_sth():
    """
    总的调用处理模块，负责核心调度
    :return:
    """
    # ----------写法1 不加async-----------------------
    # 请求数据
    data1 = get_data("同步请求")
    if not data1:
        # 异常处理
        print("请求异常")

    # -------------写法2 async异步--------------------
    print('异步发请求中......')
    loop = asyncio.get_event_loop()
    data2 = loop.run_until_complete(async_get_data('方法2'))

    # -------------写法3 异步并发请求--------------------
    print('高并发请求中......')
    loop = asyncio.get_event_loop()
    params = range(10)  # 可以换成参数列表
    tasks = [async_get_data(x) for x in params]
    data_list = loop.run_until_complete(asyncio.gather(*tasks))
    print(f'异步请求数据列表 {data_list}')
    # --------------------------------------------------
    # 解析数据
    result = parse_data(data1)
    # print(result)
    return result


if __name__ == '__main__':
    main_do_sth()
