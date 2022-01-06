from helper_functions import run_simulation_with_streak, run_simulation_without_streak, compare_simulations

# Clarifications:
# - Winner = tails
# - Given streak is reached, cost-free, before bet is placed
# - Simulation variables should be integers

settings = {
    # -- Money variables
    'starting_money': 5000,  # Starting money
    'bet_cost': 100,  # How much it costs to place a bet
    'win_multiplier': 2,  # Earnings multiplier for winning (gross not net)
    # -- Simulation variables
    'streak_to_reach': 10,  # Streak to reach before placing bet
    'amount_of_bets': 20,  # How many times to bet
    'runs': 1000  # Times to run simulation
}

compare_simulations(settings)
# Run individually
# run_simulation_with_streak(settings, plotting=True)
# run_simulation_without_streak(settings, plotting=True)
