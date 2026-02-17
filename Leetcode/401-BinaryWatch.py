class Solution:
    def readBinaryWatch(self, turnedOn: int):
        result = []
       
        for hour in range(12):
            for minute in range(60):
                total_ones = bin(hour).count('1') + bin(minute).count('1')
                
                if total_ones == turnedOn:
                    time = f"{hour}:{minute:02d}"
                    result.append(time)
        
        return result
