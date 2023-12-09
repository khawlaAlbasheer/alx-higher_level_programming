#!/usr/bin/python3
if __name__ == "__main__":
    import sys
        i = len(sys.argv)
        if i >= 1:
            for arg in sys.argv:
                result += int(arg)
    print(result)
