import math
import datetime as dt

import numpy as np
import yfinance as yf

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start, end)
    df2 = yf.download(ticker2, start, end)
    return df1, df2

def plot_data(data, indicators, sync_axis=None):
    df = data
    gain = df.Close > df.Open
    loss = df.Open > df.Close
    width = 12 * 60 * 60 * 1000

    p = figure(x_axis_type="datetime", width=1000)
    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(df.index[gain], width, df.Open[gain], df.Close[gain], fill_color="green")

    return p

def on_button_click(ticker1, ticker2, start, end, indicators):
    df1, df2 = load_data(ticker1, ticker2, start, end)
    p1 = plot_data(df1, indicators)
    p2 = plot_data(df2, indicators, sync_axis=p1.x_range)
    curdoc().clear()
    curdoc().add_root(layout)
    curdoc().add_root(row(p1,p2))

stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")
data_picker_from = DatePicker(title="Start Date", value="2020-01-01", min_date="2000-01-01",
                               max_date=dt.datetime.now().strftime("%Y-%m-%d"))
data_picker_to = DatePicker(title="Start Date", value="2020-02-01", min_date="2000-01-01",
                               max_date=dt.datetime.now().strftime("%Y-%m-%d"))
indicator_choice = MultiChoice(options=["100 Day SMA", "30 Day SMA", "Linear Regression Line"])
load_button = Button(label="Load Data", button_type="success")
def f():
    on_button_click(stock1_text.value, stock2_text.value, data_picker_from.value, data_picker_to.value, indicator_choice.value)

load_button.on_click(f)
#lambda: on_button_click(stock1_text.value, stock2_text.value, data_picker_from.value, data_picker_to.value, indicator_choice.value)
layout = column(stock1_text, stock2_text, data_picker_from, data_picker_to, indicator_choice, load_button)


curdoc().clear()
curdoc().add_root(layout)
