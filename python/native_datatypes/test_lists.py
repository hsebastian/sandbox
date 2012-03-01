import logging
import math
import os


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename="debug.log", filemode='w',
                    level=logging.INFO)


class TestLists(object):
    def test_ordered_elements(self):
        numbers = []
        for i in range(0, 10):
            numbers.append(i)
        i = 0
        while len(numbers) > 0:
            assert numbers.pop(0) == i
            i += 1

    def test_negative_list_indices(self):
        days = ['m', 't', 'w', 't', 'f', 's', 's']
        days_week = ''
        for i in range(-7, 0):
            days_week += days[i]
        assert days_week == 'mtwtfss'

    def test_mapping_list(self):
        maximum = 10
        cube_sides = range(1, maximum)
        cube_volumes = [ side * side * side for side in cube_sides]
        for side in cube_sides:
            assert int(math.pow(side, 3)) == cube_volumes.pop(0)

    def test_adding_items(self):
        raise AssertionError, "TODO"

    def test_slicing_list(self):
        raise AssertionError, "TODO"

    def test_searching_items(self):
        raise AssertionError, "TODO"

    def test_operators(self):
        raise AssertionError, "TODO"

    def test_stacks(self):
        raise AssertionError, "TODO"

    def test_queues(self):
        raise AssertionError, "TODO"
