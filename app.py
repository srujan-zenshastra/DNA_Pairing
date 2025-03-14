import random

# Define proteins and their pairing rules
proteins = ['A', 'C', 'G', 'T']
pairing_rules = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# 1. Create strand1 (list) with random proteins
strand1 = [random.choice(proteins) for _ in range(10)]  # Generating a strand of length 10

# 2. Create a pairable strand2 based on values in Strand1
strand2 = [pairing_rules[base] for base in strand1]

# 3 & 4. Create a dictionary with sequential keys and assign each pair to a base
dna_structure = {i: [strand1[i], strand2[i]] for i in range(len(strand1))}

# Print results
print("Strand1:", strand1)
print("Strand2:", strand2)
print("DNA Structure:", dna_structure)