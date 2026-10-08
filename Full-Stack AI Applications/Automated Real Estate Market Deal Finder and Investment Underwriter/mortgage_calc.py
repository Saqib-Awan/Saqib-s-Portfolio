"""
Mortgage and Cashflow Amortization Formulas
"""

def calculate_monthly_mortgage(principal: float, rate_annual: float, years: int = 30) -> float:
    r = rate_annual / 12.0
    n = years * 12
    return principal * (r * (1 + r)**n) / ((1 + r)**n - 1)