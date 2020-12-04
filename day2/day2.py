import sys
import re


def valid1(line):
    m = re.match(r"(\d+)-(\d+) (.): (.*)", line)
    a, b, char, string = m.groups()

    a = int(a)
    b = int(b)

    return a <= len([c for c in string if c == char]) <= b


def valid2(line):
    m = re.match(r"(\d+)-(\d+) (.): (.*)", line)
    a, b, char, string = m.groups()

    a = int(a)
    b = int(b)

    return (string[a - 1] == char) != (string[b - 1] == char)


lines = [line.strip() for line in sys.stdin.readlines()]

print(len([line for line in lines if valid1(line)]))
print(len([line for line in lines if valid2(line)]))
