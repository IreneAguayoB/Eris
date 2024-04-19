import pandas as pd
# dash
import dash
from dash import Dash, html, dcc, dash_table #,callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
#plotly
import plotly.express as px

# import dfs
df_month = pd.read_csv('mart_milestones_condition_months.csv')
#df_day_week = pd.read_csv('mart_milestones_condition_day_of_the_week.csv')
df_total_city = pd.read_csv('mart_conditions_total_per_city.csv')
# my_palette
red='#E74C3C'
purple = '#9B59B6'
light_purple = '#D7BDE2'
blue='#3498DB '
light_blue ='#AED6F1 '
green= '#1ABC9C'
light_green ='#ABEBC6'
orange='#F39C12'
grey_text = '#D7DBDD'
 # spicific dfs for city
df_seoul = df_month[df_month['city']=='Seoul']
df_busan = df_month[df_month['city']=='Busan']
df_berlin = df_month[df_month['city']=='Berlin']

app =dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
# add server
server = app.server
##################### TABLES

# table Seoul definition
s_table = dash_table.DataTable(df_seoul.to_dict('records'),
                               [{'name':i, 'id':i} for i in df_seoul.columns],
                              style_data={'color': 'lightblue','backgroundColor': "#222222"},
                              style_header={
                                  'backgroundColor': light_blue,
                                  'color': 'black','fontWeight': 'bold'})


# table Busan definition
bu_table = dash_table.DataTable(df_busan.to_dict('records'),
                               [{'name':i, 'id':i} for i in df_seoul.columns],
                              style_data={'color': light_green,'backgroundColor': "#222222"},
                              style_header={
                                  'backgroundColor': light_green,
                                  'color': 'black','fontWeight': 'bold'})



# table Berlin definition
be_table = dash_table.DataTable(df_berlin.to_dict('records'),
                               [{'name':i, 'id':i} for i in df_seoul.columns],
                              style_data={'color': light_purple,'backgroundColor': "#222222"},
                              style_header={
                                  'backgroundColor': light_purple,
                                  'color': 'black','fontWeight': 'bold'})

# set app layout


################################## GRAPHS
# Average temperature per month
fig1 = px.bar(df_month, 
             x='month_of_year', 
             y='avg_temp',  
             color='city',
             barmode='group',
             height=300, 
              #title = "Average temperature per month",
             color_discrete_map = {'Berlin': purple, 'Seoul': blue, 'Busan': green})
fig1 = fig1.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white")
graph1 = dcc.Graph(figure=fig1)
#fig1.show()
#Average humidity
fig2 = px.bar(df_month, 
             x='month_of_year', 
             y='avg_humidity',  
             color='city',
             barmode='group',
             height=300, #title = "Average humidity",
             color_discrete_map = {'Berlin': purple, 'Seoul': blue, 'Busan': green})
fig2 = fig2.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white")
graph2 = dcc.Graph(figure=fig2)
# fig2.show()

# rainy days
fig3 = px.bar(df_month, 
             x='month_of_year', 
             y='rainy_days',  
             color='city',
             barmode='group',
             height=300, #title = "Rainy days",
             color_discrete_map = {'Berlin': purple, 'Seoul': blue, 'Busan': green})
fig3 = fig3.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white")
graph3 = dcc.Graph(figure=fig3)
#fig3.show()

fig4 = px.bar(df_total_city, x='city', y=['rainy_days', 'sunny_day'], color_discrete_map = {'rainy_days': '#5D6D7E ', 'sunny_day': orange},
             #title = "Total rainy and sunny days per city"
             )
fig4 = fig4.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white")
graph4 = dcc.Graph(figure=fig4)
#fig4.show()

fig5=px.bar(df_total_city, x='city', y='tropical_nights',color= 'city', color_discrete_map ={'Berlin': purple, 'Seoul': blue, 'Busan': green},
           #title = "Tropical nights"
           )
fig5 = fig5.update_layout(
        plot_bgcolor="#222222", paper_bgcolor="#222222", font_color="white")
graph5 = dcc.Graph(figure=fig5)
#fig5.show()

# just adding the multi = True parameter for our dropdown

graph = dcc.Graph()
#city =df_month['city'].unique().tolist() 


app.layout = html.Div([html.H1('Can I convince my husband to move to South Korea?', style={'textAlign': 'center', 'color': green}), 
                       html.Div([html.H4("Using the Weather API data we compare the climate conditions of Seoul, Busan and Berlin"),
                                html.P("According to the climate conditions which city would be better to live in?")], 
                                style={'marginLeft': 50, 'marginRight': 25}),


                       html.Div([html.Div([html.H1('Seoul', style={'textAlign': 'center', 'color': light_blue}),html.Div(s_table)]),
                                html.Div([html.H1('Busan', style={'textAlign': 'center', 'color': light_green}),html.Div(bu_table)]),
                                html.Div([html.H1('Berlin', style={'textAlign': 'center', 'color': light_purple}),html.Div(be_table)]),
                                 #dropdown, 
                                 html.Div([html.H2('Average temperature per month', style={'textAlign': 'center', 'color': grey_text}),html.Div(graph1)]),
                                 html.Div([html.H2('Average humidity', style={'textAlign': 'center', 'color': grey_text}),html.Div(graph2)]),
                                 html.Div([html.H2('Rainy days', style={'textAlign': 'center', 'color': grey_text}),html.Div(graph3)]),
                                 html.Div([html.H2('Total rainy and sunny days per city', style={'textAlign': 'center', 'color': grey_text}),html.Div(graph4)]),
                                 html.Div([html.H2('Tropical nights', style={'textAlign': 'center', 'color': grey_text}),html.Div(graph5)])
                                ])
                      ])
#@callback(
    #Output(graph1, "figure"), 
    #Input(dropdown, "value"))    

if __name__ == "__main__":
    app.run_server()




