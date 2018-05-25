from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def generate_file():
    f = open("guru99.txt", "w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.close()


@shared_task
def gen_prime(x):
    multiples = []
    results = []
    from redis._compat import xrange
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results


