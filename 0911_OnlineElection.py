# 1st solution
# O(n + q * log(n)) time | O(n) space
# where n = number of votes and  q = number of queries
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in zip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)