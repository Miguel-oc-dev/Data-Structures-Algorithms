def backtrack(path, choices):
    if end_condition(path):
        result.append(path[:])
        return

    for i in range(len(choices)):
        path.append(choices[i])
        backtrack(path, choices)
        path.pop()
