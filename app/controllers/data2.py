import matplotlib.pyplot as plt
import pandas as pd

# Create a data frame
data = pd.DataFrame({
    'Task Name': ['MARZO', 'MAYO', 'JULIO'],
    'Task Creation Date': ['30', '40', '50'],
    'Task Completion Date': ['10', '20', '30']
})

# Calculate the elapsed time for each task in hours
data['Elapsed Time'] = (pd.to_datetime(data['Task Completion Date'], format='%d') - 
                        pd.to_datetime(data['Task Creation Date'], format='%d')).dt.total_seconds() / 3600

# Bar chart
plt.bar(data['Task Name'], data['Elapsed Time'])
plt.xlabel('Task')
plt.ylabel('Elapsed Time (hours)')
plt.title('Task Elapsed Time')
plt.savefig('bar_chart.pdf')
plt.clf()  # Clear the figure to start fresh for the next plot

# Line chart
plt.plot(data['Task Name'], data['Elapsed Time'], marker='o')
plt.xlabel('Task')
plt.ylabel('Elapsed Time (hours)')
plt.title('Task Elapsed Time')
plt.savefig('line_chart.pdf')
plt.clf()

# Scatter plot
plt.scatter(data['Task Name'], data['Elapsed Time'])
plt.xlabel('Task')
plt.ylabel('Elapsed Time (hours)')
plt.title('Task Elapsed Time')
plt.savefig('scatter_plot.pdf')
