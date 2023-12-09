#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    i = len(sys.argv)
    for j in range(1, i):
        result += int(sys.argv[j])
    print(result)
