def min_flips(coins):
    heads = coins.count('О')
    tails = coins.count('Р')
    
    return min(heads, tails)
    
coins = input("ввести расположение моенток")
min_flips_count = min_flips(coins)
print(min_flips_count)