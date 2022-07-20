import pandas as pd
import plotly.express as px
data = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/correlation/master/data/Ice-Cream%20vs%20Cold-Drink%20vs%20Temperature%20-%20Ice%20Cream%20Sale%20vs%20Temperature%20data.csv")
graph = px.scatter(data, x = "Temperature", y = "Ice-cream Sales( ₹ )")
graph.show()
print(data.corr())