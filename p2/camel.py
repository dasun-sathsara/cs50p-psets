camel_case = input("Enter word: ")
snake_case = ""

for char in camel_case:
    if char.isupper():
        snake_case += f"_{char.lower()}"
    else:
        snake_case += char

print(snake_case)
