# import sys
args = sys.argv
params = [each for each in args]
print(list(map(int, params[1:])))
