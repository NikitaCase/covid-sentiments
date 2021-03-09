# Import Libraries
# ----------------------------------------------------------------------------

from flask import Flask, render_template, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
#from config import db_address

# ------------------------------------------------------------------------------
# Create an engine for the database
# ------------------------------------------------------------------------------
#engine = create_engine(db_address, echo=False)
engine = create_engine('sqlite:///trial.sqlite')


# Reflect Database into ORM classes
# ------------------------------------------------------------------------------
Base = automap_base()
Base.prepare(engine, reflect=True)

print(Base.classes.keys())

# # ------------------------------------------------------------------------------
# # Flask Setup
# # ------------------------------------------------------------------------------
# app = Flask(__name__)


# # Frontend Route and Homepage
# # ------------------------------------------------------------------------------
# @app.route("/")
# def home():
#     return render_template("index.html")


# # Backend Routes:
# # Timeline
# # ------------------------------------------------------------------------------

# # for some reason doesnt work in flask but works in jupyter 
# @app.route('/timeline')
# def timeline():

#     airlines = Base.classes.airlines
#     session = Session(engine)
    
#     lines = session.query(airlines.id_str, airlines.date, airlines.Sentiment, airlines.Polarity, airlines.retweet_count).all()

#     id_str = [col[0] for col in lines]
#     date = [col[1] for col in lines]
#     sentiment = [col[2] for col in lines]
#     polarity = [col[3] for col in lines]
#     retweet_count = [col[4] for col in lines]
#     #favourite_count = [col[5] for col in lines]

#     lined = {'timeline':[{
#         'id_str': id_str, 
#         'date': date, 
#         'sentiment': sentiment,
#         'polarity': polarity,
#         'retweet_count': retweet_count  
#     }]}

#     session.close()
#     return jsonify(lined)


# # Timeline
# # ------------------------------------------------------------------------------
# @app.route('/map')
# def map():

#     airlines = Base.classes.airlines
#     session = Session(engine)
    
#     lines = session.query(airlines.id_str, airlines.latitude, airlines.longitude, airlines.Sentiment).all()

#     loc =[]
#     for col in lines:
#         lo = {
#             'id_str': [col[0] for col in lines], 
#             'latitude': [col[1] for col in lines], 
#             'longitude': [col[2] for col in lines],
#             'sentiment': [col[3] for col in lines] 
#             }
#         loc.append(lo)

#     session.close()
#     return jsonify(loc)
 

    
# # Dates page
# # --------------------------------------------------------------------------------
# # @app.route('/dates')
# # def dates():

# #     stocks = Base.classes.dates_table
# #     session = Session(engine)

# #     news = session.query(stocks.Date, stocks.News).all()

# #     date_dict = {"Story": [{
# #         'Date': [row[0] for row in news],
# #         'News': [row[1] for row in news]
# #     }]}

# #     session.close()
# #     return jsonify(date_dict)


 

# if __name__ == "__main__":
#     app.run()