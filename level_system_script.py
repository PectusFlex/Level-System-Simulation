### ONLY CHANGE THESE VALUES AND RUN THE SCRIPT TO PLAY AROUND ######
k = 10 # Cut off Level
a = 25 # Linear Growth factor
b = 1.1 # Exponential growth factor
base_xp = 75
max_level = 25


### DO NOT TOUCH THIS ###
xp_linear = base_xp*k + a*(k*(k-1)/2)
xp_exponential = (base_xp + k*a) * (1-pow(b, 30-k))/(1-b)
total_xp = xp_linear + xp_exponential
cutofflevel_linear = base_xp + a*k

xp_nostreak = 151
xp_2daystreak = xp_nostreak * 1.25
xp_4daystreak = xp_nostreak * 1.5
xp_level30 = 13363.5

def xpNeededForNextLevelLinear(level):
    return base_xp + a*level

def xpNeededForNextLevelExponential(level):
    return cutofflevel_linear * pow(b, (level-k))

# Simulation variables
days_of_exercise = 0
level = 1
current_xp = 0
total_xp = 0
print("---------Linear XP Phase Simulation---------")
while total_xp < xp_linear:
    if days_of_exercise == 0 or days_of_exercise == 1:
        current_xp += xp_nostreak
        total_xp += xp_nostreak
    elif days_of_exercise == 2 or days_of_exercise == 3:
        current_xp += xp_2daystreak
        total_xp += xp_2daystreak
    elif days_of_exercise >= 4:
        current_xp += xp_4daystreak
        total_xp += xp_4daystreak
    while current_xp >= xpNeededForNextLevelLinear(level):
        current_xp -= xpNeededForNextLevelLinear(level)
        level += 1
    days_of_exercise += 1
    print("----------")
    print(f"Day {days_of_exercise}")
    print(f"XP needed for next level: {int(xpNeededForNextLevelLinear(level))}")
    print(f"Current XP: {int(current_xp)}")
    print(f"Total XP: {int(total_xp)}")
    print(f"Level: {level}")
cutoff_days = days_of_exercise
print("---------Exponential XP Phase Simulation---------")
while total_xp < xp_level30:
    current_xp += xp_4daystreak
    total_xp += xp_4daystreak
    while current_xp >= xpNeededForNextLevelExponential(level):
       current_xp -= xpNeededForNextLevelExponential(level)
       level += 1
    days_of_exercise += 1
    print("----------")
    print(f"Day {days_of_exercise}")
    print(f"XP needed for next level: {int(xpNeededForNextLevelExponential(level))}")
    print(f"Current XP: {int(current_xp)}")
    print(f"Total XP: {int(total_xp)}")
    print(f"Level: {level}")
    if days_of_exercise > 60:
        break

print("------------------------------------------")

print(f'Linear XP: {xp_linear}')
print(f'Exponential XP: {xp_exponential}')
print(f'Total XP: {total_xp}')
print(f"It takes {cutoff_days} days until cut off is reached") 