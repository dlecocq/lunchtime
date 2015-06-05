from nose.tools import assert_equal

import lunchtime

implementations = [
    lunchtime.greedy
]

# Just some example restaurants
restaurants = [
    lunchtime.Restaurant('Saltys', 'seafood'),
    lunchtime.Restaurant('Scariyaki', 'Japanese'),
    lunchtime.Restaurant('Pot Bellys', 'americana'),
    lunchtime.Restaurant('Palisade', 'seafood')
]
# Turn this into a map
restaurants = dict((r.name, r) for r in restaurants)

def test_basic():
    assert lunchtime.satisfied(lunchtime.greedy(restaurants.values()))


def test_satisfied():
    def function(example, expected):
        choices = []
        for choice in example:
            if choice == 'LFH':
                choices.append(lunchtime.LFH)
            else:
                choices.append(restaurants[choice])

        assert_equal(lunchtime.satisfied(choices), expected)

    examples = [
        # Missing lunch-from-home
        (('Saltys', 'Scariyaki', 'Pot Bellys', 'Palisade', 'Scariyaki'),
            False),
        # Two lunch-from-homes
        (('Saltys', 'LFH', 'LFH', 'Palisade', 'Scariyaki'),
            False),
        # Same place on consecutive days
        (('Saltys', 'Saltys', 'LFH', 'Pot Bellys', 'Scariyaki'),
            False),
        # Same cuisine more than twice in a week
        (('Saltys', 'LFH', 'Saltys', 'Palisade', 'Scariyaki'),
            False)
    ]
    for choices, expected in examples:
        yield function, choices, expected


def test_permutations():
    expected = len(list(lunchtime.permutations_oracle(restaurants.values())))
    actual = len(list(lunchtime.permutations(restaurants.values())))
    assert_equal(expected, actual)
