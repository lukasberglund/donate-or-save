from donate_or_save import *

import time
import sys

SLEEP_TIME = 0.7
SHOW_DISCLAIMER = True

defaults = {
    'career_length': 40, # how many years you donate money for
    'annual_income': 50000,
    'fraction_donated': 0.1,
    'growth_rate': 1.06,
    'inflation': 1.02,
    'donations_per_year': 12 # how frequently you donate (does not change total donations)
}

"""
questions asked to user to ascertain certain values
"""
default_qs = {
    'career_length': 'How many years will you make money for?',
    'annual_income': 'How much will you make each year on average (after tax)?',
    'fraction_donated': 'Of that what fraction will you donate?',
    'growth_rate': 'By what rate will your savings grow each year on average?',
    'inflation': 'What will the average annual inflation rate be?',
    'donations_per_year': 'How many times a year will you donate your money?'
}

def print_(x):
    print(x)
    time.sleep(SLEEP_TIME)
    print()

def clear_line():
    """
    Clear line in stdout
    """
    
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def input_(x):
    user_input = input(x)
    clear_line()

    return user_input

def ask_yes_no(question):
    answer = input_(question + " (y/n) ")

    if answer in ['y', 'yes']:
        return True
    elif answer in ['n', 'no']:
        return False
    else:
        print_("Please write either \'y\' or \'n\'")
        return ask_yes_no(question)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def change_default(name, default):
    question = f"{default_qs[name]} (default: {default}) "
    answer = input_(question)

    if is_number(answer):
        try:
            return int(answer)
        except ValueError:
            return float(answer)
    elif answer == "":
        return default
    else:
        print_("Please input some kind of number")
        return change_default(name, default)

def change_defaults(defaults):
    print_("To use defaults simply type write nothing.")


    for name, default_val in defaults.items():

        defaults[name] = change_default(name, default_val)

    return defaults


def print_values():
    saved_money = simulate_saving(career_length, annual_donation, growth_rate, inflation, donations_per_year)
    saved_adj = adjust_for_inflation(saved_money, inflation, career_length)
    instant = simulate_instant_donating(career_length, annual_income, fraction_donated)
    print_(f"If you donated your money instantly you would donate " +
          f"{format_usd(instant)}.")
    print_(f"If you saved your money rather than donating it directly you would " +
          f"have {format_usd(saved_money)} left at the end of your career, " +
          f"which is {format_usd(saved_adj)} adjusted for inflation")
    print_(f"That's {(saved_adj / instant):.2f} times as much")

def print_disclaimer():
    print_("DISCLAIMER: This is not the only thing to consider when making " +
          "this choice. Maybe your money is more valuable if donated now " +
          "rather than later. Maybe the impact of a donation decreases " +
          "exponentially over time the same way savings increase exponentially")

if ask_yes_no('Use custom values?'):

    defaults = change_defaults(defaults)

career_length, annual_income, fraction_donated, growth_rate, inflation, donations_per_year = tuple(defaults.values())
annual_donation = annual_income * fraction_donated


print_values()

if SHOW_DISCLAIMER:
    print_disclaimer()
