class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = sorted(
            [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        )
        
        stack = []  # store indices of robots moving right
        alive = [True] * len(positions)
        
        for pos, health, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:  # d == 'L'
                while stack and healths[i] > 0:
                    j = stack[-1]
                    
                    if healths[j] < healths[i]:
                        alive[j] = False
                        stack.pop()
                        healths[i] -= 1
                    elif healths[j] > healths[i]:
                        alive[i] = False
                        healths[j] -= 1
                        break
                    else:
                        alive[i] = False
                        alive[j] = False
                        stack.pop()
                        break
        
        # collect survivors in original order
        result = []
        for i in range(len(positions)):
            if alive[i]:
                result.append(healths[i])
        
        return result
