import pandas as pd
import plotly.express as px
data = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/correlation/master/data/cups%20of%20coffee%20vs%20hours%20of%20sleep.csv")
graph = px.scatter(data, x = "Coffee in ml", y = "sleep in hours")
graph.show()
print(data.corr())