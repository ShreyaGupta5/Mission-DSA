class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = True
        
        while n >= stones:
            n -= stones
            stones -= 1
            alice_turn = not alice_turn
            
        # If it's currently Bob's turn (alice_turn is False) when stones run out, 
        # Bob cannot make a move and Alice wins.
        return not alice_turn
