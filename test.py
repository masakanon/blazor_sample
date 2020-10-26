# import pyproj 
# import time

# start = time.time()

# wgs84 = 'EPSG:4326'
# tokyo = 'EPSG:4301'
# transformer = pyproj.Transformer.from_crs(wgs84, tokyo)

# # 35.6672664,139.7127083
# # lat = (1) * 1000
# # lon = (2) * 1000
# # l1, l2 = transformer.transform(xx=lat, yy=lon)
# # elapsed_time = time.time() - start
# # print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# # for i in range(1000):
# #     l1, l2 = transformer.transform(xx=35.6672664, yy=139.7127083)
# # elapsed_time = time.time() - start
# # print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# wgs84 = pyproj.Proj(init='EPSG:4326') # WGS84 緯度経度
# tokyo = pyproj.Proj(init='EPSG:4301') # 平面直角座標6系
 
# lat, lng = 34.705185, 135.498468 # 梅田駅
 
# # WGS84緯度経度から、平面直角座標6系のXY座標に変換
# for i in range(1000):
#     x, y = pyproj.transform(wgs84, tokyo, lng, lat)
# elapsed_time = time.time() - start
# print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

from pyproj import Geod


lon0, lat0 = [(139.7127083,35.6672664),(139.7127083,35.6672664)]
lon1, lat1 = [(139.7099034,35.6652511),(139.7099034,35.6652511)]
n_extra_points = 100

geoid = Geod(ellps="WGS84")
extra_points = geoid.npts(lon0, lat0, lon1, lat1, n_extra_points)

data2 = map(lambda x: x * 2, data1)
