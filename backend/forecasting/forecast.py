import pandas as pd
from prophet import Prophet
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(BASE_DIR, "..", "data/sales.csv"))

# Establish DataFrame
df = pd.read_csv(DATA)

# Establish the date column as a DatatimeIndex (necessary for Prophet)
df["date"] = pd.to_datetime(df["date"])


def create_forecast_for_product(df, index):
    """Create forecast for a given product using it's index"""

    # Create new Dataframe based off a single product using the given index
    df = df[df["product_id"] == index].copy()

    # Drop all unnecessary columns and establish the necessary columns for prophet
    df = df.drop(
        ["transaction_id", "product_id", "unit_price", "total_amount", "customer_id"],
        axis=1,
    )
    df = df.groupby("date", as_index=False)["quantity"].sum()
    df.columns = ["ds", "y"]

    # Begin training the prohet model with the dataframe
    m = Prophet(interval_width=0.95)
    m.fit(df)

    # Create the forecast for the next 100 days after the last transaction in the sales data
    future = m.make_future_dataframe(periods=100, freq="D")
    forecast = m.predict(future)

    # Narrow down the dataframe and make the columns more readable
    forecast = forecast[["ds", "yhat"]]
    forecast.columns = ["date", "predicted_sales"]

    # Add a product_id column and set it to the product index
    forecast.insert(0, "product_id", index)

    # Return the forecast
    return forecast


def create_main_forecast():
    # Empty list that new dataframes will be append to
    all_dfs = []

    # For loop that creates a forecast for each product and adds to the list of dataframes
    for i in range(1, 29):
        forecast = create_forecast_for_product(df, i)
        all_dfs.append(forecast)

    # Create concatanated dataframe with all product dataframes
    final_df = pd.concat(all_dfs, ignore_index=True)

    # Sort the dataframe so it lists the products by day
    final_df = final_df.sort_values(["date", "product_id"]).reset_index(drop=True)

    # Return the final dataframe
    return final_df
