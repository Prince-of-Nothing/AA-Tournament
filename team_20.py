def strategy(my_history, opponent_history):
    n = len(my_history)

    if n == 0:
        return 'D'

    round_number = n + 1

    # Every 50th round, defend.
    if round_number % 50 == 0:
        return 'D'

    # Give the opponent two grace rounds after each defensive round.
    if round_number % 50 in (1, 2):
        return 'C'

    # Otherwise, use tit for tat.
    if opponent_history[-1] == 'D':
        return 'D'
    return 'C'
