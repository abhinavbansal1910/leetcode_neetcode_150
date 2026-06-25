class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle= (hour %12) *30 + minutes *0.5
        mins_angle= minutes*6
        diff=abs(hour_angle-mins_angle)
        return min(diff,360-diff)