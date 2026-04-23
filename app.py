import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.optimization import calculate_optimal_stock

st.set_page_config(page_title="Licious Demand Optimizer", layout="wide")
st.title("🥩 Licious: Fresh Inventory & Waste Optimizer")

df = pd.read_csv('data/licious_demand.csv')
product = st.sidebar.selectbox("Select Product SKU", df['Product'].unique())

prod_df = df[df['Product'] == product]
mean_demand = prod_df['Demand'].mean()
std_demand = prod_df['Demand'].std()
price = prod_df['Price'].iloc[0]
cost = prod_df['Cost'].iloc[0]

opt_q, service_level = calculate_optimal_stock(mean_demand, std_demand, price, cost)

col1, col2, col3 = st.columns(3)
col1.metric("Recommended Stock Level", f"{opt_q} Units")
col2.metric("Target Service Level", f"{service_level:.1%}")
col3.metric("Current Spoilage Risk", f"{(1-service_level):.1%}")

st.subheader("Historical Demand Trends")
st.line_chart(prod_df.set_index('Date')['Demand'])

st.info(f"Summary: To maximize profit for {product}, the manager should stock {opt_q} units daily. This balances the high cost of spoilage against the revenue of fresh sales.")
