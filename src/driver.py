from donate_or_save import *

SHOW_DISCLAIMER = True

def print_values():
    saved_money = simulate_saving()
    saved_adj = adjust_for_inflation(saved_money)
    instant = simulate_instant_donating()
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
