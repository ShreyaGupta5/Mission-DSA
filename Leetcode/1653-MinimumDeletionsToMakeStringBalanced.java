class Solution {
    public int minimumDeletions(String s) {
        int b_count = 0;
        int deletions = 0;

        for (char ch : s.toCharArray()){
            if(ch == 'b'){
                b_count++;
            }
            else{
                deletions = Math.min(deletions +1, b_count);
            }
        }

        return deletions;
    }
}
