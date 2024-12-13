from helpers import *
path, testpath = get_input(10)

res = 0
grid = parse_as_nparray(path)
positions = find_all_in_grid(grid, ["0"], True)

for start in positions["0"]:
    paths = [[start]]
    for i in range(1, 10):
        new_paths = []
        for path in paths:
            dir = V2(0, 1)
            for _ in range(4):
                pos = path[-1] + dir
                if pos_in_nparray(grid, pos) and check_pos_in_grid(grid, pos, str(i)):
                    new_path = path.copy()
                    new_path.append(pos)
                    new_paths.append(new_path)
                dir = dir.rotated90()
        paths = new_paths
    res += len(paths)

print(res)