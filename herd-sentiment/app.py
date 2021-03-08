# Import Libraries
# ----------------------------------------------------------------------------

from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_address

# ------------------------------------------------------------------------------
# Create an engine for the database
# ------------------------------------------------------------------------------
engine = create_engine(db_address, echo=False)


# Reflect Database into ORM classes
# ------------------------------------------------------------------------------
Base = automap_base()
Base.prepare(engine, reflect=True)

# ------------------------------------------------------------------------------
# Flask Setup
# ------------------------------------------------------------------------------
app = Flask(__name__)


# Frontend Route and Homepage
# ------------------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# Backend Routes:
# Entertainment page
# ------------------------------------------------------------------------------
@app.route('/entertainment')
def entertainment():

    stocks = Base.classes.entertainment
    session = Session(engine)

    gc = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'GC.TO').order_by(stocks.Date).all()
    recp = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'RECP.TO').order_by(stocks.Date).all()
    cgx = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'CGX.TO').order_by(stocks.Date).all()

    entertainment_stocks = {"entertainment_stocks": [
        {
            'Ticker': 'GC.TO',
            'Date': [row[2] for row in gc],
            'Adj_Close': [row[1] for row in gc]
        },
        {
            'Ticker': 'RECP.TO',
            'Date': [row[2] for row in recp],
            'Adj_Close': [row[1] for row in recp]
        },
        {
            'Ticker': 'CGX.TO',
            'Date': [row[2] for row in cgx],
            'Adj_Close': [row[1] for row in cgx]
        }
    ]}
    session.close()
    return jsonify(entertainment_stocks)

# Telecommunication page
# ------------------------------------------------------------------------------
@app.route('/telecommunication')
def telecommunication():

    stocks = Base.classes.telecommunication
    session = Session(engine)

    rci = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'RCI-B.TO').order_by(stocks.Date).all()
    bce = session.query(stocks.Ticker, stocks.Adj_Close, stocks.Date).filter(
        stocks.Ticker == 'BCE.TO').order_by(stocks.Date).all()

    telecommunication_stocks = {"telecommunication_stocks": [
        {
            'Ticker': 'RCI-B.TO',
            'Date': [row[2] for row in rci],
            'Adj_Close': [row[1] for row in rci]
        },
        {
            'Ticker': 'BCE.TO',
            'Date': [row[2] for row in bce],
            'Adj_Close': [row[1] for row in bce]
        }
    ]}
    session.close()
    return jsonify(telecommunication_stocks)

# Dates page
# --------------------------------------------------------------------------------
@app.route('/dates')
def dates():

    stocks = Base.classes.dates_table
    session = Session(engine)

    news = session.query(stocks.Date, stocks.News).all()

    date_dict = {"Story": [{
        'Date': [row[0] for row in news],
        'News': [row[1] for row in news]
    }]}

    session.close()
    return jsonify(date_dict)


 

if __name__ == "__main__":
    app.run()