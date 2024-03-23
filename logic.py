import json

def create_grid(letters):
    if len(letters) != 16:
        raise ValueError("Input must be exactly 16 letters long.")
    return [list(letters[i:i+4]) for i in range(0, 16, 4)]

letters = input("LEMME COOK ")
grid = create_grid(letters)

print("4x4 Grid:")
for row in grid:
    print(row)

json_file_path = 'words_dictionary.json'

def has_short_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) < 3:
                    return True
    return False

with open(json_file_path, 'r') as json_file:
    dictionary = json.load(json_file)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_valid_position(x, y, visited):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y]

def is_valid_word(word):
    if len(word) > 4:
            return dictionary.get(word.lower(), 0) == 1
    return False

found_words = []

def dfs(x, y, visited, path):
    visited[x][y] = True
    word = ''.join(path)
    if is_valid_word(word):
        found_words.append(word)
        print(f"Found word: {word}")
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid_position(nx, ny, visited):
            dfs(nx, ny, visited, path + [grid[nx][ny]])
    visited[x][y] = False

def find_words():
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            dfs(x, y, [[False for _ in range(len(grid[0]))] for _ in range(len(grid))], [grid[x][y]])

find_words()

sorted_found_words = sorted(found_words, key=len, reverse=True)
print("TYPE:")
print(sorted_found_words)
