def strategy(my_history, opponent_history):
    n = len(my_history)

    if n == 0:
        return 'D'

    check_interval = 50
    grace_period = 2

    # Every 50 rounds, use a cooperative check to probe the opponent.
    if n % check_interval == 0:
        return 'C'

    # After one of our checks, give the opponent two rounds of space
    # before switching back to retaliation.
    last_check_round = None
    for round_index in range(n - 1, -1, -1):
        if round_index % check_interval == 0 and my_history[round_index] == 'C':
            last_check_round = round_index
            break

    if last_check_round is not None:
        rounds_since_check = n - 1 - last_check_round
        if rounds_since_check <= grace_period:
            return 'C'

    # Default behavior: cooperate unless the opponent defected recently.
    if opponent_history[-1] == 'D':
        return 'D'
    return 'C'
