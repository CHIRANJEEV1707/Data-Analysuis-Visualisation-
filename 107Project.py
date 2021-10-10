import pandas as pd
import plotly.express as pdx
import csv
import plotly.graph_objects as go

df=pd.read_csv(r"C:\Users\Chiranjeev\Downloads\Data-visualization-master\data visualisation by graphs(data).csv")

s=df.loc[df["student_id"]=="TRL_zet"]

x1=s.groupby("level")["attempt"].mean()

fig=go.Figure(go.Scatter(x=x1,y=["level-1","level-2","level-3","level-4"],orientation='h'))

fig.show()

print(x1)