import logging


logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    filemode='w', level=logging.INFO)


def build_connection_string(params):
    """Accepts a dictionary and returns its key value pairs as a semi-colon
    separated string. From Dive Into Python chapter 2.1
    """
    return "; ".join(["%s=%s" % (k, v) for k, v in sorted(params.items())])

def test_build_connection_string():
    d = {'lead vocal': 'thom',
         'lead guitar': 'johnny',
         'rhythm guitar': 'ed',
         'bass guitar': 'colin',
         'drummer': 'phil'}
    actual = build_connection_string(d)
    expected = ('bass guitar=colin; drummer=phil; lead guitar=johnny; '
                'lead vocal=thom; rhythm guitar=ed')
    assert actual == expected


