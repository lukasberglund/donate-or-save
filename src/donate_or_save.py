import math

"""
Calculate how much one could donate if one saved the money vs donating now
"""

def adjust_for_inflation(total, inflation, career_length):
    return total / math.pow(inflation, career_length)

def simulate_saving(career_length, annual_donation, growth_rate, inflation, donations_per_year):
    """
    calculate the amount of money you would have saved up if you set a certain
    FRACTION OF YOUR INCOME aside a certain NUMBER OF TIMES A YEAR for a certain
    NUMBER OF YEARS given an INFLATION RATE, GROWTH RATE OF YOUR SAVINGS, and
    ANNUAL DONATIONS
    """

    growth_rate_per_donation = math.pow(growth_rate, 1 / donations_per_year)
    inflation_per_donation = math.pow(inflation, 1 / donations_per_year)

    num_donations = career_length * donations_per_year
    amount_donated = annual_donation / donations_per_year # grows with inflation

    total = 0

    for _ in range(num_donations):
        total *= growth_rate_per_donation
        total += amount_donated

        amount_donated *= inflation_per_donation

    return total

def simulate_instant_donating(career_length, annual_income, fraction_donated):
    return career_length * annual_income * fraction_donated

def format_usd(x):
    return '${:,.2f}'.format(x)
