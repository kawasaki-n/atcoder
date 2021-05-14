#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    x = 0
    y = 0
    turnX = True
    for i in sorted(a, reverse=True):
        if turnX:
            x += i
        else:
            y += i
        turnX = not(turnX)

    print(x - y)
    return


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()