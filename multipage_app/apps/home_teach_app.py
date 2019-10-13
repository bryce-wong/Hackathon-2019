# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app
import base64

# image_directory = '/Users/Dell/Documents/Hackathon 2019/Hackathon-2019/Hackathon-2019/multipage_app/apps/images'
logo_big = 'static/Blackbox logo big.png'
encoded_image = base64.b64encode(open(logo_big, 'rb').read())
logo_big_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 50,
                'padding-right' : 0
            })

logo_small = 'static/Blackbox logo big.png'
encoded_image = base64.b64encode(open(logo_small, 'rb').read())
logo_small_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '80%',
                'margin': 10
            })

background_design = 'static/background.jpg'
encoded_image = base64.b64encode(open(background_design, 'rb').read())
background_design_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding' : 40,
                'border-radius': '100px'
            })

background_stars = 'static/background2.png'
encoded_image = base64.b64encode(open(background_stars, 'rb').read())
background_stars_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding': 40,
                'border-radius': '100px',
                'opacity': '70%'
            })

button1 = 'static/background.jpg'
encoded_image = base64.b64encode(open(button1, 'rb').read())
button1_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding' : 40,
                'border-radius': '100px'
            })

button2 = 'static/background2.png'
encoded_image = base64.b64encode(open(button2, 'rb').read())
button2_thumb = html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={
                'height' : '35%',
                'width' : '35%',
                'float' : 'center',
                'position' : 'relative',
                'padding-top' : 0,
                'padding-right' : 0,
                'padding': 40,
                'border-radius': '100px',
                'opacity': '70%'
            })
#############
# Layout

layout = html.Div(
    id='main-page-content',children= [
    html.Div(
        children=[
            #nav bar
            html.Nav(
                #inside div
                html.Div(
                    children=[
                        html.A(logo_small_thumb,href='/'),
                        #ul list components
                        html.Ul(
                            children=[
                               html.Li(html.A('Home', href='/')),
                               html.Li(html.A('Tool Lookup', href='/apps/tool')),
                               html.Li(html.A('Tutorial Videos', href='/apps/vid')),
                            ],
                            id='nav-mobile',
                            className='right hide-off-med-and-down'
                        ),
                    ],
                    className='nav-wrapper'
                ),style={'background-color':'#66ccff'}),
        ],
        className='navbar-fixed'
    ),
    html.Div(
        html.Center(
            children=[
                logo_big_thumb,
            # html.Img(
            # src='https://i.imgur.com/Qp1SMwQ.png',
            # style={
            #     'height' : '35%',
            #     'width' : '35%',
            #     'float' : 'center',
            #     'position' : 'relative',
            #     'padding-top' : 50,
            #     'padding-right' : 0
            # }),
                html.Center(
        html.H1('''Breaking Open the Black Box
    '''), style={'padding-bottom': 100})
             ], style={'padding-bottom': 0})
    ),
    html.Div(
        children=[
            html.Center(
                html.H3('What is this website?'),style={'padding-top': 50,'text-shadow': '0.5px 0.5px gray'}),
            html.Center(
            html.H5('The healthcare field needs more tech-savvy professionals, like you, to understand and smartly leverage Artificial Intelligence (AI) technology. At the 2019 Mount Sinai Health Hackathon we set about to make AI more accesible to those working in a healthcare setting. This website provides access to explanations of AI tools used in the health care setting today as well as the concepts behind these tools'),style={'padding': 50,'text-shadow': '0.5px 0.5px gray'},className='slim-paragraph'
        )],style={
        'backgroundColor':'#80ffff',
        'border': 'grey',
        'padding': '50px 10px 10px',
        'box-shadow': '5px 5px 5px #888888'}
    ),
    html.Div(
        children=[
            html.Center(
            html.H3('How should you use this website?'),style={'padding-top': 50,'color':'#ffffff','text-shadow': '0.5px 0.5px black'}),
            html.Center(
            html.H5('Start with what interests or drives you: Is it existing AI tools and how they aid in medical decision-making? Or do you want to understand the statistical concepts underpinning AI? Go at your own pace - spend 5 seconds getting the quick info, or spend 5 hours diving deeper and deeper. Learn how you want, for as long as you want.'),
            style={'padding': 50,'color':'#ffffff','text-shadow': '0.5px 0.5px black'},className='slim-paragraph'
        )],style={
        'backgroundColor':'#71da71',
        'border': 'grey',
        'padding': '50px 10px 50px',
        'box-shadow': '5px 5px 5px #888888'}
    ),
    html.Center(
        children=[
        html.H3('Choose where you want to start:'),
        html.A(background_design_thumb, href='/apps/tool'),
        html.A(background_stars_thumb, href='/apps/vid')], style={'padding': 100})
    ]
)

# if __name__ == '__main__':
#     app.run_server(debug=True)