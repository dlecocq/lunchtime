Lunchtime
=========
Given the following constraints, schedule a week's worth of lunches:

1. The lunches should be chosen as randomly as possible.
2. Lunch on consecutive days can't be from the same place.
3. Lunch cannot be of the same cuisine more than twice in a week.
4. Lunch is brought from home exactly once a week.

Tests
=====
With `nose` installed, tests can be run with `make test`.

Randomness
==========
Two approaches are implemented: `greedy` and `permutation`-based. The greedy
approach is more efficient, but is not as random as the perumtation approach.

The greedy approach randomly selects a restaurant for the first day and continues
exploring possibilities based on satisfying the constraints. This does not lead to
a uniform sampling of the valid permutations, but may be considered sufficiently random.
The permutation-based approach materializes all valid permutations and samples uniformly
into them.

For example, with 4 restaurants available, the greedy approach would uniformly distribute
the Monday choice among them. More generally, we expect `20%` of the Monday representation
to be lunch-from-home and the remaining `80%` distributed evenly among the remaining
restaurants. In a simulation of 10000 runs, we see evidence of this:

```
Monday restaurant => representation in greedy approach
             Home =>   20.06000%
         Palisade =>   19.92000%
       Pot Bellys =>   19.88000%
           Saltys =>   19.88000%
        Scariyaki =>   20.26000%
```

However, the Monday restaurant representation does not have this distribution
when considering all permutations:

```
Monday restaurant => # valid permutations
             Home =>   17.52137%
         Palisade =>   16.23932%
       Pot Bellys =>   25.00000%
           Saltys =>   16.23932%
        Scariyaki =>   25.00000%
```
