from src.utils import math_operations, fruit_data

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = math_operations.add(5, 3)
print("Result:", result)

data = fruit_data.getData()
print("Data:", data)
