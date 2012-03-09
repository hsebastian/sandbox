import types


class Program(object):
    SYSTEM_PORT = "7999"
    def __init__(self, port):
        self.port = port
    def start(self):
        print "Program is running on port: %s" % self.port


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

    def test_callable(self):
        assert callable(Program) == True
        assert callable(Program.start) == True
        assert callable("hello world") == False
        assert callable(types) == False


