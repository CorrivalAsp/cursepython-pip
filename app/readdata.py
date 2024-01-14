import csv
def readdata(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data= []
    
    for row in reader:
      iterable = zip(header, row)
      country_dic= { key: value for key, value in iterable}
      data.append(country_dic)
  return data

if __name__ == '__main__':
  data = readdata('data.csv')

  print(data[1])
      