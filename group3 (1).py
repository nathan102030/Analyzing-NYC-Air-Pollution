
import csv # optional, but useful


def read_data(filename):
  """
  should return two dictionaries (i.e. a tuple with two elements, 
  each of them a dictionary).

  1) A dictionary mapping each UHF geographic IDs to a lists of measurement tuples.
  2) A dictionary mapping each date (as a string) to a list of measurement tuples.
  """
  id_to_measurement = {}
  date_to_measurement = {}

  with open(filename, "r") as data:
    for line in data:
      line = tuple(line.strip().split(","))
      
      id = line[0]
      if not id in id_to_measurement: id_to_measurement[id] = [] 
      id_to_measurement[id].append(line)
        
      date = line[2] 
      if not date in date_to_measurement: date_to_measurement[date] = []
      date_to_measurement[date].append(line)

  return (id_to_measurement, date_to_measurement)


def measurement_to_string(measurement):
  """
  format a single measurement tuple as a string. For example: 
  "6/1/09 UHF 205 Sunset Park 11.45 mcg/m^3"
  """
  id = measurement[0]
  borough = measurement[1] 
  date = measurement[2]
  pm = measurement[3]
  
  return f"{date} UHF {id} {borough} {pm} mcg/m^3"


def read_uhf(filename):
  """
  should return two dictionaries: 
  1) A dictionary mapping each zip code to a list of UHF geographic IDs 
  2) A dictionary mapping each borough name to a list of UHF geographic IDs.
  """
  zip_to_id = {}
  borough_to_id = {}

  with open(filename, "r") as data:
    for line in data: 
      line = line.strip().split(",")
      for i in range(3,len(line)): 
        zip = line[i]
        if not zip in zip_to_id: zip_to_id[zip] = []
        zip_to_id[zip].append(line[2])

      borough = line[0]
      if not borough in borough_to_id: borough_to_id[borough] = []
      borough_to_id[borough].append(line[2])
        
  return (zip_to_id, borough_to_id) 


def main():
  search = True
  
  data_filename = "air_quality.csv"
  uhf_filename = "uhf.csv"

  data_dicts = read_data(data_filename)
  uhf_dicts = read_uhf(uhf_filename)

  #add code to quit  
  while search: 
    user_method = input("Would you like to search by zip code, UHF id, borough, or date? Type '.' to quit: ").lower()
    
    if user_method == ".": 
      search = False
      break
      
    if user_method != ".": user_input = input(f"Type a {user_method}: ")

    id_list = None

    if user_method == ".": 
      search = False
      break
    if user_method == "uhf id": 
      measurement_list = data_dicts[0][user_input]
      for measurement in measurement_list:
        measurement_to_string(measurement)
    elif user_method == "date": 
      measurement_list = data_dicts[1][user_input]
      for measurement in measurement_list:
        measurement_to_string(measurement)
      
    elif user_method == "zip code": id_list = uhf_dicts[0][user_input]
    elif user_method == "borough": id_list = uhf_dicts[1][user_input]

    if id_list: 
      for id in id_list:
        measurement_list = data_dicts[0][id]
        for measurement in measurement_list:
          measurement_to_string(measurement)

if __name__ == "__main__": 

  main()
