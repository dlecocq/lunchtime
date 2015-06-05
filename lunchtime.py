import random
import itertools
from collections import Counter

class Restaurant(object):
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def __str__(self):
        return '%s (%s)' % (self.name, self.cuisine)

    def __repr__(self):
        return '<Restaurant %s >' % self

# Lunch from home
LFH = Restaurant('Home', None)


def satisfied(choices):
    '''Verify the constraints are satisfied:
    1. As random as possible (not verified here)
    2. Cannot eat from the same restaurant on two consecutive days
    3. Cannot eat the same cuisine twice in a week
    4. Lunch from home exactly once
    '''
    # 2. Cannot eat from the same restaurant on two consecutive days
    for i in range(len(choices) - 1):
        if choices[i].name == choices[i+1].name:
            return False

    # 3. Cannot eat the same cuisine twice in a week
    counts = Counter(c.cuisine for c in choices)
    if max(counts.values()) > 2:
        return False

    # 4. Lunch from home exactly once
    if len([c for c in choices if c == LFH]) != 1:
        return False

    # If we've made it this far, all constraints are satisfied
    return True


def greedy(available, choices=None):
    '''Greedily pick random restaurants'''
    # On the first iteration, assign lunch from home
    if choices == None:
        choices = [None] * 5
        choices[random.choice(range(5))] = LFH

    # If we'e chosen the whole week, then we're done
    if len([c for c in choices if c != None]) == 5:
        if satisfied(choices):
            return choices
        else:
            return False

    # Find the slot that we're assigning. In other words, the first
    # non-chosen day
    slot = [i for i, c in enumerate(choices) if c == None][0]

    # We'll iterate through all the possibilities in a random order
    # This allows us to have more options in the case that a branch
    # is unsatisfiable
    for choice in random.sample(available, len(available)):
        choices[slot] = choice
        results = greedy(available, choices)
        if results:
            return results
        choices[slot] = None

    # If we haven't returned yet, this is not satisfiable
    return False


def permutations(available, choices=None):
    '''Generator for all permutations that are valid. This does not aggressively prune
    branches from the search path, but such an optimization would be possible.'''
    # First, assign the lunch-from-home day
    if choices == None:
        choices = [None] * 5
        for slot in range(5):
            choices[slot] = LFH
            for result in permutations(available, list(choices)):
                # Make a copy of the list
                yield result
            choices[slot] = None
        return

    # If we'e chosen the whole week, then we're done
    if len([c for c in choices if c != None]) == 5:
        if satisfied(choices):
            # Make a copy of our choices
            yield list(choices)
        return

    # Find the slot that we're assigning. In other words, the first
    # non-chosen day
    slot = [i for i, c in enumerate(choices) if c == None][0]

    # We'll iterate through all the possibilities in a random order
    # This allows us to have more options in the case that a branch
    # is unsatisfiable
    for choice in available:
        choices[slot] = choice
        for results in permutations(available, list(choices)):
            yield results


def permutations_oracle(available):
    '''This is a less-efficient but more-trustworthy implementation.'''
    available = list(available) + [LFH]
    for choice in itertools.product(available, repeat=5):
        if satisfied(choice):
            yield choice
