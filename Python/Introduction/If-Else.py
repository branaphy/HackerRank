#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")

else:
    if n < 6:
        print("Not Weird")
    elif n < 21:
        print("Weird")
    else:
        print("Not Weird")
