items = {}
while True:
    try:
        item = input("")
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        break

sorted_items = sorted(list(items.keys()))

print("")
for key in sorted_items:
    print(f"{items[key]} {key.upper()}")
