from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    max_profit = 0
    lowest = float('inf')
    for price in prices:
        lowest = min(price, lowest)
        max_profit = max(max_profit, price - lowest)

    # [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
