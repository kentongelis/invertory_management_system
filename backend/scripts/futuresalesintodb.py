from backend.server.app import app
from backend.server.extensions import db
from backend.models.data_models import Future_Sales
from backend.forecasting.forecast import create_main_forecast


def load_future_sales():
    df = create_main_forecast()

    records = []

    for _, row in df.iterrows():
        record = Future_Sales(
            product_id=int(row["product_id"]),
            date=row["date"].strftime("%Y-%m-%d"),
            predicted_sales=float(row["predicted_sales"]),
        )
        records.append(record)

    db.session.bulk_save_objects(records)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        print("Adding future sales into database...")

        load_future_sales()

        print("Successfully added all future sales data.")
