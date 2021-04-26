def isalpha(in1):
    for c in in1:
        if not ((ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z'))):
            return False
    return True


def isdigit(in1):
    for c in in1:
        if not (ord('0') <= ord(c) <= ord('9')):
            return False
    return True


def isalnum(in1):
    for c in in1:
        if not (ord('0') <= ord(c) <= ord('9') or (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z'))):
            return False
    return True


def lencmp(in1, in2):
    if len(in1) == len(in2):
        return 0
    elif len(in1) > len(in2):
        return 1
    else:
        return -1


def tolower(in1):
    res=""
    for c in in1:
        if ord('A') <= ord(c) <= ord('Z'):
            res+=chr(ord('a') + ord(c) - ord('A'))
        else:
            res+=c
    return res


def strcmp(in1, in2):
    in1 = tolower(in1)
    in2 = tolower(in2)
    s = len(in1)
    if len(in1) > len(in2):
        s = len(in2)
    for i in range(s):
        if in1[i]>in2[i]:
            return 1
        if in1[i]<in2[i]:
            return -1
    if len(in1) == len(in2):
        return 0
    elif len(in1) > len(in2):
        return 1
    else:
        return -1