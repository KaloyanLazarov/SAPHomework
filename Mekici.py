def next_stove(mekici, timings, stove_timers): # check if we have a stove that can finish faster
    """
    Determines whether we continue with the gready approach or we have a stove which can finish the task faster

    :param mekici: number of mekici when deciding in which stove to put the next
    :param timings: the array holding the time it takes of each stove to produce a mekica
    :param stove_timers: the time each stove has spent working
    :return: the index of the stove we are going to put in the next mekica
    """
    next_available_stove = stove_timers.index((min(stove_timers)))  # Find the next available stove



    for index in range(len(timings)): # for each stove

        time_required_to_finish_the_rest = timings[index] * mekici # calculate the time required to finish the task for the current stove

        if (stove_timers[index] + time_required_to_finish_the_rest) <= (stove_timers[next_available_stove] + timings[next_available_stove]):
        #check if the current stove can finish the task faster, than the next available stove
        #+ this is the moment we stop with the grready approach, becuase we have a stove which can finish the task faster
            stove_timers.pop(next_available_stove)
            timings.pop(next_available_stove)
            return index

    return next_available_stove


def list_solution(mekici, stoves, timings, stove_timers=None):
    """
    The solution takes the gready approach up until we have a stove which can finish the task faster

    :param mekici: the current number of mekici
    :param stoves: the number of stoves
    :param timings: the array holding the time it takes of each stove to produce a mekica
    :param stove_timers: the time each stove has spent working
    :return: the time it will take for all mekica to be ready
    """

    if not stove_timers:
        stove_timers = [0 for _ in range(stoves)]  # begin with a list of timers each representing a single stove

    if mekici == 0: # the bottom of the recursion
        return max(stove_timers) # return the time for the stove which finished last

    index_next_stove = next_stove(mekici, timings, stove_timers)
    stove_timers[index_next_stove] += int(timings[index_next_stove]) # we put a mekica on the stove by addining the time required for mekica to be ready

    mekici -= 1

    return list_solution(mekici, stoves, timings, stove_timers) # the recursive call with updated number of mekici


if __name__ == "__main__":
    test_cases = int(input())

    for i in range(test_cases):
        numbers_mekici_and_stoves = input().split(" ")
        mekici = int(numbers_mekici_and_stoves[0])
        stoves = int(numbers_mekici_and_stoves[1])

        timings_string = input().split(" ")
        timings = sorted([int(time) for time in timings_string])


        if mekici <= 0: # in case of an input error, there can be another input errors but it is not requested to handle such
            print("Invalid number for mekici")
        else:
            print(list_solution(mekici, stoves, timings))
