# Write a program to mark a spot on a map with an X
line1 = ["O", "O", "O"]
line2 = ["O", "O", "O"]
line3 = ["O", "O", "O"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot")

position = input()

for index, line in enumerate(map):
    for i, place in enumerate(line):
        if position[0].capitalize() == 'A' and i + 1 == int(position[1]):
            line1[i] = 'X'
        elif position[0].capitalize() == 'B' and i + 1 == int(position[1]):
            line2[i] = 'X'
        elif position[0].capitalize() == 'C' and i + 1 == int(position[1]):
            line3[i] = 'X'
        # else: 
        #     print("Invalid position")
        #     exit(0)

print(f'Treasure hidden!\n{line1}\n{line2}\n{line3}')

# ANOTHER SOLUTION
letter = position[0].capitalize()
abc = ["A", "B", "C"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f'Treasure hidden!\n{line1}\n{line2}\n{line3}')
