#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import count
from operator import index


list = [50, 65, 80, 95, 110, 125,]
count=0
for i in list:
    if i%10 == 0:
        count += 1
for i in list:
    if i%10 == 0:
        large = (list.index(i))
        print("индекс элементf", large)
print("кол-во элементов списка, удовлетворяющих заданному условию: ", count)
