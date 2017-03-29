def create_alpha(c):
    '''生成26个小写字母

    Args:
        c: 一个字符，l表示返回列表，s表示返回字符串

    Return:
        包含26个小写字母的列表或字符串
    '''
    if c == 'l':
        return [chr(i) for i in range(97, 123)]
    elif c == 's':
        return ''.join([chr(i) for i in range(97, 123)])
    else:
        return 'Invalid argument.'

def create_digital(c):
    '''生成0-9是个数字

    Args:
        一个字符，l表示返回列表，s表示返回字符串

    Return:
        包含0-9的列表或字符串
    '''
    if c == 'l':
        return [str(i) for i in range(10)]
    elif c == 's':
        return ''.join(create_digital('l'))
    else:
        return 'Invalid argument.'

def create_words(c1):
    '''生成字母和数字

    Args:
        :c1: 一个字符，b表示大写字母，s表示小写字母，a表示大小写字母
    Return:
        包含可选字母和数字的列表
    '''
    if c1 == 'b':
        req = []
        temp = create_alpha('l')
        for i in range(len(temp)):
            req.append(temp[i].upper())
        return req + create_digital('l')
    elif c1 == 's':
        return create_alpha('l') + create_digital('l')
    elif c1 == 'a':
        req = []
        temp = create_alpha('l')
        for i in range(len(temp)):
            req.append(temp[i].upper())
        return req + create_alpha('l') + create_digital('l')

def create_str(c):
    if c == 'w':
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',
                '2', '3', '4', '5', '6', '7', '8', '9', '_']

    elif c == 'd':
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    elif c == 'b':
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    elif c == 's':
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    elif c == 'sd':
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
                '1', '2', '3', '4', '5', '6', '7', '8', '9']

    elif c == 'bd':
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0',
                '1', '2', '3', '4', '5', '6', '7', '8', '9']

    else:
        return 'Invalid argument'