def strategy(my_history, opponent_history)
    #We do not want to cooperate first, we defend, so they know that we can defend, so they don't take advantaage of us thinking that we are 'fools' , who will only cooperate, we are oportunists, but more about instilling fear into the opponent
    n = len(my_history)
    if n==0:
      return 'D'
    planned = [0, 49, 99, 149, 249, 399, 649, 1049]

    # forgiveness after our own D
    if n >= 1 and my_history[-1] == 'D':
        if opponent_history[-1] == 'D':
            return 'D'
        return 'C'
    if n >= 2 and my_history[-2] == 'D':
        if opponent_history[-1] == 'D':
            return 'D'
        return 'C'

    # find next planned defection
    idx = 0
    for i in range(len(planned)):
        if planned[i] > n:
            idx = i
            break

    # check if opponent tolerates our past defections
    tolerance = 0
    for i in range(1, n):
        if my_history[i-1] == 'D' and opponent_history[i] == 'C':
            tolerance += 1
        if my_history[i-1] == 'D' and opponent_history[i] == 'D':
            tolerance -= 2

    # only follow plan if opponent is tolerant
    if tolerance > 0 and idx < len(planned) and n == planned[idx]:
        return 'D'

    # fallback
    if opponent_history[-1] == 'D':
        return 'D'
    return 'C'
      # if we defected last round -> forgive mode
    if my_history[-1] == 'D':
        return 'C'

    # if we defected two rounds ago -> second forgiveness
    if len(my_history) > 1 and my_history[-2] == 'D':
        return 'C'

    # tit for tat otherwise
    if opponent_history[-1] == 'D':
        return 'D'
    else:
        return 'C'
    return opponent_history[-1]
