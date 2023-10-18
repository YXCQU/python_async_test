import requests

from utils.wrap import async_wrap


def get_data(params):
    """
    模拟请求
    :param params:
    :return:
    """
    p = params
    # 解析参数等
    url1 = "http://127.0.0.1:5000/api"
    response = None
    try:
        response = requests.get(url=url1)
        print(f'请求中 参数: {p}')
    except:
        # 处理
        pass
    return response


@async_wrap
def async_get_data(params):
    """
    添加装饰器，异步模拟请求
    :param params:
    :return:
    """
    p = params
    # 解析参数等
    url1 = "http://127.0.0.1:5000/api"
    response = None
    try:
        response = requests.get(url=url1)
        print(f'请求中 参数: {p}')
    except:
        # 处理
        pass
    return response
