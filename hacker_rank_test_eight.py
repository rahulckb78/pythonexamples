import numpy as np
from itertools import permutations
def permutation_of_arrays(x,y,z,n):
    arr_nums = np.arrange(n).reshape(x,y,z)
    arr_nums = arr_nums.flatten()
    print(arr_nums)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    permutation_of_arrays(x,y,z,n)