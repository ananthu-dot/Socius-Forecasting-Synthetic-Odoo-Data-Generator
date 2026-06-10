from pathlib import Path

import pandas as pd


class OdooLoader:

    def __init__(self, raw_folder):

        self.raw_folder = Path(raw_folder)

    def load(self):

        return {

            "orders": pd.read_excel(
                self.raw_folder / "Sales Order (sale.order).xlsx"
            ),

            "order_lines": pd.read_excel(
                self.raw_folder / "Sales Order (sale.order.line).xlsx"
            ),

            "products": pd.read_excel(
                self.raw_folder / "Product (product.product).xlsx"
            ),

            "product_categories": pd.read_excel(
                self.raw_folder / "Product (product.category).xlsx"
            ),

            "customers": pd.read_excel(
                self.raw_folder / "Contact (res.partner).xlsx"
            ),
        }
    
# Test
loader = OdooLoader("data/raw")

tables = loader.load()

products = tables["products"]
customers = tables["customers"]
print(products.head())