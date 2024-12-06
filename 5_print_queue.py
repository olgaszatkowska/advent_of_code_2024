from copy import copy


def get_page_ordering_rules() -> tuple[dict, dict]:
    rules_predecessors = {}
    rules_successors = {}
    with open("inputs/5.txt") as file:
        for line in file:
            if "|" in line:
                num_1, num_2 = list(map(int, line.split("|")))
                predecessors = rules_predecessors.get(num_2)
                successors = rules_successors.get(num_1)
                if predecessors:
                    predecessors.append(num_1)
                    rules_predecessors[num_2] = predecessors
                else:
                    rules_predecessors[num_2] = [num_1]

                if successors:
                    successors.append(num_2)
                    rules_successors[num_1] = successors
                else:
                    rules_successors[num_1] = [num_2]
    return rules_predecessors, rules_successors


def get_updates():
    updates = []
    with open("inputs/5.txt") as file:
        for line in file:
            if "," in line:
                numbers = list(map(int, line.split(",")))
                updates.append(numbers)
    return updates


def check_if_valid_successor(
    current, next, rules_successors: dict, rules_predecessors: dict
):
    current_predecessors = rules_predecessors.get(current)
    current_successors = rules_successors.get(current)
    if current_successors:
        if next in current_successors:
            return True
    if not current_predecessors:
        return True

    if next in current_predecessors:
        return False

    return True


def is_update_valid(update, rules_successors: dict, rules_predecessors: dict):
    for i, number in enumerate(update):
        next_numbers = update[i : len(update) + 1]
        for next_number in next_numbers:
            valid = check_if_valid_successor(
                number, next_number, rules_successors, rules_predecessors
            )
            if not valid:
                return False
    return True


def get_middle_number(update):
    middle = len(update) / 2
    return update[int(middle)]


def correct_invalid_update(
    update: list, rules_successors: dict, rules_predecessors: dict
):
    is_valid = False
    while not is_valid:
        is_valid = True
        for i, number in enumerate(update):
            next_numbers = update[i : len(update) + 1]
            for next_number in next_numbers:
                valid = check_if_valid_successor(
                    number, next_number, rules_successors, rules_predecessors
                )
                if not valid:
                    is_valid = False
                    next_number_i = update.index(next_number)

                    update.remove(number)
                    update.insert(next_number_i + 1, number)

    return update


def correct_invalid_updates():
    rules_predecessors, rules_successors = get_page_ordering_rules()
    updates = get_updates()
    return [
        correct_invalid_update(update, rules_successors, rules_predecessors)
        for update in updates
        if not is_update_valid(update, rules_successors, rules_predecessors)
    ]


def get_middle_pages_correct_update_sum():
    rules_predecessors, rules_successors = get_page_ordering_rules()
    updates = get_updates()

    middle_numbers = [
        get_middle_number(update)
        for update in updates
        if is_update_valid(update, rules_successors, rules_predecessors)
    ]

    print(sum(middle_numbers))


def get_middle_pages_sum():
    corrected_updates = correct_invalid_updates()
    middle_numbers = [get_middle_number(update) for update in corrected_updates]

    print(sum(middle_numbers))


get_middle_pages_correct_update_sum()
get_middle_pages_sum()
