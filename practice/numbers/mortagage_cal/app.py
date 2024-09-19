"""
P = L[c(1 + c)^n]/[(1 + c)^n - 1]. 
In this formula, P represents the fixed monthly payment, 
L is the loan amount, 
c is the monthly interest rate, and 
n is the number of monthly payments or the loan term

 Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
 Also figure out how long it will take the user to pay back the loan. 
 For added complexity, add an option for users to select the compounding interval 
 (Monthly, Weekly, Daily, Continually).
"""
from math import pow, ceil, floor

def cal_mortgage(loan:float, rate:float, term:int):
    
    rate_term: float = (1 + (((rate / 100)/ 12))) ** term

    first_half: float = floor((loan * (((rate / 100) / 12)) * rate_term))
    second_half: float = rate_term - 1.00

    fixed: float = first_half / second_half
    
    return ceil(fixed) 