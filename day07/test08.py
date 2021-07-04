loc = ['서울','부산','광주','대구','대전']
data = [28.8, 33.7, 29.4, 35.2, 26.3]

loc_data = dict(zip(loc,data))
print(loc_data)

sort_data = sorted(loc_data.items(), key = lambda x : x[1], reverse=True)
print(sort_data)
