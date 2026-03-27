def strategy(my_history, opponent_history)
    #We do not want to cooperate first, we defend, so they know that we can defend, so they don't take advantaage of us thinking that we are 'fools' , who will only cooperate, we are oportunists, but more about instilling fear into the opponent
    if len(opponent_history)==0:
      return 'D'
    return opponent_history[-1]
