#!/usr/bin/python3
i = len(argv)
if i == 0:
    print('{} argument.'.format(i))
if i == 1:
    print('{} argument:'.format(i))
else:
    print('{} arguments:'.format(i))
    for j in range(1, i):
        print('{}: {}'.format(j, argv[j]))

