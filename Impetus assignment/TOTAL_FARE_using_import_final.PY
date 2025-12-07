from typing import final
CHARGES:Final=3
distance_travelled_in_km = eval(input("Enter the distance travelled by the traveller in km:"))
age = input("Enter the age of the Citize in years:")
DISCOUNT_RATE:Final = 0.5

if age >= 60:
print("The Total fare to be charged is:",(distance_travelled_in_km * CHARGES)/DISCOUNT_RATE)
