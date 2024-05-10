import math
import random
import struct
from typing import Any


def insert_random_character(s: str) -> str:
    """
    向 s 中下标为 pos 的位置插入一个随机 byte
    pos 为随机生成，范围为 [0, len(s)]
    插入的 byte 为随机生成，范围为 [32, 127]
    """
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]


def flip_random_bits(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 bitflip 与 random havoc 实现相邻 N 位翻转（N = 1, 2, 4），其中 N 为随机生成
    从 s 中随机挑选一个 bit，将其与其后面 N - 1 位翻转（翻转即 0 -> 1; 1 -> 0）
    注意：不要越界
    """
    if s == "":
        return insert_random_character(s)

    def FLIP_BITS(buf: str, index: int) -> str:
        return buf[:(index >> 3)] + chr(ord(buf[index >> 3]) ^ (128 >> (index & 7))) + buf[(index >> 3) + 1:]

    N = random.choice([1, 2, 4])
    pos = random.randint(0, len(s) * 8 - N)
    for i in range(N):
        s = FLIP_BITS(s, pos + i)
    return s


def arithmetic_random_bytes(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 arithmetic inc/dec 与 random havoc 实现相邻 N 字节随机增减（N = 1, 2, 4），其中 N 为随机生成
    字节随机增减：
        1. 取其中一个 byte，将其转换为数字 num1；
        2. 将 num1 加上一个 [-35, 35] 的随机数，得到 num2；
        3. 用 num2 所表示的 byte 替换该 byte
    从 s 中随机挑选一个 byte，将其与其后面 N - 1 个 bytes 进行字节随机增减
    注意：不要越界；如果出现单个字节在添加随机数之后，可以通过取模操作使该字节落在 [0, 255] 之间
    """
    if s == "":
        return insert_random_character(s)

    max_pow = min(math.floor(math.log2(len(s))), 2)
    p = random.randint(0, max_pow)
    N = pow(2, p)

    def ARITH_BYTES(buf: str, index: int) -> str:
        num = ord(buf[index])
        rand = random.choice([-1, 1]) * random.randint(1, 35)
        num = (num + rand + 256) % 256
        return buf[:index] + chr(num) + buf[index + 1:]

    pos = random.randint(0, len(s) - N)
    for i in range(N):
        s = ARITH_BYTES(s, pos + i)
    return s


def interesting_random_bytes(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 interesting values 与 random havoc 实现相邻 N 字节随机替换为 interesting_value（N = 1, 2, 4），其中 N 为随机生成
    interesting_value 替换：
        1. 构建分别针对于 1, 2, 4 bytes 的 interesting_value 数组；
        2. 随机挑选 s 中相邻连续的 1, 2, 4 bytes，将其替换为相应 interesting_value 数组中的随机元素；
    注意：不要越界
    """
    if s == "":
        return insert_random_character(s)

    INTERESTING8 = [-128, -1, 16, 32, 64, 100, 127]
    INTERESTING16 = [-32768, -129, 128, 255, 256, 512, 1000, 1024, 4096, 32767] + INTERESTING8
    INTERESTING32 = [-2147483648, -100663046, -32769, 32768, 65535, 65536, 100663045, 2147483647] + INTERESTING16

    max_pow = min(math.floor(math.log2(len(s))), 2)
    p = random.randint(0, max_pow)
    N = pow(2, p)

    def INTERESTING_BYTES(buf: str, index: int, N: int) -> str:
        if N == 1:
            interesting_value = random.choice(INTERESTING8)
            bytes_data = struct.pack('b', interesting_value)
            return buf[:index] + str(bytes_data) + buf[index + 1:]
        if N == 2:
            interesting_value = random.choice(INTERESTING16)
            bytes_data = struct.pack('>h', interesting_value)
            return buf[:index] + str(bytes_data) + buf[index + 2:]
        if N == 4:
            interesting_value = random.choice(INTERESTING32)
            bytes_data = struct.pack('>i', interesting_value)
            return buf[:index] + str(bytes_data) + buf[index + 4:]

    pos = random.randint(0, len(s) - N)
    s = INTERESTING_BYTES(s, pos, N)
    return s


def havoc_random_insert(s: str):
    """
    基于 AFL 变异算法策略中的 random havoc 实现随机插入
    随机选取一个位置，插入一段的内容，其中 75% 的概率是插入原文中的任意一段随机长度的内容，25% 的概率是插入一段随机长度的 bytes
    """
    return s


def havoc_random_replace(s: str):
    """
    基于 AFL 变异算法策略中的 random havoc 实现随机替换
    随机选取一个位置，替换随后一段随机长度的内容，其中 75% 的概率是替换为原文中的任意一段随机长度的内容，25% 的概率是替换为一段随机长度的 bytes
    """
    return s


class Mutator:

    def __init__(self) -> None:
        """Constructor"""
        self.mutators = [
            insert_random_character,
            flip_random_bits,
            arithmetic_random_bytes,
            interesting_random_bytes,
            # havoc_random_insert,
            # havoc_random_replace
        ]

    def mutate(self, inp: Any) -> Any:
        mutator = random.choice(self.mutators)
        return mutator(inp)
