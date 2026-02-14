class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        
        // Create a 2D array (max 100 rows as per constraints)
        double[][] tower = new double[101][101];
        
        // Pour all champagne into the top glass
        tower[0][0] = poured;
        
        // Process row by row
        for (int row = 0; row <= query_row; row++) {
            for (int glass = 0; glass <= row; glass++) {
                
                // If overflow happens
                if (tower[row][glass] > 1) {
                    
                    double extra = (tower[row][glass] - 1) / 2.0;
                    
                    // Distribute extra to next row
                    tower[row + 1][glass] += extra;
                    tower[row + 1][glass + 1] += extra;
                    
                    // Current glass holds only 1
                    tower[row][glass] = 1;
                }
            }
        }
        
        // Return the answer (max 1)
        return tower[query_row][query_glass];
    }
}
