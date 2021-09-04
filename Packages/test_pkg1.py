'''
import pkg1

n = int(input())


print(pkg1.isprime(n))


from pkg1 import *


n = int(input())
li = list(map(int, input().split()))

print(isprime(n),list_sum(li))
'''

from pkg1 import isprime, list_sum


n = int(input())
li = list(map(int, input().split()))

print(isprime(n),list_sum(li))
