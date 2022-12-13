from dash import Dash, Input, Output, State, html, dcc, dash_table, callback
import webbrowser

app = Dash(__name__, title='COST Pubmed Customizer')

app.layout = html.Div(id = 'div1'
                      ,children = [
                        html.H1("COST Homecage Pubmed Search Customizer")
                        , html.Br()
                        , dcc.Checklist(id="checkboxes",
                            options=[
                                {'label': 'Homecage', 'value': 'home'},
                                {'label': 'Automated', 'value': 'auto'},
                                {'label': 'Activity', 'value': 'activity'},
                                {'label': 'Behavior', 'value': 'behav'},
                                {'label': 'Phenotype', 'value': 'pheno'},
                            ],
                            value=['home'])
                        , html.Br()
                        , html.P("Custom terms", style={'display': 'inline-block'})
                        , dcc.Input(id="custom", type="text", value="", style={'marginRight':'10px', 'display': 'inline-block'})
                        , html.Br()
                        , html.P("Search string")
                        # , dcc.Input(id='searchstring', type="text", value="", style={'display': 'inline-block'})
                        , html.Div(id='searchstring', children="", style={'display': 'inline-block'})
                        , dcc.Clipboard(target_id="searchstring", style={'display': 'inline-block'})
                        , html.Br()
                        , html.Button('Open Pubmed', id='pubmed_btn', n_clicks=0)
                        , html.Div(id='btn_pressed', children="")
                        ]
                    )

@app.callback(Output('searchstring', 'children'),
              Input('checkboxes', 'value'),
              Input('custom', 'value')
              )
def render_searchstring(checkboxes, custom):

    print("Rendering search string")
    return generate_searchstring(checkboxes, custom)

@app.callback(Output('btn_pressed', 'children'),
              Input('pubmed_btn', 'n_clicks'),
              State('checkboxes', 'value'),
              State('custom', 'value'))
def open_pubmed(nclicks, checkboxes, custom):

    if nclicks > 0:
        webbrowser.open(generate_searchstring(checkboxes, custom))
        return "Pubmed search opened in different tab"

def generate_searchstring(checkboxes, custom):
    
    combiner = ' AND '
    substrings = {}

    if 'auto' in checkboxes:
        substrings["auto"] = 'automat*'

    if 'home' in checkboxes:
        substrings["homecage"] = '("home cage" OR "homecage" OR "home-cage")'

    if 'activity' in checkboxes:
        substrings["activity"] = '(activity OR monitoring)'

    if 'behav' in checkboxes:
        substrings["behavior"] = '("behavior" OR "behaviour")'

    if 'pheno' in checkboxes:
        substrings["pheno"] = 'phenotyping'

    pubmed_search_string = 'https://pubmed.ncbi.nlm.nih.gov/?term='
    for substring in substrings.values():
        pubmed_search_string = pubmed_search_string + substring + combiner
    pubmed_search_string = pubmed_search_string.strip("AND ")

    # need to try removing trailing ANDs, could consider mocing custom to end if easier

    if len(custom) > 0:
        pubmed_search_string = pubmed_search_string + combiner + custom

    return pubmed_search_string

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
