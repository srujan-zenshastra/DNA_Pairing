# DNA Strand Pairing Simulation

## Overview
This project simulates the pairing of DNA strands using Python. It generates a random DNA sequence (Strand1) and creates its complementary strand (Strand2) based on standard DNA base pairing rules.

## How It Works
1. A random DNA sequence (Strand1) is generated using the bases **A (Adenine), C (Cytosine), G (Guanine), and T (Thymine)**.
2. A complementary strand (Strand2) is created based on the following pairing rules:
   - **A pairs with T**
   - **T pairs with A**
   - **C pairs with G**
   - **G pairs with C**
3. The paired bases are stored in a dictionary, where each index represents a base pair.
4. The results are printed, showing the original strand, its complementary strand, and the structured DNA pairing.

## Installation and Dependencies
This project requires Python 3.x and no additional external libraries. The built-in `random` module is used to generate random DNA sequences.

## Usage
Run the Python script to generate and display the DNA strands:
```python
python dna_pairing.py
```

## Example Output
Strand1: ['A', 'G', 'T', 'C', 'A', 'C', 'G', 'T', 'G', 'A']
Strand2: ['T', 'C', 'A', 'G', 'T', 'G', 'C', 'A', 'C', 'T']
DNA Structure: {0: ['A', 'T'], 1: ['G', 'C'], 2: ['T', 'A'], 3: ['C', 'G'], 4: ['A', 'T'], 5: ['C', 'G'], 6: ['G', 'C'], 7: ['T', 'A'], 8: ['G', 'C'], 9: ['A', 'T']}
