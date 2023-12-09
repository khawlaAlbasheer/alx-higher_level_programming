#!/usr/bin/python3
if __name__ == "__main__":
    impport sys
    i = len(sys.argv) - 1
    
    if i == 0:
        print('{} arguments.'.format(i))
    elif i == 1:
        print('{} argument:'.format(i))
    else:
        print('{} arguments:'.format(i))
        for j in range(1, i):
            print('{}: {}'.format(j, argv[j]))

