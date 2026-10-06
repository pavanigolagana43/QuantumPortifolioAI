"""
Dark dashboard UI for the quantum portfolio optimizer.
"""

import streamlit as st

from portfolio import find_optimal_portfolio


# Global page settings
st.set_page_config(page_title="QuantumPortfolio AI", page_icon="📈", layout="wide")

# Custom CSS to match the dashboard look and feel in the reference design
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(90deg, #020b15 0%, #061b2c 45%, #0a2140 100%);
        color: #e9f3ff;
        font-family: "Segoe UI", sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }

    .main-block-container {
        padding-top: 1.2rem;
    }

    .dashboard-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #eaf6ff;
        margin: 0;
        padding: 0;
    }

    .dashboard-label {
        font-size: 0.8rem;
        letter-spacing: 0.18rem;
        color: #8ab7d8;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }

    .workflow-pill {
        background: rgba(78, 159, 255, 0.12);
        border: 1px solid rgba(98, 172, 255, 0.35);
        color: #7cc7ff;
        border-radius: 999px;
        padding: 0.75rem 1.25rem;
        text-align: center;
        font-weight: 700;
        width: fit-content;
        margin-left: auto;
        margin-top: 0.9rem;
    }

    .panel {
        background: rgba(10, 25, 38, 0.8);
        border: 1px solid rgba(124, 166, 204, 0.12);
        border-radius: 22px;
        padding: 1.4rem 1.2rem 1rem 1.2rem;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.18);
        margin-bottom: 1rem;
    }

    .panel h3 {
        margin-top: 0;
        margin-bottom: 1rem;
        color: #eff8ff;
        font-size: 1.1rem;
    }

    .metric-box {
        background: rgba(11, 28, 42, 0.9);
        border: 1px solid rgba(122, 156, 190, 0.18);
        border-radius: 14px;
        padding: 0.9rem 0.8rem;
        text-align: center;
        height: 100%;
    }

    .metric-box .label {
        color: #8aa8c3;
        font-size: 0.74rem;
        text-transform: uppercase;
        letter-spacing: 0.08rem;
    }

    .metric-box .value {
        margin-top: 0.55rem;
        font-size: 1.4rem;
        font-weight: 800;
        color: #eefaff;
    }

    .status-live {
        background: rgba(63, 192, 136, 0.15);
        border: 1px solid rgba(76, 215, 154, 0.5);
        color: #7ee7b1;
        border-radius: 999px;
        padding: 0.4rem 0.7rem;
        font-size: 0.7rem;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.08rem;
        margin-left: auto;
    }

    .soft-input {
        background: rgba(15, 27, 38, 0.8);
        border: 1px solid rgba(152, 183, 210, 0.15);
        color: #eaf7ff;
        border-radius: 10px;
    }

    div[data-testid="stSlider"] > div {
        background: rgba(15, 27, 38, 0.8);
    }

    .stButton > button {
        width: 100%;
        border: none;
        border-radius: 12px;
        background: linear-gradient(90deg, #56b7ff 0%, #6d8efd 100%);
        color: #08131b;
        font-weight: 800;
        height: 3rem;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #6ec4ff 0%, #80a6ff 100%);
    }

    .result-card {
        background: rgba(13, 29, 41, 0.9);
        border: 1px solid rgba(138, 190, 235, 0.15);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        margin-top: 1rem;
    }

    .tiny {
        font-size: 0.75rem;
        color: #8aa8c3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Application layout and values
with st.container():
    header_col, right_col = st.columns([4, 1])
    with header_col:
        st.markdown('<div class="dashboard-label">Quantum Investment Optimizer</div>', unsafe_allow_html=True)
        st.markdown('<div class="dashboard-title">QuantumPortfolio AI</div>', unsafe_allow_html=True)
    with right_col:
        st.markdown('<div class="workflow-pill">QAOA workflow</div>', unsafe_allow_html=True)

left_panel, right_panel = st.columns([0.9, 1.8])

with left_panel:
    with st.container():
        st.markdown(
            """
            <div class="panel">
                <h3>Portfolio Inputs</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )

        investment_amount = st.number_input("Investment Amount", min_value=1000, value=95000, step=1000)
        investment_period = st.number_input("Investment Period (months)", min_value=1, value=24, step=1)
        number_of_assets = st.number_input("Number of Assets", min_value=3, max_value=8, value=6, step=1)
        minimum_return = st.number_input("Minimum Return (%)", min_value=0, max_value=100, value=30, step=1)

        risk_tolerance = st.slider("Risk Tolerance (%)", min_value=0, max_value=100, value=50, step=1)

        risk_preference = st.selectbox(
            "Risk Preference",
            ["Balanced", "Conservative", "Aggressive"],
            index=0,
        )

        selected_sectors = st.multiselect(
            "Asset Sectors",
            ["Technology", "Finance", "AI", "Consumer", "Energy", "Healthcare"],
            default=["Technology", "Finance"],
        )

        st.markdown("<br>", unsafe_allow_html=True)
        optimize_clicked = st.button("Optimize Portfolio")

with right_panel:
    st.markdown(
        """
        <div class="panel">
            <div style="display:flex; align-items:center; justify-content:space-between; gap: 1rem;">
                <h3 style="margin:0;">Quantum Optimization Run</h3>
                <div class="status-live">Live</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metric_cols = st.columns(4)
    with metric_cols[0]:
        st.markdown('<div class="metric-box"><div class="label">Algorithm</div><div class="value">QAOA</div></div>', unsafe_allow_html=True)
    with metric_cols[1]:
        st.markdown('<div class="metric-box"><div class="label">Qubits</div><div class="value">--</div></div>', unsafe_allow_html=True)
    with metric_cols[2]:
        st.markdown('<div class="metric-box"><div class="label">Depth</div><div class="value">--</div></div>', unsafe_allow_html=True)
    with metric_cols[3]:
        st.markdown('<div class="metric-box"><div class="label">Shots</div><div class="value">--</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.write("Searching feasible portfolios...")

    risk_weight = risk_tolerance / 100.0
    if optimize_clicked:
        result = find_optimal_portfolio(num_assets=3, risk_weight=risk_weight)
        selected_stocks = ", ".join(result["stocks"])
        avg_return = result["average_return"]
        avg_risk = result["average_risk"]
        score = result["score"]

        st.markdown("<div style='margin-top:1rem;'><div class='tiny'>Selected portfolio</div></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='margin-top:0.2rem; color:#ebf7ff;'>{selected_stocks}</h3>", unsafe_allow_html=True)

        score_cols = st.columns(3)
        with score_cols[0]:
            st.markdown(f'<div class="metric-box"><div class="label">Expected Return</div><div class="value">{avg_return:.2%}</div></div>', unsafe_allow_html=True)
        with score_cols[1]:
            st.markdown(f'<div class="metric-box"><div class="label">Avg Risk</div><div class="value">{avg_risk:.4f}</div></div>', unsafe_allow_html=True)
        with score_cols[2]:
            st.markdown(f'<div class="metric-box"><div class="label">Score</div><div class="value">{score:.4f}</div></div>', unsafe_allow_html=True)

        st.write(f"Assets selected: {len(result['stocks'])}")
        st.write(f"Constraint satisfied: {'Yes' if len(result['stocks']) == 3 else 'No'}")
        st.write(f"Combinations tested: {result['num_combinations_tested']}")

    st.markdown('</div>', unsafe_allow_html=True)

# Keep the default screen looking similar to the mockup even before clicking
if not optimize_clicked:
    st.markdown(
        """
        <div style="margin-top: 1rem; color: #98b7d6; font-size: 0.9rem;">
            The optimizer will evaluate all 3-asset portfolio combinations and pick the best one based on return minus risk penalty.
        </div>
        """,
        unsafe_allow_html=True,
    )
