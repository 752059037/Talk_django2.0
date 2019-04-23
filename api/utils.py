# 创建人;Ye
# 创建时间 : 19.4.18  10:39


def is_ascii(x):
    """
    判断一个字符串是否为常规的ascii码组成
    :param x:iterable
    :return: 布尔值
    """
    return all([32 < ord(i) < 127 for i in x])
