class UndergroundSystem:

    def __init__(self):
        self.station_avg = {}
        self.check_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
        travel_time = t - start_time
        key = f"{start_station},{stationName}"
        if key not in self.station_avg:
           self.station_avg[key] = (0, 0) 
        self.station_avg[key][0] += travel_time
        self.station_avg[key][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f"{startStation},{endStation}"
        return self.station_avg[key][0] / self.station_avg[key][1] 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)