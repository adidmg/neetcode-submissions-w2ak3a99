class TimeMap:

    def __init__(self):
        self.time_map=defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp]=value
        

    def get(self, key: str, timestamp: int) -> str:
        if timestamp not in self.time_map[key]:
            other_ts=timestamp-1
            while other_ts>=1:
                if other_ts in self.time_map[key]:
                    return self.time_map[key][other_ts]
                other_ts-=1
            return ""
        return self.time_map[key][timestamp]
