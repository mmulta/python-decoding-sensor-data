from house_info import HouseInfo
from datetime import date

class TemperatureData(HouseInfo):
    def _convert_data(self,data):
        recs=[]
        for rec in data:
            recs.append(int(rec))
        return recs

    def get_data_by_area(self,rec_area=0):
        recs=get_data_by_area("temperature",rec_area)
        return _convert_data(recs)
    def get_data_by_date(self,rec_data=date.today()):
        recs=get_data_by_date("temperature",rec_date)
        return _convert_data(recs)
