import types


class TestAssignment(object):
    def test_assigning_multiple_values_at_once(self):
        comics = ('dono', 'kasino', 'indro')
        assert len(comics) == 3
        x, y, z = comics
        assert x == 'dono'
        assert y == comics[1]
        assert z == 'indro'


    def test_assigning_consecutive_values(self):
        length = 6
        my_list = range(length)
        assert type(my_list) == types.ListType
        a, b, c, d, e, f = range(length)
        assert type(a) == types.IntType
        assert a == my_list[0]

