class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Strategy 1: Buy all required items individually
        buy_individual = need1 * cost1 + need2 * cost2
        
        # Strategy 2: Buy bundle items for the overlapping need, then buy the rest individually
        common_need = min(need1, need2)
        buy_mixed = (
            common_need * costBoth
            + (need1 - common_need) * cost1
            + (need2 - common_need) * cost2
        )
        
        # Strategy 3: Buy only bundle items to cover the larger requirement (since excess is allowed)
        buy_all_both = max(need1, need2) * costBoth
        
        return min(buy_individual, buy_mixed, buy_all_both)
