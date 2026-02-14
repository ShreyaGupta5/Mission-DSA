class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP = INT_MAX, profit = 0;
        for (int p : prices)
            minP = min(minP, p), profit = max(profit, p - minP);
        return profit;
    }
};
