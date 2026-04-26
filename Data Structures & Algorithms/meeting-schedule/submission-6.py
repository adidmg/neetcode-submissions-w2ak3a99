"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_intervals=sorted([(i.start,i.end) for i in intervals])
        i=0
        j=1
        while j<len(s_intervals):
            if s_intervals[j][0]<s_intervals[i][1]:
                return False
            if s_intervals[j][1]>=s_intervals[i][0]:
                i=j
                j+=1
        return True
        


