
def reservoir_volume_calculator(reservoir_volume,rainfall):
    rainfall -= 0.1*rainfall
    reservoir_volume+= rainfall
    reservoir_volume+= reservoir_volume * (5/100)
    reservoir_volume-= reservoir_volume * (5/100) 

    rainfall -= 2.5e5
    return reservoir_volume

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

print(reservoir_volume_calculator(reservoir_volume,rainfall))
