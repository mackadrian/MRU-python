# Name(s):  Mack Bautista(201729981) / Soona Youssef(201708547)


def get_file_read(file_name) -> list:
    """
    Given a file handler that reads and returns a list.
    """
    try:
        building = open(file_name, "r")
        contents = building.readlines()
        building.close
        return contents
    except OSError as e:
        print(e)


def get_file_write(raw_file, glass, recycled, stone, wood):
    """
    Writes the results in a new file called 'scoring-results.txt'.
    """
    try:
        solutions = open("datafiles/scoring-results.txt", "w")
        total = glass + recycled + stone + wood
        for row in raw_file:
            for column in row:
                solutions.write(column)
        solutions.write(f"""

+----------+----+
| glass    | {glass}  |
| recycled | {recycled}  |
| stone    | {stone}  |
| wood     | {wood}  |
+==========+====+
| total    | {total} |
+----------+----+
""")

        solutions.close()
        print("File has been successfully written.")

    except OSError as e:
        print("Could not write output to error due to error", {e})


def find_length(read_text) -> int:
    """
    Finds the length of file.
    """
    num_levels = len(read_text)
    return num_levels


def get_level(raw_file, num_levels: int) -> list:
    """
    Processes building.txt by taking the indices and turning it into a list of lists.
    """
    level = []
    for _ in raw_file:
        num_levels -= 1
        idx = [
            raw_file[num_levels][0] + raw_file[num_levels][1],
            raw_file[num_levels][2],
            raw_file[num_levels][3] + raw_file[num_levels][4],
            raw_file[num_levels][5],
            raw_file[num_levels][6] + raw_file[num_levels][7],
        ]
        level.append(idx)
    return level


def get_glass_score(levels: list) -> int:
    """
    Calculates the score of glass dice.
    """
    score = 0
    for row in levels:
        for column in row:
            if "G1" in column:
                score += 1
            elif "G2" in column:
                score += 2
            elif "G3" in column:
                score += 3
            elif "G4" in column:
                score += 4
            elif "G5" in column:
                score += 5
            elif "G6" in column:
                score += 6
    return score


def get_recycled_score(levels: list) -> int:
    """
    Calculates the score of recycled dice.
    """
    recycled = 0
    for row in levels:
        for column in row:
            if "R" in column:
                recycled += 1
            if recycled == 1:
                score = 2
            elif recycled == 2:
                score = 5
            elif recycled == 3:
                score = 10
            elif recycled == 4:
                score = 15
            elif recycled == 5:
                score = 20
            elif recycled == 6:
                score = 30
    return score


def get_stone_score(levels) -> int:
    """
    Calculates the score of stone dice.
    """
    score = 0
    for row in range(len(levels)):
        for column in range(len(levels[row])):
            if ("S" in levels[row][column]) and (row == 0):
                score += 2
            elif ("S" in levels[row][column]) and (row == 1):
                score += 3
            elif ("S" in levels[row][column]) and (row == 2):
                score += 5
            elif ("S" in levels[row][column]) and (row >= 3):
                score += 8
    return score


def get_wood_score(levels: list) -> int:
    """
    Calculates the score of wood dice.
    """
    score = 0
    adjacent_counter = 0
    for row in range(len(levels)):
        for column in range(len(levels)):
            if "W" in levels[row][column]:
                if (not "-" in levels[row - 1][column]):
                    adjacent_counter += 1
                elif (not "-" in levels[row + 1][column]):
                    adjacent_counter += 1
                if (not "-" in levels[row][column - 1]):
                    score += 2
                elif (not "-" in levels[row][column + 1]):
                    adjacent_counter += 1
            else:
                score += 0

    for _ in range(adjacent_counter):
        score += 2

    return adjacent_counter


def main() -> None:
    """
    Main function and calls will be done here.
    """
    raw_file = get_file_read("datafiles/building.txt")
    num_levels = find_length(raw_file)
    levels = get_level(raw_file, num_levels)
    glass = get_glass_score(levels)
    print(glass)
    recycled = get_recycled_score(levels)
    print(recycled)
    stone = get_stone_score(levels)
    print(stone)
    wood = get_wood_score(levels)
    print(wood)
    # get_file_write(raw_file, glass, recycled, stone, wood)


main()
