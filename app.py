# Library Setup
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Import function from db_service.py
from services.db_service import get_rush_hours_data

# Initialize Dash Application
app = Dash(__name__)
server = app.server # Required for deployment

# Fetching a data via db_service
df = get_rush_hours_data()

# Create Plotly Visualization
"""
TODO: Create a chart that show volume of each channel in each hour
"""
fig = px.bar(
    df,
    x="hour_of_day",
    y="total_order",
    color="channel",
    barmode="group",
    title="Total Orders by Clock Hour and Sales Channel (21 Sep – 1 Nov 2026)",
    labels={
        "hour_of_day": "Clock Hour of Day",
        "total_order": "Total Orders (All Recorded Days)",
        "channel": "Sales Channel"
    }
)


# App Layout
app.layout = html.Div(
    style={
        "maxWidth": "1100px",
        "margin": "0 auto",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif",
        "textAlign": "center",
    },
    children=[
        html.H1(
            "Bubble Tea Store Analytics",
            style={"marginBottom": "8px"},
        ),
        html.P(
            "Rush-hour analysis: total orders per clock hour by sales channel "
            "(Walk-in vs Foodpanda), summed across all recorded days "
            "from 21 Sep to 1 Nov 2026.",
            style={"color": "#555", "marginBottom": "30px"},
        ),
        dcc.Graph(
            id="rush-hour-chart",
            figure=fig,
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug = True)