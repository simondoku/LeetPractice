def carFleet(target, position, speed):
    # Sort cars by position so you can simulate the merging of fleets from back to front.
    # Use the time each car takes to determine whether it forms a new fleet or joins an existing one.
    pair = [[p, s] for p, s in zip(position, speed)]

    stack = []
    for p,s in sorted(pair)[::-1]:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)