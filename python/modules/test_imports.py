import os
import sys
import tempfile


def test_add_dir_to_import_search_path():
    """Create a dir and a python file in it. The name of the python file
    would be the module to import. The test will try to import this and 
    fail at first. It will then add its dir to the import search path and
    then verify that the module can now be imported"""
    dirname = tempfile.mkdtemp()
    module_name = 'module1'
    f = open(os.path.join(dirname, '%s.py' % module_name), 'w')
    f.close()

    try:
        import module1
        assert False, "Test should not reach this point"
    except ImportError: pass

    sys.path.append(dirname)
    import module1


if __name__ == '__main__':
    print "The name of the module is when executed directly is '__main__'."
