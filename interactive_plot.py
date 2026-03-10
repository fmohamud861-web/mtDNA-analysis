import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(
    df,
    x="sequence_length",
    y="gc_content",
    labels={"sequence_length":"Sequence Length (bp)","gc_content":"GC Content (%)"},
    title="GC Content vs Sequence Length of Human mtDNA",
    hover_data=["sequence_length","gc_content"]
)

fig.write_html("interactive_plot.html")
print("Interactive plot saved as interactive_plot.html")
