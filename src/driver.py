from donate_or_save import *

SHOW_DISCLAIMER = True

career_length = 40 # how many years you donate money for
annual_income = 50000
fraction_donated = 0.1
growth_rate = 1.05
inflation = 1.02
donations_per_year = 12 # how frequently you donate (does not change total donations)

annual_donation = annual_income * fraction_donated

def print_values():
    saved_money = simulate_saving(career_length, annual_donation, growth_rate, inflation, donations_per_year)
    saved_adj = adjust_for_inflation(saved_money, inflation, career_length)
    instant = simulate_instant_donating(career_length, annual_income, fraction_donated)
    print(f"If you donated your money instantly you would donate " +
          f"{format_usd(instant)}.")
    print(f"If you saved your money rather than donating it directly you would " +
          f"have {format_usd(saved_money)} left at the end of your career, " +
          f"which is {format_usd(saved_adj)} adjusted for inflation")
    print(f"That's {(saved_adj / instant):.2f} times as much")

def print_disclaimer():
    print("DISCLAIMER: This is not the only thing to consider when making " +
          "this choice. Maybe your money is more valuable if donated now " +
          "rather than later. Maybe the impact of a donation decreases " +
          "exponentially over time the same way savings increase exponentially")

print()
print_values()
print()
if SHOW_DISCLAIMER:
    print_disclaimer()
print()
