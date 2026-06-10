from generators.loader import OdooLoader


def main():

    loader = OdooLoader("data/raw")

    tables = loader.load()

    print()

    print("Customers")

    print(tables["customers"].head())

    print()

    print("Products")

    print(tables["products"].head())


if __name__ == "__main__":

    main()