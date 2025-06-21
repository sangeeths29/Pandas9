# Problem 2 - Customer Placing the Largest Number of Orders (https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(['customer_number']).count().reset_index()
    df = df[df['order_number'] == df['order_number'].max()]
    return df[['customer_number']]