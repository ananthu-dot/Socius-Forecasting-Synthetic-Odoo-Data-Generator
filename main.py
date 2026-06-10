from generators.loader import OdooLoader
import generators.util
import pandas as pd


def main():

    loader = OdooLoader("data/raw")

    tables = loader.load()

    orders_df = generators.util.normalize_column_names(tables["orders"])
    orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])

    order_lines_df = generators.util.normalize_column_names(tables["order_lines"])

    products_df = generators.util.normalize_column_names(tables["products"])

    product_categories_df = generators.util.normalize_column_names(tables["product_categories"])

    customers_df = generators.util.normalize_column_names(tables["customers"])


    print("\nOrders")

    print(orders_df.head())

    print("\nOrders Lines")

    print(order_lines_df.head())

    print("\nProducts")

    print(products_df.head())


if __name__ == "__main__":

    main()