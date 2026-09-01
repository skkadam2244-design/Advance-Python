class MultiplicationTable:
    def __init__(self, number):
        self.number = number
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 10:
            result = self.number * self.current
            self.current += 1
            return result
        else:
            raise StopIteration


# Accept input number
number = int(input("Enter a number: "))

# Create iterator
table = MultiplicationTable(number)

# Print multiplication table
print("\nMultiplication Table of", number)

for i, result in enumerate(table, start=1):
    print(number, "x", i, "=", result)