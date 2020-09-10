import math


def dot(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dot(v, v))


def sub(v1, v2):
    return [(a-b) for a, b in zip(v1, v2)]


def distance(v1, v2):
    return length(sub(v1, v2))


def normalize(v):
    return [x / length(v) for x in v]


def dir(v1, v2):
    x, y = sub(v1, v2)
    return format(math.atan2(x, y), '.32f')


def get_lattice_size(dimensions, distance):
    width = dimensions[0]
    height = dimensions[1]

    lattice_width = ((distance / width) + 1) * 2
    lattice_height = ((distance / height) + 1) * 2

    return max(lattice_width, lattice_height)


def enumerate(size):
    lattice = []
    x = y = 0
    dx = 0
    dy = -1
    for _ in range(size**2):
        if (-size/2 < x <= size/2) and (-size/2 < y <= size/2):
            lattice.append((x, y))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

    return lattice


def get_positions(lattice, dimensions, initial_position):
    previous_grid = lattice[0]
    positions = [initial_position]

    for i in range(1, len(lattice)):
        grid = lattice[i]

        delta_x, delta_y = tuple(x-y for x, y in zip(grid, previous_grid))

        prev = positions[i - 1]

        if delta_x < 0:
            from_left = abs(prev[0] % dimensions[0])
            positions.append([prev[0] - from_left * 2, prev[1]])
        elif delta_x > 0:
            from_right = dimensions[0] - abs((prev[0] % dimensions[0]))
            positions.append([prev[0] + from_right * 2, prev[1]])
        elif delta_y < 0:
            from_bottom = abs(prev[1] % dimensions[1])
            positions.append([prev[0], prev[1] - from_bottom * 2])
        elif delta_y > 0:
            from_top = dimensions[1] - abs((prev[1] % dimensions[1]))
            positions.append([prev[0], prev[1] + from_top * 2])

        previous_grid = grid
    return positions


def count_valid(your_positions, guard_positions, max_distance):
    ip = your_positions[0]
    seen_directions = {}
    count = 0

    if distance(guard_positions[0], ip) < max_distance:
        count += 1
        seen_directions[dir(guard_positions[0], ip)] = True

    for i in range(1, len(guard_positions)):
        direction = dir(guard_positions[i], ip)

        seen_directions[dir(your_positions[i], ip)] = True

        if distance(guard_positions[i], ip) <= max_distance and direction not in seen_directions:
            count += 1
            seen_directions[direction] = True

    return count


def solution(dimensions, your_position, guard_position, distance):

    lattice_size = get_lattice_size(dimensions, distance)
    lattice = enumerate(lattice_size)
    guard_position_list = get_positions(lattice, dimensions, guard_position)
    your_position_list = get_positions(lattice, dimensions, your_position)
    return count_valid(your_position_list, guard_position_list, distance)


print(solution([2, 5], [1, 2], [1, 4], 11))
