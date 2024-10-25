import dash
import boto3
import pandas as pd
import plotly.express as px

from dash import dcc, html
from dash.dependencies import Input, Output

# Define Athena connection.
client = boto3.client('athena')
df = client.start_query_execution(
    QueryString="SELECT * FROM streaming_layer.streaming_data",
    QueryExecutionContext={'Database': 'driven_data'},
    ResultConfiguration={'OutputLocation': 's3://drivendata-results/'}
)

# Define allowed columns for selection in the dropdown.
allowed_columns = ["accessed_at","session_duration","download_speed","upload_speed","consumed_traffic"]

# Initialize Dash app.
app = dash.Dash(__name__)

# Layout of the dashboard.
app.layout = html.Div([
    html.H1("DrivenData Dashboard"),

    # Dropdown to select column to view on X axis.
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in allowed_columns],
        value='upload_speed',
        clearable=False,
        className='dropdown'
    ),

    # Graphs container.
    html.Div(className='graph-container', children=[
        # Graph to display consumed traffic vs selected column.
        dcc.Graph(id='scatter-plot', className='graph'),
        # Graph to display person names vs selected column.
        dcc.Graph(id='name-parameter-plot', className='graph'),
        # Graph to display selected column vs index.
        dcc.Graph(id='line-plot', className='graph'),
        # Graph to display distribution of selected column.
        dcc.Graph(id='box-plot', className='graph'),
        # Graph to display histomgram of selected column.
        dcc.Graph(id='histogram', className='graph'),
        # Graph to display distribution of age.
        dcc.Graph(id='pie-chart', className='graph')
    ])
])


# Callback to update scatter plot.
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_scatter_graph(selected_column):
    # Sort the data by 'consumed_traffic' to get the top 10 highest values.
    df_sorted = df.sort_values(by='consumed_traffic', ascending=False).head(10)
    # Create scatter plot for 'consumed_traffic' vs selected_column (limited to top 10 values).
    fig = {
        'data': [
            {
                'x': df_sorted[selected_column],
                'y': df_sorted['consumed_traffic'],
                'type': 'scatter',
                'mode': 'markers',
                'marker': {'size': 12}
            }
        ],
        'layout': {
            'title': f'Consumed traffic vs. {" ".join(selected_column.split("_")).capitalize()} (Top 10)',
            'xaxis': {'title': " ".join(selected_column.split("_")).capitalize()},
            'yaxis': {'title': 'Consumed traffic'}
        }
    }
    return fig


# Callback to update person names vs selected parameter plot.
@app.callback(
    Output('name-parameter-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_names_graph(selected_parameter):
    # Sort the data by the selected parameter to get the top 10 highest values.
    df_sorted = df.sort_values(by=selected_parameter, ascending=False).head(10)
    # Create a bar plot for person names vs selected parameter.
    fig = {
        'data': [
            {
                'x': df_sorted['person_name'],
                'y': df_sorted[selected_parameter],
                'type': 'bar'
            }
        ],
        'layout': {
            'title': f'Top 10 People by {" ".join(selected_parameter.split("_")).capitalize()}',
            'xaxis': {'title': 'Person name'},
            'yaxis': {'title': " ".join(selected_parameter.split("_")).capitalize()}
        }
    }
    return fig


# Callback to update line plot
@app.callback(
    Output('line-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_line_graph(selected_parameter):
    fig = px.line(df, x=df.index, y=selected_parameter, title=f'{" ".join(selected_parameter.split("_")).capitalize()} over Index')
    fig.update_layout(yaxis_title=" ".join(selected_parameter.split("_")).capitalize())
    return fig


# Callback to update box plot.
@app.callback(
    Output('box-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_box_graph(selected_parameter):
    fig = px.box(df, y=selected_parameter, title=f'Distribution of {" ".join(selected_parameter.split("_")).capitalize()}')
    fig.update_layout(yaxis_title=" ".join(selected_parameter.split("_")).capitalize())
    return fig


# Callback to update histogram.
@app.callback(
    Output('histogram', 'figure'),
    Input('column-dropdown', 'value')
)
def update_histogram(selected_parameter):
    fig = px.histogram(df, x=selected_parameter, title=f'Histogram of {" ".join(selected_parameter.split("_")).capitalize()}', nbins=30)
    fig.update_layout(xaxis_title=" ".join(selected_parameter.split("_")).capitalize(), yaxis_title='Count')
    return fig


# Callback to update pie chart.
@app.callback(
    Output('pie-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_pie_chart(selected_parameter):
   # Convert 'birth_date' to datetime and extract the year.
    df['birth_year'] = pd.to_datetime(df['birth_date'], errors='coerce').dt.year
    # Count occurrences of each year and get the top 10 most frequent years with their percentages.
    year_percentages = (
        df['birth_year']
        .value_counts()
        .nlargest(10)
        .div(df['birth_year'].notna().sum())
        * 100
    )
    fig = px.pie(names=year_percentages.index, values=year_percentages.values, title='Distribution of Age')
    return fig


# Run the Dash app.
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
