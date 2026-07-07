import streamlit as st
import pandas as pd
import plotly.express as px
df=pd.read_csv("inventory_data.csv")
df["Inventory Value"]=df["Stock Quantity"]*df["Unit Cost"]
st.title("Inventory Management Dashboard")
st.metric("Total Inventory Value", f"${df['Inventory Value'].sum():,.0f}")
st.metric("Low Stock Items", int((df["Stock Quantity"]<=df["Reorder Level"]).sum()))
st.plotly_chart(px.bar(df,x="Product Name",y="Stock Quantity",color="Category"))
st.plotly_chart(px.pie(df,names="Category",values="Inventory Value"))
st.plotly_chart(px.bar(df.groupby("Supplier",as_index=False)["Inventory Value"].sum(),x="Supplier",y="Inventory Value"))
st.dataframe(df[df["Stock Quantity"]<=df["Reorder Level"]])
