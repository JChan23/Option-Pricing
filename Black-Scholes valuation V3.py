import math
from scipy.stats import norm #normal distribution
import numpy as np

#S = current price of asset
#K = strike price of option
#T = option's time to maturity in years
#r = risk free intrest rate as a decimal (<=1)
#sigma = annual volatility of asset

def BS_CallOption(S, K, T, r, sigma): #takes parameters into formula
    global call_option_price
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2)*T ) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    call_option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2) #estimated/fair value of call option price

def MC_CallOption(S, K, T, r, sigma, num_simulations):
    global estimated_call_option_price
    option_prices = []

    # constants
    dt = T / 252  # set time interval to one trading day (252 trading days a year)
    drift = (r - 0.5 * sigma**2) * dt  # drift in time series
    volatility_over_time = sigma * np.sqrt(dt)

    for i in range(num_simulations):
        price_path = [S]  # map of price path as an array
        for j in range(252):
            random_price_movement = np.exp(drift + volatility_over_time * np.random.normal(0, 1))
            price_path.append(price_path[-1] * random_price_movement)  # add new price to array. calculated by previous price*movement
        option_payoff = max(price_path[-1] - K, 0)  # payoff will be the current price of the asset*the strike price. Since it is an option and not a future, trade does not have to be executed if net payoff is < 0. therefore min payoff = 0
        option_prices.append(option_payoff * np.exp(-r * T))  # reverse calculate option price based on payoff
    estimated_call_option_price = np.mean(option_prices)

def RangeCheck(item):
    global valid
    if item < 0:
        print("Please enter a number greater than or equal to 0 \n")
        valid = False

#input current asset price
valid = False
while valid == False:
    try:
        current_price = float(input('Enter the current price of the asset($): '))
        valid = True
        RangeCheck(current_price)
    except ValueError:
        print("Please enter a numeric value \n")

#input option strike price
valid = False
while valid == False:
    try:
        strike_price = float(input('Enter the strike price of the option($): '))
        valid = True
        RangeCheck(strike_price)
    except ValueError:
        print("Please enter a numeric value \n")

#input time to maturity
valid = False
while valid == False:
    try:
        time_to_maturity = int(input("Enter the option's time to maturity in months: "))
        valid = True
        RangeCheck(time_to_maturity)
    except ValueError:
        print("Please enter a numeric value \n")
time_to_maturity = time_to_maturity/12

#input risk free intrest rate
valid = False
while valid == False:
    try:
        risk_free_intrest_rate = float(input("Enter the current risk free intrest rate as a percentage(%): "))
        valid = True
        RangeCheck(risk_free_intrest_rate)
    except ValueError:
        print("Please enter a numeric value \n")
risk_free_intrest_rate = risk_free_intrest_rate/100

#input annual volatility
valid = False
while valid == False:
    try:
        volatility = float(input("Enter the annual volatility of the asset as a percentage(%): "))
        valid = True
        RangeCheck(volatility)
    except ValueError:
        print("Please enter a numeric value \n")
volatility = volatility/100

#call procedure
BS_CallOption(current_price, strike_price, time_to_maturity, risk_free_intrest_rate, volatility)
MC_CallOption(current_price, strike_price, time_to_maturity, risk_free_intrest_rate, volatility, 10000)

#output
print(f"\nOption's current value based on the Black-Scholes model: ${round(call_option_price, 2)}")
print(f"Option's restimated value based on the Monte Carlo simulation: ${round(estimated_call_option_price, 2)}")
