import pygal
from die import Die

die1 = Die()
die2 = Die(10)

results1 = []
results2 = []
for roll_num in range(1000):
    result1 = die1.roll()
    result2 = die2.roll()
    results1.append(result1)
    results2.append(result2)

frequencies1 = []
frequencies2 = []
for value in range(1,11):
    frequency = results1.count(value)
    frequencies1.append(frequency)
    frequency = results2.count(value)
    frequencies2.append(frequency)

line_chart = pygal.Bar()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str,range(1,11))
line_chart.add('D1', frequencies1)
line_chart.add('D2', frequencies2)
line_chart.x_title = 'Result'
line_chart.y_title = "Frequency"
line_chart.title = '%'
line_chart.render_to_file('dice.svg')