# Array Advanced Game Problem
# Non Greedy Way

def possible_to_reach_end_of_array(my_array):
    i = 0
    farthest_reached = 0
    while (i <= farthest_reached and farthest_reached < len(my_array) - 1):
        farthest_reached = max(farthest_reached, my_array[i] + i)
        print('Farthest Reached = %i' % farthest_reached)
        i += 1
    print("------------------------------------------")
    return farthest_reached >= len(my_array) - 1


def main():
    test_array_collection = [[2, 3, 1, 1, 0, 2, 3],
                             [3, 3, 1, 0, 2, 0, 1],
                             [0, 0, 0, 0, 2]
                             ]

    for item in test_array_collection:
        print(possible_to_reach_end_of_array(item))


if __name__ == "__main__":
    main()
