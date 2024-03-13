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

#input volatility
valid = False
while valid == False:
    try:
        volatility = float(input("Enter the volatility of the asset as a percentage(%): "))
        valid = True
        RangeCheck(volatility)
    except ValueError:
        print("Please enter a numeric value \n")
volatility = volatility/100

#call procedure
BS_CallOption(current_price, strike_price, time_to_maturity, risk_free_intrest_rate, volatility)

#output
print(f"\nOption's current value based on the Black-Scholes model: ${round(call_option_price, 2)}")
