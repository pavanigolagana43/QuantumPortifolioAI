"""
Main entry point for the Quantum Portfolio Optimizer.

This script runs the portfolio optimization and displays a clean report
showing the optimal selection of 3 stocks based on return and risk balance.
"""

from portfolio import find_optimal_portfolio


def main():
    """
    Run the portfolio optimizer and display results.
    """
    # Configuration
    NUM_ASSETS = 3           # Select exactly 3 stocks
    RISK_WEIGHT = 0.5        # Balance between return and risk
    
    # Run the optimizer
    result = find_optimal_portfolio(num_assets=NUM_ASSETS, risk_weight=RISK_WEIGHT)
    
    # Extract results
    selected_stocks = result['stocks']
    avg_return = result['average_return']
    avg_risk = result['average_risk']
    score = result['score']
    num_combinations = result['num_combinations_tested']
    
    # Check constraint: exactly 3 assets selected
    constraint_satisfied = len(selected_stocks) == NUM_ASSETS
    
    # Display the report
    print("=" * 60)
    print("      QUANTUM PORTFOLIO OPTIMIZER")
    print("=" * 60)
    print()
    
    # Selected Stocks
    print("SELECTED PORTFOLIO:")
    print(f"  Stocks: {', '.join(selected_stocks)}")
    print()
    
    # Performance Metrics
    print("PERFORMANCE METRICS:")
    print(f"  Expected Return: {avg_return:.2%}")
    print(f"  Average Risk:    {avg_risk:.4f}")
    print(f"  Portfolio Score: {score:.4f}")
    print()
    
    # Portfolio Details
    print("PORTFOLIO DETAILS:")
    print(f"  Number of Assets: {len(selected_stocks)}")
    print(f"  Constraint (Exactly {NUM_ASSETS} Assets): {'✓ SATISFIED' if constraint_satisfied else '✗ NOT SATISFIED'}")
    print()
    
    # Optimization Info
    print("OPTIMIZATION INFO:")
    print(f"  Total Combinations Tested: {num_combinations}")
    print(f"  Risk Weight Factor: {RISK_WEIGHT}")
    print()
    
    print("=" * 60)


if __name__ == "__main__":
    main()
