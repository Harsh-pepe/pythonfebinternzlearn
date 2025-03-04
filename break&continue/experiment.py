numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Using break:")
for num in numbers:
    if num == 6:
        print(f"Number {num} found, stopping loop!")
        break  # Exit the loop when 6 is found
    print(num)

print("\nUsing continue:")
for num in numbers:
    if num == 5:
        print("Skipping 5!")
        continue  # Skip printing 5 and move to the next iteration
    print(num)
