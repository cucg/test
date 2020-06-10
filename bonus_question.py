# 附加题

def compare():
    # 获取用户输入
    version1 = input('version1:')
    version2 = input('version2:')
    # 转换为list
    version1 = version1.split('.')
    version2 = version2.split('.')
    # 使两个版本号长度保持一致
    while True:
        if len(version1) == len(version2):
            break
        if len(version1) > len(version2):
            version2.append('0')
        if len(version1) < len(version2):
            version1.append('0')
    # 去除前导零并将列表转换成数字int类型
    version1 = int(''.join([str(int(i)) for i in version1]))
    version2 = int(''.join([str(int(x)) for x in version2]))
    # 比较
    if version1 > version2:
        return 1
    elif version1 < version2:
        return -1
    else:
        return 0


if __name__ == "__main__":
    while True:
        print(compare())
