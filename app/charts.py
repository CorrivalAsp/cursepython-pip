import matplotlib.pyplot as plt

def generate_bar_charts (labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

def generate_pie_charts (labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
if __name__ in '__main__':
  labels = ['Colombia', 'Mexico']
  values = [300, 200]
 # generate_bar_charts(labels, values)
  generate_pie_charts(labels, values)