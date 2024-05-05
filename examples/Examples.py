import math


def example1(s: str):
    number = float(s)
    r1 = 1 - number
    r2 = r1 / number
    if r1 <= r2:
        example1(str(r2 + 1))
    else:
        temp = s[int(r1)].join(str(r2))


def example2(s: str):
    temp = """%d. {Key} is """
    r = s.split(".")
    temp += r[1]
    temp = temp.format(Key=r[0])
    temp = temp % len(s)

    def can_convert_to_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    if can_convert_to_int(r[0]):
        temp += str(math.sqrt(int(r[0])))


def example3(s: str):
    if s[0] == 'F':
        if s[1] == 'D':
            if s[2] == 'U':
                t = (ord(s[4]) - 65) / (ord(s[3]) - 80)
                if t != 0:
                    index = s.index("L")
                    assert s[index + 1] == 'A'
                    if not s[index + 2:].startswith('B'):
                        raise RuntimeError
