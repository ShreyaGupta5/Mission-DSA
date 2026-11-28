import collections
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # 1. Count occurrences of each factor (1 <= factor <= len(items))
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
            
        # 2. Use a Sieve approach to count how many items have a factor divisible by f
        multiples_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] == 0:
                continue
            for multiple in range(f, max_f + 1, f):
                multiples_count[f] += freq[multiple]
                
        # 3. Group valid "buy-one-get-one-free" pairs by item price
        min_price = min(p for _, p in items)
        bogo_groups = collections.defaultdict(int)
        
        for f, price in items:
            # Only worth buying for freebies if price < 2 * min_price
            if price < 2 * min_price:
                # Subtract 1 because an item cannot give a free copy of itself (i != j)
                bogo_groups[price] += multiples_count[f] - 1
                
        # 4. Greedily buy the cheapest 2-for-1 deals first
        total_items = 0
        for price in sorted(bogo_groups):
            can_buy = min(bogo_groups[price], budget // price)
            total_items += 2 * can_buy
            budget -= can_buy * price
            if budget == 0:
                break
                
        # 5. Spend any leftover budget on the absolute cheapest item
        total_items += budget // min_price
        return total_items
