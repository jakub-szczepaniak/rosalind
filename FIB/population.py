def population(months, offspring=1):
    if months < 2:
        return months
    else:
        return (population(months - 1, offspring) + population(months - 2, offspring) * offspring)
