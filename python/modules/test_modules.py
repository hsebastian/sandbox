import os
import subprocess


print_line = "The name of the module when executed directly is '__main__'."


def test_module_name_as_main():
    # Unless this file is run directly, this file is a module in which the
    # filename is the name of the module.
    assert __name__ == os.path.basename(__file__).split('.')[0]

    # Executes the file directly and verifies the value of print_line is
    # returned. 
    cmd = ['python', __file__]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p.stdout.read()
    for line in p.stdout:
        assert line == '%s\n' % print_line


if __name__ == '__main__':
    print print_line
