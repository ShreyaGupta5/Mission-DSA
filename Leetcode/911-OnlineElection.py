import bisect
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        
        count = defaultdict(int)
        leader = -1
        
        for p in persons:
            count[p] += 1
            if leader == -1 or count[p] >= count[leader]:
                leader = p
            self.leaders.append(leader)

    def q(self, t):
        i = bisect.bisect_right(self.times, t) - 1
        return self.leaders[i]
