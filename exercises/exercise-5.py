# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
# First 50 terms when starting at 0 only goes up to term 49...

count = 0
base = 0
next = 1
next2 = 0
while count < 50:
    print(f"term: {count} / number: {base}")
    next2 = base + next
    base = next
    next = next2
    count += 1