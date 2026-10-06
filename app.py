"""
Minimal static-looking frontend based on the reference screenshot.
"""

import streamlit as st

st.set_page_config(page_title="QuantumPortfolioAI", page_icon="📈", layout="wide")

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #f3f3f3;
        color: #1e1e1e;
        font-family: "Segoe UI", sans-serif;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
        box-shadow: none;
    }

    .main-block-container {
        padding-top: 0.5rem;
    }

    .title {
        font-size: 3.1rem;
        font-weight: 800;
        text-align: center;
        color: #1d1d1d;
        margin-top: 0.2rem;
        margin-bottom: 0.5rem;
    }

    .divider {
        border-top: 1px solid rgba(0,0,0,0.15);
        margin-top: 0.75rem;
        margin-bottom: 0.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">QuantumPortfolioAI</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Leave the rest of the page intentionally empty to match the reference mockup.
# The screenshot shows a minimal title-only interface without visible controls.
st.empty()
