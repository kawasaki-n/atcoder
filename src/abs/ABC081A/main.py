#!/usr/bin/env python3


# Generated by 2.3.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    value = next(tokens)

    ret = 0
    if(value[0] == "1"):
        ret += 1
    if(value[1] == "1"):
        ret += 1
    if(value[2] == "1"):
        ret += 1
    
    print(ret)

if __name__ == '__main__':
    main()