import mod
import readdata
import charts
import pandas as pd

def run ():
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_charts(countries,percentages)
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  
  countries = df['Country/Territory'].values 
  percentages = df['World Population Percentage'].values
  charts.generate_pie_charts(countries, percentages)

  data = readdata.readdata('data.csv')

  country= input('Type your country => ')
 
  result= mod.getpopulation_by_country(data, country)
 
  if len(result)>0:
    country=result[0]
    labels, values = mod.getpopu(country)
    charts.generate_bar_charts(country['Country/Territory'], labels, values)
  
if __name__ == '__main__':
  run()