#!/usr/bin/env python3
"""
Demonstration of f-string alignment options
"""

text = "Hello"
number = 42.567

print("=== Alignment Demonstration ===\n")

# Default alignment (left for strings, right for numbers)
print("Default alignment:")
print(f"Text: '{text:10}' | Number: '{number:10.2f}'")
print()

# Explicit left alignment
print("Left alignment (<):")
print(f"Text: '{text:<10}' | Number: '{number:<10.2f}'")
print()

# Right alignment
print("Right alignment (>):")
print(f"Text: '{text:>10}' | Number: '{number:>10.2f}'")
print()

# Center alignment
print("Center alignment (^):")
print(f"Text: '{text:^10}' | Number: '{number:^10.2f}'")
print()

# Your metro area example with explicit symbols
print("=== Your Metro Area Code ===")
print("With explicit alignment symbols:")
print(f'{"City":<15} | {"Latitude":>9} | {"Longitude":>9}')
print(f'{"Tokyo":<15} | {35.6900:>9.4f} | {139.6900:>9.4f}')
print(f'{"Delhi NCR":<15} | {28.6100:>9.4f} | {77.2000:>9.4f}')