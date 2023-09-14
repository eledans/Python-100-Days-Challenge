password = ""

for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)
