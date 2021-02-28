# the variable 'teams' is already defined
import itertools

my_iter = itertools.combinations(teams, 2)
for each in my_iter:
    print(each)
