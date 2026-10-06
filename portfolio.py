"""
Portfolio optimizer module for constrained portfolio selection.

This module provides sample stock data and an optimization function
to find the best portfolio of exactly 3 stocks based on returns and risk.
"""

from itertools import combinations


# Sample stock data: name -> (expected_annual_return, risk_value)
# These are simplified sample values for demonstration purposes
STOCKS = {
    "AAPL": (0.12, 0.18),      # Apple: 12% return, 0.18 risk
    "MSFT": (0.10, 0.16),      # Microsoft: 10% return, 0.16 risk
    "GOOGL": (0.11, 0.17),     # Google: 11% return, 0.17 risk
    "AMZN": (0.14, 0.22),      # Amazon: 14% return, 0.22 risk
    "NVDA": (0.18, 0.28),      # NVIDIA: 18% return, 0.28 risk (high risk, high return)
    "META": (0.09, 0.24),      # Meta: 9% return, 0.24 risk
    "JPM": (0.08, 0.15),       # JPMorgan: 8% return, 0.15 risk (lower risk)
    "TSLA": (0.16, 0.30),      # Tesla: 16% return, 0.30 risk (very volatile)
}


def calculate_score(portfolio, risk_weight):
    """
    Calculate the score for a portfolio.
    
    The score balances return and risk:
    score = average_return - risk_weight * average_risk
    
    Args:
        portfolio (tuple): Tuple of stock symbols (e.g., ("AAPL", "MSFT", "GOOGL"))
        risk_weight (float): Weight for risk penalty (higher = more risk-averse)
    
    Returns:
        tuple: (average_return, average_risk, score)
    """
    # Extract returns and risks for the selected stocks
    returns = [STOCKS[stock][0] for stock in portfolio]
    risks = [STOCKS[stock][1] for stock in portfolio]
    
    # Calculate averages
    average_return = sum(returns) / len(returns)
    average_risk = sum(risks) / len(risks)
    
    # Calculate score: favor higher returns, penalize higher risk
    score = average_return - risk_weight * average_risk
    
    return average_return, average_risk, score


def find_optimal_portfolio(num_assets=3, risk_weight=0.5):
    """
    Find the optimal portfolio by testing all combinations of exactly num_assets stocks.
    
    Uses brute-force combinatorial search to evaluate every possible combination
    and select the one with the highest score.
    
    Args:
        num_assets (int): Number of assets to select (default: 3)
        risk_weight (float): Weight for risk in score calculation (default: 0.5)
    
    Returns:
        dict: Dictionary containing:
            - 'stocks': tuple of selected stock symbols
            - 'average_return': average expected annual return
            - 'average_risk': average risk value
            - 'score': calculated portfolio score
            - 'num_combinations_tested': total combinations evaluated
    """
    # Get all stock symbols
    all_stocks = list(STOCKS.keys())
    
    # Generate all possible combinations of exactly num_assets stocks
    all_combinations = list(combinations(all_stocks, num_assets))
    
    # Initialize variables to track the best portfolio
    best_portfolio = None
    best_score = float("-inf")  # Start with worst possible score
    best_return = 0
    best_risk = 0
    
    # Evaluate each combination
    for portfolio in all_combinations:
        avg_return, avg_risk, score = calculate_score(portfolio, risk_weight)
        
        # Update best portfolio if this one scores higher
        if score > best_score:
            best_score = score
            best_portfolio = portfolio
            best_return = avg_return
            best_risk = avg_risk
    
    # Return results
    return {
        'stocks': best_portfolio,
        'average_return': best_return,
        'average_risk': best_risk,
        'score': best_score,
        'num_combinations_tested': len(all_combinations),
    }
