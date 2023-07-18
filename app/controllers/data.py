import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.append('/path/to/matplotlib')
import sys
sys.path.append('/path/to/pandas')


# Create a data frame
data = pd.DataFrame({
    'Task Name': ['MARZO', 'MAYO', 'JULIO'],
    'Task Creation Date': ['30', '40', '50'],
    'Task Completion Date': ['10', '20', '30']
})

# Plot a graph of the data
plt.bar(data['Task Name'], data['Task Completion Date'], data= ['Task Creation Date'])
plt.show()

# Save the graph to a PDF file
plt.savefig('graph.pdf')