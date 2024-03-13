import math
from scipy.stats import norm #normal distribution

#S = current price of asset
#K = strike price of option
#T = option's time to maturity in years
#r = risk free intrest rate as a decimal (<=1)
#sigma = volatility of asset

def BS_CallOption(S, K, T, r, sigma): #takes parameters into formula
    global call_option_price
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2)*T ) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    call_option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2) #estimated/fair value of call option price

current_price = int(input('Enter the current price of the asset($): '))
strike_price = int(input('Enter the strike price of the option($): '))
time_to_maturity = int(input("Enter the option's time to maturity in months: "))
time_to_maturity = time_to_maturity/12
risk_free_intrest_rate = float(input("Enter the current risk free intrest rate as a percentage(%): "))
risk_free_intrest_rate = risk_free_intrest_rate/100
volatility = float(input("Enter the volatility of the asset as a percentage(%): "))
volatility = volatility/100

BS_CallOption(current_price, strike_price, time_to_maturity, risk_free_intrest_rate, volatility)

print(f"\nOption's current value based on the Black-Scholes model: ${round(call_option_price, 2)}")
