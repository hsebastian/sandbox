import logging
import types


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filemode='w', level=logging.INFO)


def basic_function():
    """This is a doc string. A doc string is an attribute of the function"""
    logging.info("A function returns None if no return statement is given.")


class TestFunctions(object):
    def test_return_none(self):
        assert basic_function() == None

    def test_doc_string_as_attribute(self):
        assert basic_function.__doc__.startswith("This is a doc string")

    def test_function_is_object(self):
        x = basic_function

        # every object has an ID and in cpython implementation, this is the
        # address of the object in memory. The builtin id() function returns
        # this
        assert type(id(x)) == types.IntType

        # types is a module that defines standard Python object types
        assert type(x) == types.FunctionType

        # one way to determine that this is a Function object is to use
        # builtin hasattr()
        assert hasattr(x, 'func_name')
