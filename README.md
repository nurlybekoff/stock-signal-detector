# Stock Signal Detector

A lightweight Python project for fetching stock prices, computing moving average crossovers, and visualizing signal events for a list of tickers.

## Overview

This repository downloads historical stock data using `yfinance`, computes short- and long-term moving averages, identifies crossover points, and renders a set of charts showing price action and trade signal points.

The current example analyzes these tickers:

- `AAPL`
- `MSFT`
- `GOOGL`
- `AMZN`
- `NVDA`
- `TSLA`

## What it does

- Downloads 1 year of historical stock price data for each ticker
- Computes 7-day and 30-day moving averages on the `Close` price
- Detects crossover events where the 7-day average crosses the 30-day average
- Plots the raw closing price, moving averages, and crossover markers
- Saves the result as `signals.png` and displays the chart window

## Repository structure

- `main.py` - entry point that loads tickers, fetches data, and generates chart panels
- `helper.py` - data model and plotting classes for stock data, moving averages, and crossover markers
- `requirements.txt` - pinned Python dependencies required to run the project

## Setup

### Prerequisites

- Python 3.11+ recommended
- `pip` package manager

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the main script to fetch data, generate plots, and save the output image:

```bash
python main.py
```

The script will:

- download data from Yahoo Finance
- compute moving averages
- plot six ticker charts in a 2x3 grid
- save the plot as `signals.png`
- display the plot using Matplotlib

## Customization

To analyze a different set of stocks, update the `tickers` list in `main.py`.

To change the lookback window, modify the `period` passed to `data.fetch()` in `main.py`.

To adjust moving average lengths, edit `helper.py`:

- `roll_7` for the short window
- `roll_30` for the long window

## Notes

- The sample implementation plots crossover points using the long moving average value.
- Internet access is required because data is downloaded from Yahoo Finance.
- If you want to add signal filtering or trade logic, extend `StockData` and the plotter classes.

## Troubleshooting

- If `yfinance` fails, verify network access and ticker symbols.
- If Matplotlib cannot display a window, run the script in an environment with GUI support or save the figure manually.