import random
import pylab


def flip():
    if random.random() <= 0.5:
        return 'heads'
    else:
        return 'tails'


def run_simulation_without_streak(settings, plotting=False):
    random.seed(5)
    starting_money = settings['starting_money']
    bet_cost = settings['bet_cost']
    win_multiplier = settings['win_multiplier']
    amount_of_bets = settings['amount_of_bets']
    runs = settings['runs']

    # Point 0 added statically so bet #0 is accurate
    money_plot = [starting_money] + [0] * amount_of_bets  # Plot points for money over # of bets
    end_balances = []
    for _ in range(runs):
        money = starting_money
        bets_made = 0
        while bets_made < amount_of_bets:
            # Flip coin (bet coin)
            coin = flip()
            if money >= bet_cost:  # If money is still left to bet
                money -= bet_cost
                if coin == 'tails':  # Win
                    money += bet_cost * win_multiplier
            bets_made += 1
            money_plot[bets_made] += money
        end_balances.append(money)
    print(f'(NORMAL) AVERAGE FINAL BALANCE: {sum(end_balances)/len(end_balances)}')
    # Point 0 added statically so bet #0 is accurate
    average_money = [starting_money] + [x/runs for x in money_plot[1:]]
    if not plotting:  # For compare function
        return average_money
    else:
        pylab.plot(average_money)
        pylab.title("Normal Money Results")
        pylab.xlabel("Bet")
        pylab.ylabel("Money")
        pylab.show()


def run_simulation_with_streak(settings, plotting=False):
    starting_money = settings['starting_money']
    bet_cost = settings['bet_cost']
    win_multiplier = settings['win_multiplier']
    streak_to_reach = settings['streak_to_reach']
    amount_of_bets = settings['amount_of_bets']
    runs = settings['runs']

    random.seed(5)
    all_tries = []  # Store how many tries it took to reach given streak
    # Plot points for money over # of bets. Summed then averaged at the end.
    # Point 0 added statically so bet #0 is accurate
    money_plot = [starting_money] + [0] * amount_of_bets
    final_heads = 0  # Amount of heads after streak
    final_tails = 0  # Amount of tails after streak
    end_balances = []
    for _ in range(runs):
        money = starting_money
        bets_made = 0
        while bets_made < amount_of_bets:
            tries = 1
            streak = 0
            while streak < streak_to_reach:
                if flip() == 'heads':  # If heads, streak increases
                    streak += 1
                else:  # If tails, attempt to reach streak failed, so reset
                    streak = 0
                    tries += 1
            all_tries.append(tries)  # Target streak was reached, log amount of tries it took
            # Flip final coin (bet coin)
            final_coin = flip()
            if final_coin == 'heads':
                final_heads += 1
            else:
                final_tails += 1
            if money >= bet_cost:  # If money is still left to bet
                money -= bet_cost
                if final_coin == 'tails':
                    money += bet_cost * win_multiplier
            bets_made += 1
            money_plot[bets_made] += money
        end_balances.append(money)
    # Final printing
    expected_chance = 0.5**streak_to_reach  # For streak goal
    print(f'(STREAK) AVERAGE FINAL BALANCE: {sum(end_balances) / len(end_balances)}')
    print(f'Expected chance to reach goal streak: 1/{int(1/expected_chance)}')
    print(f'Average tries to reach goal streak: ~{int(sum(all_tries) / len(all_tries))}')
    print(f'Number of heads directly after reaching streak: {final_heads}')
    print(f'Number of tails directly after reaching streak: {final_tails}')
    # Point 0 added statically so bet #0 is accurate
    average_money = [starting_money] + [x/runs for x in money_plot[1:]]
    if not plotting:  # For compare function
        return average_money
    else:
        pylab.plot(average_money)
        pylab.title("Streak Money Results")
        pylab.xlabel("Bet")
        pylab.ylabel("Money")
        pylab.show()


def compare_simulations(settings):
    starting_money = settings['starting_money']
    streak_money = run_simulation_with_streak(settings)
    normal_money = run_simulation_without_streak(settings)

    pylab.plot(streak_money, label="Average Streak Money")
    pylab.plot(normal_money, label="Average Normal Money")
    pylab.title("Money Results")
    pylab.xlabel("Bet")
    pylab.ylabel("Money")
    pylab.legend(loc="best")
    pylab.ylim(starting_money * 0.95, starting_money * 1.05)
    pylab.show()
