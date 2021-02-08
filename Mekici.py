def list_solution(mekici, stoves, timings, stove_timers=None):

    if not stove_timers:
        stove_timers = [0 for _ in range(stoves)]  # begin with a list of timers each representing a single stove

    if mekici == 0: # the bottom of the recursion
        return max(stove_timers) # return the time for the stove which finished last

    next_available_stove = stove_timers.index((min(stove_timers))) # the next available stove is going to be the one
    # which has the lowest time up to that point,
    stove_timers[next_available_stove] += int(timings[next_available_stove]) # we put a mekica on the stove by addining the time required for mekica to be ready

    mekici -= 1

    return list_solution(mekici, stoves, timings, stove_timers) # the recursive call with updated number of mekici


if __name__ == "__main__":
    test_cases = int(input())

    for i in range(test_cases):
        numbers_mekici_and_stoves = input().split(" ")
        mekici = int(numbers_mekici_and_stoves[0])
        stoves = int(numbers_mekici_and_stoves[1])

        timings = input().split(" ")

        print(list_solution(mekici, stoves, timings))
