import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Helper Function
def create_weather_situation_df(df):
    weather_situation_df = df.groupby(by="weathersit").cnt.mean().reset_index()
    weather_situation_df.rename(columns={
        "weathersit": "weather_situation"
    }, inplace=True)
    return weather_situation_df

def create_weekday_df(df):
    weekday_df = df.groupby(by="weekday").cnt.mean().sort_values(ascending=False).reset_index()
    return weekday_df

def create_season_day_df(df):
    season_day_df = df.groupby(by="season").agg({
        "casual": "mean",
        "registered": "mean"
    })
    return season_day_df

def create_holiday_df(df):
    holiday_df = df.groupby("holiday").cnt.mean().reset_index()
    holiday_df["holiday"] = holiday_df["holiday"].replace({0: "Not Holiday", 1: "Holiday"})
    return holiday_df

def create_clustrering_df(df):
    clustering_df = df[["instant","temp"]]
    clustering_df.rename(columns={"temp": "temperature"}, inplace=True)
    max_temp = clustering_df["temperature"].max()
    bins = [0, (1/3) * max_temp, (2/3) * max_temp, max_temp] 
    labels = ["Low Temp", "Medium Temp", "High Temp"]
    clustering_df["temperature_category"] = pd.cut(clustering_df["temperature"], bins=bins, labels=labels, include_lowest=True)
    return clustering_df


# Main Program
cleaned_df = pd.read_csv("dashboard/cleaned_day.csv")

min_date = pd.to_datetime(cleaned_df["dteday"]).dt.date.min()
max_date = pd.to_datetime(cleaned_df["dteday"]).dt.date.max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

primary_df = cleaned_df[(cleaned_df["dteday"] >= str(start_date)) &
                        (cleaned_df["dteday"] <= str(end_date))]

weather_situation_df = create_weather_situation_df(primary_df)
weekday_df = create_weekday_df(primary_df)
season_day_df = create_season_day_df(primary_df)
holiday_df = create_holiday_df(primary_df)
clustering_df = create_clustrering_df(primary_df)



st.header('Bike Rental Dashboard')

# Weather Situation
st.subheader('Impact of Weather on Average Customers')
fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#31C7E1", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="weather_situation",
    y="cnt",
    data=weather_situation_df,
    palette=colors,
    ax=ax
)
ax.set_title("Average Number of Customers by Weather Situation", loc="center", fontsize=35)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=25)
st.pyplot(fig)

# Best & Worst Average Customers by Weekday
st.subheader('Best & Worst Average Customers by Weekday')
fig, ax = plt.subplots(figsize=(20,10))
colors = ["#31C7E1", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#E14B31"]
sns.barplot(
    x="cnt",
    y="weekday",
    data=weekday_df,
    palette=colors,
    ax=ax
)
ax.set_title("Average Number of Customers by Weekday", loc="center", fontsize=35)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=25)
st.pyplot(fig)

# Impact of Season on Average Customers
st.subheader('Impact of Season on Average Customers')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(x="season", y ="casual", data=season_day_df, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Casual Customer", loc="center", fontsize=50)
ax[0].tick_params(axis='x', labelsize=30)
ax[0].tick_params(axis="y", labelsize=35)

sns.barplot(x="season", y="registered", data=season_day_df, palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("Registered Customer", loc="center", fontsize=50)
ax[1].tick_params(axis='x', labelsize=30)
ax[1].tick_params(axis="y", labelsize=35)

st.pyplot(fig)

# Average Bike Rentals on Non-Holiday vs Holiday
st.subheader("Average Bike Rentals on Non-Holiday vs Holiday")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="holiday",
    y="cnt",
    data=holiday_df,
    palette=colors,
    ax=ax
)
ax.set_title("Average Number of Customer by Holiday", loc="center", fontsize=35)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=25)
ax.tick_params(axis='x', labelsize=25)
st.pyplot(fig)

# Clustering Temperature with Binning
st.subheader("Clustering Temperature with Binning")
labels = ["Low Temp", "Medium Temp", "High Temp"]

fig, ax = plt.subplots(figsize=(8, 5))
colors = {'Low Temp': 'blue', 'Medium Temp': 'orange', 'High Temp': 'red'}
ax.scatter(x=clustering_df["instant"], y=clustering_df["temperature"],
            c=clustering_df["temperature_category"].map(colors), alpha=0.6)
ax.set_xlabel("Index")
ax.set_ylabel("Temperature")
ax.set_title("Temperature Clustering with Binning")
ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[label], markersize=8, label=label) for label in labels])
st.pyplot(fig)

st.caption('Copyright (c) Rio Octaviannus Loka 2025')