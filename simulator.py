import numpy as np

def crash_round():
    return np.random.exponential(1.5)

def mines_round():
    return np.random.rand()

def run_simulation(game, bankroll, bet, rounds):
    history = []
    balance = bankroll

    for _ in range(rounds):
        if game == "Crash":
            multi = crash_round()
            win = multi > 1.8
        else:
            win = np.random.rand() > 0.5

        balance += bet if win else -bet
        history.append(balance)

    roi = (balance - bankroll) / bankroll

    return {
        "history": history,
        "summary": {
            "final_balance": balance,
            "roi": roi
        }
  }
