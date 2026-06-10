# BUSINESS ASSUMPTIONS/CONSTANTS

from datetime import datetime
# from dataclasses import dataclass, field

# ------------------------
# Simulation Period
# ------------------------

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2025, 12, 31)

TARGET_YEARS = 3

# ------------------------
# Monthly Seasonality
# ------------------------

MONTH_MULTIPLIERS = {
    1: 0.90,
    2: 0.95,
    3: 1.00,
    4: 1.00,
    5: 1.05,
    6: 1.05,
    7: 0.95,
    8: 0.95,
    9: 1.00,
    10: 1.05,
    11: 1.20,
    12: 1.35,
}

# ------------------------
# Business Size
# ------------------------

TARGET_ORDERS = 7000

YEARLY_GROWTH = 0.10

BASE_ORDERS_PER_MONTH = 180

ORDER_NOISE_MIN = 0.90
ORDER_NOISE_MAX = 1.10

# ------------------------
# Customer Behaviour
# ------------------------

CHURN_RATE = 0.10

AT_RISK_RATE = 0.20

LOYAL_RATE = 0.70

NEW_CUSTOMERS_PER_QUARTER = 5

CUSTOMER_TIERS = {             # Proportion of each customer tier
    "enterprise": 0.10,
    "mid_market": 0.30,
    "small_business": 0.60,
}

CUSTOMER_PURCHASE_WEIGHT = {   # Weight of each customer tier in terms of purchase volume
    "enterprise": 10,
    "mid_market": 4,
    "small_business": 1,
}

# ------------------------
# Order Behaviour
# ------------------------

MIN_LINES_PER_ORDER = 1
MAX_LINES_PER_ORDER = 5

LINES_PER_ORDER = {
    1: 0.20,
    2: 0.35,
    3: 0.30,
    4: 0.10,
    5: 0.05,
}

ORDER_STATUS = {
    "Sales Order": 0.80,
    "Quotation": 0.15,
    "Cancelled": 0.05,
}

# ------------------------
# Discounts
# ------------------------

DISCOUNT_WEIGHTS = {
    0: 0.70,
    5: 0.15,
    10: 0.10,
    20: 0.05,
}

# ------------------------
# Product Behavior
# ------------------------

PRODUCT_CLASSES = {
    "fast": 0.20,
    "medium": 0.60,
    "slow": 0.20,
}

PRODUCT_WEIGHTS = {
    "fast": 15,
    "medium": 5,
    "slow": 1,
}

QUANTITY_BY_CLASS = {
    "fast": (2, 20),
    "medium": (1, 8),
    "slow": (1, 3),
}


# ------------------------
# Noise
# ------------------------

NOISE_MIN = 0.95
NOISE_MAX = 1.05