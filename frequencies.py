"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        frequencies[str(item)] = 1 + frequencies.get(str(item), 0)

    return frequencies
