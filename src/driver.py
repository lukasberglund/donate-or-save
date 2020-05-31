from donate_or_save import *

print(format_usd(simulate_saving()))
print(format_usd(adjust_for_inflation(simulate_saving())))
print(format_usd(simulate_instant_donating()))
