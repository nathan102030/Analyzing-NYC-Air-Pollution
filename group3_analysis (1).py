from group3 import read_uhf, read_data

data_dicts = read_data("air_quality.csv")
uhf_dicts = read_uhf("uhf.csv")

#part a
pm_max = 0
pm_min = 99999

id_list = uhf_dicts[0]["10027"]

for id in id_list:
  measurement_list = data_dicts[0][id]
  for measurement in measurement_list:
    pm = float(measurement[3])
    if pm > pm_max: pm_max = pm
    if pm < pm_min: pm_min = pm

print(
  f"The highest polution measurement ever recorded in zip code 10027 was {pm_max} mcg/m^3 and the lowest was {pm_min} mcg/m^3."
)

#part b
date_list = []
pm_to_id = {}
pm_max = 0

for k in data_dicts[1]:
  if k[-2:] == "19": date_list.append(k)

for date in date_list:
  measurement_list = data_dicts[1][date]
  for measurement in measurement_list:
    pm = float(measurement[3])
    pm_to_id[pm] = measurement[0]
    if pm > pm_max: pm_max = pm

print(
  f"The UHF id that had the worst pollution in 2019 was {pm_to_id[pm_max]}.")

#part c
year_to_date = {2008: [], 2019: []}
total_pollution = {2008: 0, 2019: 0}
counter = {2008: 0, 2019: 0}

for k in data_dicts[1]:
  if k[-2:] == "08": year_to_date[2008].append(k)
  elif k[-2:] == "19": year_to_date[2019].append(k)

for year in year_to_date:
  for date in year_to_date[year]:
    measurement_list = data_dicts[1][date]
    for measurement in measurement_list:
      total_pollution[year] += float(measurement[3])
      counter[year] += 1

p1 = round(total_pollution[2008] / counter[2008], 2)
p2 = round(total_pollution[2019] / counter[2019], 2)

print(
  f"The average air polution in Manhattan was {p1} mcg/m^3 in 2008 and {p2} mcg/m^3 in 2019."
)

#part d

# Q1: Which UHF id had the least pollution in 2018

date_list = []
pm_to_id = {}
pm_min = 99999

for k in data_dicts[1]:
  if k[-2:] == "18": date_list.append(k)

for date in date_list:
  measurement_list = data_dicts[1][date]
  for measurement in measurement_list:
    pm = float(measurement[3])
    pm_to_id[pm] = measurement[0]
    if pm < pm_min: pm_min = pm

print(
  f"The UHF id that had the least pollution in 2018 was {pm_to_id[pm_min]}.")

# Q2: What was the average air polution in zip code 11214 at all time?

id_list = uhf_dicts[0]["11214"]

pm_sum = 0.0

for id in id_list:
  measurement_list = data_dicts[0][id]
  for measurement in measurement_list:
    pm_sum += float(measurement[3])

pm_avg = round(pm_sum / (len(measurement_list) * len(id_list)), 2)

print(
  f"The average pollution measurement in zip code 11214 at all times was {pm_avg} mcg/m^3."
)
