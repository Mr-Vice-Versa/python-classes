# -*- coding: utf-8 -*-
__author__ = "Vladislav Ischenko"
# Python-curses Wargaming 09.04.2014 L4Problem

import time
import unittest


# First task


def map_rq(fun, sequence):
    if len(sequence) == 0:
        return []
    else:
        return [fun(sequence[0])] + map_rq(fun, sequence[1:])


def map_yield(fun, sequence):
    for elem in sequence:
        yield fun(elem)


def map_rq_yield(fun, sequence):
    if len(sequence) == 0:
        yield None
    else:
        yield fun(sequence[0])
        for i in map_rq_yield(fun, sequence[1:]):
            yield i


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.fun = lambda x: x ** 2
        self.sequence = [1, 2, 3, 4]
        self.answer = [1, 4, 9, 16]

    def test_map_rq(self):
        self.assertEqual(map_rq(self.fun, self.sequence), self.answer)

    def test_map_yield(self):
        res = [elem for elem in map_yield(fun, sequence)]
        self.assertEqual(res, self.answer)


# Second task


statistic = {}


def time_me(time_fn, statdict):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            start = time_fn()
            res = fn(*args, **kwargs)
            end = time_fn()
            statdict['cum_time'] = statdict.setdefault(
                'cum_time', 0.0) + (end - start)
            statdict['num_calls'] = statdict.setdefault('num_calls', 0) + 1
            return res
        return wrapper
    return decorator


@time_me(time.time, statistic)
def some_func(x, y):
    time.sleep(1.1)
    return x + y


if __name__ == '__main__':
    #### Unit Tests ####
    fun = lambda x: x ** 2
    sequence = [1, 2, 3, 4]
    answer = [1, 4, 9, 16]

    assert map_rq(fun, sequence) == answer
    assert [elem for elem in map_yield(fun, sequence)] == answer

    print some_func(4, 3), statistic

    # Run class unittests
    unittest.main()
