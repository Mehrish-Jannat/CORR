import pandas as pd
import plotly.express as px
data = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/correlation/master/data/Size%20of%20TV%2C%09Average%20time%20spent%20watching%20TV%20in%20a%20week%20(hours).csv")
graph = px.scatter(data, x = "Size of TV", y = "	Average time spent watching TV in a week (hours)")
graph.show()
print(data.corr())