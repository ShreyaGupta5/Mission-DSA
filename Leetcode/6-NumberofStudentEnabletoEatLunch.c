int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize) {
    
    int circular_pref = 0;
    int square_pref = 0;
    for (int i = 0; i < studentsSize; i++) {
        if (students[i] == 0) {
            circular_pref++;
        } else {
            square_pref++;
        }
    }

   
    for (int i = 0; i < sandwichesSize; i++) {
        int current_sandwich = sandwiches[i];

        if (current_sandwich == 0) {
            
            if (circular_pref > 0) {
                circular_pref--;
            } else {
                
                return square_pref; 
            }
        } 
        
        else { 
            
            if (square_pref > 0) {
                square_pref--;
            } else {
                return circular_pref; 
            }
        }
    }
    
    
    return 0;
}
