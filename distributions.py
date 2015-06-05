#! /usr/bin/env python

import lunchtime
from collections import Counter

restaurants = [
    lunchtime.Restaurant('Saltys', 'seafood'),
    lunchtime.Restaurant('Scariyaki', 'Japanese'),
    lunchtime.Restaurant('Pot Bellys', 'americana'),
    lunchtime.Restaurant('Palisade', 'seafood')
]

# Consider the number of permutations that start with each restaurant
counts = Counter(choices[0].name for choices in lunchtime.permutations(restaurants))
print 'Monday restaurant => # valid permutations'
total = float(sum(counts.values()))
for key, value in sorted(counts.items()):
    print '%17s => %10.5f%%' % (key, value * 100 / total)

# Consider the distribution of the Monday restaurant with the greedy approach
counts = Counter(lunchtime.greedy(restaurants)[0].name for _ in range(10000))
total = float(sum(counts.values()))
print 'Monday restaurant => representation in greedy approach'
for key, value in sorted(counts.items()):
    print '%17s => %10.5f%%' % (key, value * 100 / total)
