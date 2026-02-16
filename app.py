import streamlit as st
import numpy as np
from simulator import run_simulation
from risk_engine import kelly_fraction

st.set_page_config(page_title="Bet Analytics Bot", layout="wide")

st.title("🎯 Betting Strategy Analytics Dashboard")

game = st.selectbox(
    "Game Type",
    ["Crash", "AppleOfFortune", "Mines", "Kamikaze", "RoyalFeast"]
)

bankroll = st.number_input("Bankroll", 10, 100000, 1000)
rounds = st.slider("Simulation Rounds", 100, 50000, 5000)
bet_size = st.number_input("Base Bet", 1, 1000, 10)

if st.button("Run Simulation"):
    results = run_simulation(game, bankroll, bet_size, rounds)

    st.subheader("Results")
    st.write(results["summary"])

    st.line_chart(results["history"])

    edge = results["summary"]["roi"]
    kelly = kelly_fraction(edge, 2)

    st.metric("Suggested Kelly Fraction", round(kelly, 4))
