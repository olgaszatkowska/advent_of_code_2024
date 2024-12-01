from collections import defaultdict


def get_left_right():
    with open("inputs/1.txt") as file:
        left = []
        right = []
        for line in file:
            left_id, right_id = line.split()
            left.append(int(left_id))
            right.append(int(right_id))

    return left, right


def distance(left, right):
    total_distance = 0

    while left != []:
        l_min_value = min(left)
        r_min_value = min(right)

        if l_min_value > r_min_value:
            difference = l_min_value - r_min_value
        else:
            difference = r_min_value - l_min_value

        total_distance += difference

        left.remove(l_min_value)
        right.remove(r_min_value)

    print(total_distance)


def similarity_score(left, right):
    r_count = defaultdict(lambda: 0)

    for r_id in right:
        r_count[r_id] += 1

    total_score = 0

    for l_id in left:
        r_id_count = r_count.get(l_id)
        if r_id_count:
            total_score += l_id * r_id_count

    print(total_score)


distance(*get_left_right())
similarity_score(*get_left_right())
