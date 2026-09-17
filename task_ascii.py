# File: task_ascii.py
# Purpose: Convert a name to its single-digit ASCII representation.
#
# Steps:
#   1. Ask for a name.
#   2. Sum the uppercase ASCII value of each character.
#   3. Keep summing the digits of that total until only one digit remains.
#   4. Print the final single digit.

name = input("Enter your name: ").strip().upper()

print(f"\n# Input: {name}\n")
ascii_values = []
for ch in name:
    value = ord(ch)
    ascii_values.append(value)
    print(f"{ch} -> {value}")

total = sum(ascii_values)
sum_expression = " + ".join(str(v) for v in ascii_values)
print(f"\n# Sum: {sum_expression}")
print(f"= {total}")

while total > 9:
    digits = str(total)
    digit_expression = " + ".join(digits)
    total = sum(int(d) for d in digits)
    print(f"\n# Digit sum: {digit_expression}")
    print(f"= {total}")

print(f"\n# Output: {total}")