import math
import plotly
import plotly.graph_objs as go

x = [x / 10 for x in range(100)]
y = [math.sin(c) for c in x]

print(f"x={x}")
print(f"y={y}")

fig = go.Scatter(x=x, y=y)
plotly.offline.plot({"data": [fig]})

x = ["Apple Pie", "Chocolate Pie", "Pecan Pie", "Chocolate Pecan Pie"]
y = [5, 9, 4, 14]

fig = go.Pie(labels=x, values=y)
# plotly.offline.plot({"data": [fig]})
graph_div = plotly.offline.plot({"data": [fig]}, auto_open=False, output_type="div")
