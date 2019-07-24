from itertools import combinations

def find_number_pairs(numbers, N=10):
	return [t for t in combinations(numbers, 2) if sum(t) == N]
