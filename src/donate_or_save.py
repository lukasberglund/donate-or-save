import math

"""
Calculate how much one could donate if one saved the money vs donating now
"""

CAREER_LENGTH = 40 # how many years you donate money for
ANNUAL_INCOME = 50000
FRACTION_DONATED = 0.1
GROWTH_RATE = 1.05
INFLATION = 1.02
DONATIONS_PER_YEAR = 12 # how frequently you donate (does not change total donations)

def adjust_for_inflation(total, inf = INFLATION, cl = CAREER_LENGTH):
    return total / math.pow(inf, cl)

def simulate_saving(cl = CAREER_LENGTH,
                    ai = ANNUAL_INCOME,
                    gr = GROWTH_RATE,
                    inf = INFLATION,
                    dpy = DONATIONS_PER_YEAR,
                    fd = FRACTION_DONATED):
    """
    calculate the amount of money you would have saved up if you set a certain
    FRACTION OF YOUR INCOME aside a certain NUMBER OF TIMES A YEAR for a certain
    NUMBER OF YEARS given an INFLATION RATE, GROWTH RATE OF YOUR SAVINGS, and
    ANNUAL INCOME
    """

    gr_per_donation = math.pow(gr, 1 / dpy)
    inf_per_donation = math.pow(inf, 1 / dpy)

    num_donations = cl * dpy
    donation_amount = ai * fd / dpy # grows with inflation

    total = 0

    for _ in range(num_donations):
        total *= gr_per_donation
        total += donation_amount

        donation_amount *= inf_per_donation

    return total

def simulate_instant_donating(cl = CAREER_LENGTH, ai = ANNUAL_INCOME, fd = FRACTION_DONATED):
    return cl * ai * fd

def format_usd(x):
    return '${:,.2f}'.format(x)
