class TestDicts(object):
    def test_no_duplicate_keys(self):
        person = {}
        person['name'] = 'karl'
        assert len(person) == 1
        person['name'] = 'ricky'
        assert len(person) == 1
        person['name'] = 'steve'
        assert len(person) == 1

    def test_case_sensitive_keys(self):
        restaurant = {}
        restaurant['cuisine'] = 'Thai'
        assert len(restaurant) == 1
        restaurant['Cuisine'] = 'Thai'
        assert len(restaurant) == 2


    def test_keys_with_mixed_datatypes(self):
        "They must immutable objects"
        magic_hat = {}
        magic_hat[23] = 'jordan'
        magic_hat['san francisco'] = 49
        magic_hat[1.5] = {}
        magic_hat[True] = 1
        magic_hat[(0, 0)] = 'origin'
        assert magic_hat[17 + 6] == 'jordan'
        assert magic_hat[' '.join(['san', 'francisco'])] == 49
        assert magic_hat[15 * 0.1] == {}
        assert magic_hat[not False] == 1
        assert (0, 0) in magic_hat
