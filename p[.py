import random
from itertools import permutations

# Given list of words
words = ["롤", "고", "원", "리", "곤", "전", "압", "사", "산", "크", "프", "컨", "국"]

# Generate all permutations (limited to subsets for randomness)
random_samples = random.sample(list(permutations(words, len(words))), 10)

# Convert tuple results to strings
random_results = [''.join(sample) for sample in random_samples]
random_results
