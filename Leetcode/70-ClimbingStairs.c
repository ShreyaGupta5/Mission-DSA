int climbStairs(int n) {
    if (n <= 2) {
        return n; 
    }

    int oneBack = 2; 
    int twoBack = 1; 
    int currentWays;

    for (int i = 3; i <= n; i++) {
        currentWays = oneBack + twoBack; 
        twoBack = oneBack;               
        oneBack = currentWays;           
    }

    return oneBack; 
}
