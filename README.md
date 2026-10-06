# QuantumPortifolioAI

QuantumPortifolioAI is a beginner-friendly portfolio optimization concept project that explores constrained portfolio selection using a simple QAOA-inspired approach.

This project is intentionally built without external quantum libraries, APIs, or live market data. It focuses on the core idea: selecting the best combination of assets based on return and risk while satisfying a fixed-size portfolio constraint.

## Project Idea

The concept behind this project is to model a portfolio as a set of assets and evaluate combinations of stocks to find the best group according to a simple score.

The score is calculated as:

score = average_return - risk_weight * average_risk

This creates a balance between:
- maximizing expected return
- minimizing portfolio risk
- enforcing a constrained choice of exactly 3 assets

Although the real project name mentions QAOA, this first version is a simplified classical prototype inspired by the same optimization thinking. It is designed for learning rather than live trading or production use.

## Included Files

- portfolio.py
  - Contains the sample stock dataset
  - Implements the scoring function
  - Uses itertools.combinations to evaluate all possible portfolios of exactly 3 stocks
  - Identifies the best-scoring portfolio

- main.py
  - Runs the optimizer
  - Prints the final report in the terminal

- index.html
  - A static website version of the concept
  - Displays a dark portfolio dashboard layout
  - Includes a simple interactive portfolio calculator in the browser

- app.py
  - Optional Streamlit version of the portfolio optimizer

## Sample Stocks Used

- AAPL
- MSFT
- GOOGL
- AMZN
- NVDA
- META
- JPM
- TSLA

Each stock includes:
- an example expected annual return
- a sample risk value

## Optimization Logic

1. Define a list of sample assets and their return/risk values.
2. Generate all combinations of 3 stocks.
3. For each portfolio:
   - calculate average return
   - calculate average risk
   - compute score = average_return - risk_weight * average_risk
4. Select the portfolio with the highest score.
5. Display the chosen stocks and performance metrics.

## How to Run

### Terminal version

```bash
cd /home/pavaniyadav093/quantum-portfolio
python3 main.py
```

### Website version

```bash
cd /home/pavaniyadav093/quantum-portfolio
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

### Streamlit version

```bash
cd /home/pavaniyadav093/quantum-portfolio
.venv/bin/streamlit run app.py --server.headless true --server.port 8501
```

Then open:

```text
http://localhost:8501
```

## Important Notes

- This project is educational and beginner-friendly.
- It does not use real-time financial data.
- It does not use quantum hardware, Qiskit, or external APIs.
- It is a simplified demo inspired by the concept of quantum portfolio optimization.

## Future Improvement Ideas

- Add adjustable portfolio constraints
- Add more sectors and assets
- Compare multiple risk weights
- Add charts and visual reports
- Build a real QAOA-inspired optimization formulation in a more advanced version

## License

This project is for learning and demonstration purposes.

