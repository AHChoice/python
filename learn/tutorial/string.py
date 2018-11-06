# -*- coding:utf-8 -*-

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
    food = 'spam', adjective = 'absolutely horrible'))
print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred',
    other = 'Georg'))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1415926'.zfill(5))
print('3.1315926'.ljust(5)[:5])
print('3.1315926'.ljust(5))


