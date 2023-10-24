import itertools

# Create an iterable that cycles through the letters 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd' indefinitely
message = itertools.cycle("Hello World")

# Use a generator expression to print each letter with a pause in between
for letter in message:
    print(letter, end='', flush=True)  # Print the next letter without a newline and flush the buffer
    if letter == 'd':
        break  # Exit the loop when 'd' is encountered

print()  # Print a newline to complete the message
