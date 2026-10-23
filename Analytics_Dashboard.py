import datetime
import random

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


REGIONS = ["North America", "Europe", "Asia", "South America"]
CATEGORIES = ["Electronics", "Fashion", "Home", "Others"]
PRODUCTS = {
    "Electronics": ["Laptop", "Phone", "Tablet", "Smartwatch"],
    "Fashion": ["Jacket", "Sneakers", "Bag", "Watch"],
    "Home": ["Lamp", "Chair", "Desk", "Cookware"],
    "Others": ["Books", "Stationery", "Gift Set", "Accessories"],
}
CUSTOMERS = [
    "Ava Lee",
    "Noah Patel",
    "Mia Johnson",
    "Liam Chen",
    "Emma Garcia",
    "Lucas Brown",
    "Olivia Smith",
    "Ethan Williams",
]


def generate_sample_data(days: int = 90) -> pd.DataFrame:
    """Generate a realistic sample sales dataset for the dashboard."""
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days - 1)
    dates = pd.date_range(start=start_date, end=end_date, freq="D")

    rows = []
    for current_date in dates:
        for region in REGIONS:
            for category, products in PRODUCTS.items():
                for product in products:
                    sales = random.randint(180, 900)
                    customers = random.randint(10, 80)
                    orders = random.randint(4, 30)
                    profit = round(random.uniform(8, 28), 2)
                    status = random.choice(["Completed", "Pending", "Shipped"])
                    customer = random.choice(CUSTOMERS)
                    rows.append(
                        {
                            "date": pd.Timestamp(current_date),
                            "region": region,
                            "category": category,
                            "product": product,
                            "sales": sales,
                            "customers": customers,
                            "orders": orders,
                            "profit_margin": profit,
                            "status": status,
                            "customer": customer,
                        }
                    )

    return pd.DataFrame(rows)


def filter_data(df: pd.DataFrame, region: str, category: str, days: str) -> pd.DataFrame:
    """Apply user-selected filters to the data."""
    filtered = df.copy()
    if region != "All Regions":
        filtered = filtered[filtered["region"] == region]
    if category != "All":
        filtered = filtered[filtered["category"] == category]

    day_count = {"7 Days": 7, "30 Days": 30, "90 Days": 90}.get(days, 30)
    cutoff = pd.Timestamp(datetime.date.today()) - pd.Timedelta(days=day_count - 1)
    filtered = filtered[filtered["date"] >= cutoff]
    return filtered


def compute_kpis(df: pd.DataFrame) -> dict:
    """Calculate revenue, customer, growth, and average order value KPIs."""
    total_revenue = float(df["sales"].sum())
    total_customers = int(df["customers"].sum())
    total_orders = int(df["orders"].sum())
    avg_order_value = total_revenue / total_orders if total_orders else 0

    previous_days = max(1, len(df["date"].unique()) // 2)
    previous_cutoff = pd.Timestamp(datetime.date.today()) - pd.Timedelta(days=previous_days)
    prior_window = df[df["date"] < previous_cutoff]
    prior_revenue = float(prior_window["sales"].sum()) if not prior_window.empty else 0
    sales_growth = ((total_revenue - prior_revenue) / prior_revenue * 100) if prior_revenue else 0

    return {
        "total_revenue": total_revenue,
        "total_customers": total_customers,
        "sales_growth": sales_growth,
        "avg_order_value": avg_order_value,
    }


st.set_page_config(page_title="Analytics Dashboard", layout="wide")
st.title("📊 Business Analytics Dashboard")

sample_data = generate_sample_data()

st.sidebar.header("Filter Data")
region = st.sidebar.selectbox("Region", ["All Regions", *REGIONS])
category = st.sidebar.selectbox("Product Category", ["All", *CATEGORIES])
days = st.sidebar.selectbox("Time Range", ["7 Days", "30 Days", "90 Days"])

filtered_df = filter_data(sample_data, region, category, days)

kpis = compute_kpis(filtered_df)

st.subheader("Key Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}", f"{kpis['sales_growth']:.1f}%")
with col2:
    st.metric("New Customers", f"{kpis['total_customers']:,}", "+4.6%")
with col3:
    st.metric("Sales Growth", f"{kpis['sales_growth']:.1f}%", "+2.1%")
with col4:
    st.metric("Avg. Order Value", f"${kpis['avg_order_value']:,.0f}", "+3.4%")

sales_by_day = filtered_df.groupby("date", as_index=False)["sales"].sum()
fig_sales = px.line(sales_by_day, x="date", y="sales", title="Sales Overview")
st.plotly_chart(fig_sales, use_container_width=True)

category_totals = filtered_df.groupby("category", as_index=False)["sales"].sum()
fig_donut = go.Figure(
    data=[
        go.Pie(
            labels=category_totals["category"],
            values=category_totals["sales"],
            hole=0.5,
            title="Category Mix",
        )
    ]
)
st.plotly_chart(fig_donut, use_container_width=True)

product_totals = filtered_df.groupby("product", as_index=False)["sales"].sum().sort_values("sales", ascending=False).head(5)
fig_products = px.bar(
    product_totals,
    x="product",
    y="sales",
    title="Top Products",
    labels={"product": "Product", "sales": "Revenue"},
)
st.plotly_chart(fig_products, use_container_width=True)

st.subheader("Recent Orders")
recent_orders = filtered_df[["customer", "product", "status", "sales"]].sort_values("sales", ascending=False).head(8)
st.dataframe(recent_orders, use_container_width=True)
