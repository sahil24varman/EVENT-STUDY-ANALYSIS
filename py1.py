# -*- coding: utf-8 -*-
# GROUP-11
# SAHIL VARMAN 2019B1A31017H
# SAMYAK JAIN  2019B1A41485H
# Pratham Jain	2019B4A40898H
# Abhishek Bhansali	2019B1A41468H
# Nishant Sethi	2019B2A21464H
# Rudraksh Tiwari	2019B4A41021H
# Shankara Narayanan 2019A3PS1240H	
# Yarlagadda Prajay	2019B5A40794H
"""
The event we took is the RUSSIA-UKRAINE WAR which started on the 24th of Feb
2022, (Invasion)Some background;Russia invaded Ukraine on 24 February, but
Ukrainian forces retook large areas around Kyiv in early April after Russia
abandoned its push towards the capital. Areas in the west of the country,
including Lviv, have seen missile attacks but no attempt by Russian forces
to take and occupy ground.
The Effects of 2022 Russian Invasion of Ukraine has been explained below.
"""
# Created on Mon Jul  4 15:22:26 2022

# @author: Jain
# """
# NOTE: KINDLY UNCOMMENT AND THEN SECTION OF RUN CODE;
"""
Load the eventstudy module and its dependencies: numpy and matplotlib:
"""
import eventstudy as es 
from eventstudy import excelExporter
import numpy as np
import matplotlib.pyplot as plt
import datetime

"""
Set the parameters needed for your events: the returns and Fama-French factors (using es.Single.import_returns()and es.Single.import_FamaFrench()):
"""
# \\\\\\\\\\\\\\\\\\\\\MARKET MODEL CODE STARTS HERE\\\\\\\\\\\\\\\\\\\\\\\\\
    
es.Single.import_returns('RETURNS.csv')
es.Single.import_returns('MM.csv')

"""
DEFINE EVENT STUDY HERE:
Run the event study, here using the Market Model:
"""
tickers = ['AMZN', 'JPM', 'PFE', 'TSLA', 'WMT','BA','PEP','MRO','DPZ']
for ticker in tickers:

    event = es.Single.market_model( 
            security_ticker= ticker,
            market_ticker= 'SPY',
            event_date = np.datetime64('2022-02-24'),
            event_window = (-20,+20), 
            estimation_size = 200,
            buffer_size=0
    )
    
    event.plot(AR=True)
    plt.show()  
    event.results(True,decimals=3)
    event.results().to_csv('Result_MM.csv')
   
   
    
    

# \\\\\\\\\\\\\\\\\\\\\3 FACTOR MODEL CODE STARTS HERE\\\\\\\\\\\\\\\\\\\\\\\\\
    
# es.Single.import_returns('RETURNS.csv')
# es.Single.import_FamaFrench('3F.csv')

# """
# DEFINE EVENT STUDY HERE:
# Run the event study, here using the Fama-French 3-factor model:
# """
# tickers = ['AMZN', 'JPM', 'PFE', 'TSLA', 'WMT','BA','PEP','MRO','DPZ']
# for ticker in tickers:

#     event = es.Single.FamaFrench_3factor( 
#             security_ticker = ticker,
#             event_date = np.datetime64('2022-02-24'),
#             event_window = (-20,+20), 
#             estimation_size = 200,
#             buffer_size=0
#     )
    
#     event.plot(AR=True)
#     plt.show() 
#     event.results(True,decimals=3)
#     event.results().to_csv('Result_3F.csv')
   
    
    # use standard matplotlib function to display the plot
    
    
# \\\\\\\\\\\\\\\\\\\\\5 FACTOR MODEL CODE STARTS HERE\\\\\\\\\\\\\\\\\\\\\\\\\
    

# es.Single.import_returns('RETURNS.csv')
# es.Single.import_FamaFrench('5F.csv')

# """
# DEFINE EVENT STUDY HERE:
# Run the event study, here using the Fama-French 5-factor model:
# """
# tickers = ['AMZN', 'JPM', 'PFE', 'TSLA', 'WMT','BA','PEP','MRO','DPZ']
# for ticker in tickers:

#     event = es.Single.FamaFrench_5factor( 
#             security_ticker = ticker,
#             event_date = np.datetime64('2022-02-24'),
#             event_window = (-20,+20), 
#             estimation_size = 200,
#             buffer_size=0
#     )
    
#     event.plot(AR=True)
#     plt.show()
#     event.results(True,decimals=3)
#     event.results().to_csv('Result_5F.csv')    

# =============================================================================
# DESCRIPTION OF MODELS:
    
# MARKET MODEL:  
#  The market model says that the return on a security depends on the return
#  on the market portfolio and the extent of the security's responsiveness
#  as measured by beta. The return also depends on conditions that are unique 
#  to the firm. The market model can be graphed as a line fitted to a plot of 
#  asset returns against returns on the market portfolio. This relationship is 
#  sometimes called the single-index model.   
  
# Capital Asset Pricing Model
# The most popular factor model is the single factor — Capital Asset Pricing
#  Model or CAPM, which forms the basis of the Modern Portfolio Theory.
# The CAPM, describes security’s risk as a function of it’s market exposure
# or market Beta.
#         Market Beta
#         The Market Beta is a measure of the systematic risk of the security.
#         In statistics, beta is the slope of the line which is obtained by 
#         regressing the returns of stock return with that of the market return.

#         The Capital Asset Pricing Model is a financial model, which 
#         calculates expected returns as a function of the risk-free rate,
#         market risk, and market returns.  Central to this model is the 
#         idea that returns are solely dictated by systematic risk.That is, 
#         if all market participants hold similar beliefs about expected
#         returns nd the dispersion of returns, then only increases or
#         decreases in market risk will change portfolio returns.

 # 3- FACTOR MODEL:
# The Fama and French model has three factors: the size of firms, 
# # book-to-market values, and excess return on the market. 
# In other words, the three factors used are SMB (small minus big), 
# HML (high minus low), and the portfolio's return less the risk-free
# rate of return. SMB accounts for publicly traded companies with small
# market caps that generate higher returns, while HML accounts for value 
# stocks with high book-to-market ratios that generate higher returns in 
# comparison to the market.    
# 
# 4- FACTOR MODEL:
#The Monthly Momentum Factor(MOM) can be calculated by subtracting the equal
 # weighted average of the lowest performing firms from the equal weighed 
 # average of the highest performing firms, lagged one month .
 # A stock would be considered to show momentum if its prior 12-month average of 
 # returns is positive, or greater. Similar to the three factor model, momentum
 # factor is defined by self-financing portfolio of (long positive momentum)+
 # (short negative momentum). Momentum strategies continue to be popular in 
 # financial markets. Financial analysts often incorporate the 52-week price
 # high/low in their Buy/Sell recommendations.
  
# 5- FACTOR MODEL: 
# In 2014, Fama and French adapted their model to include five factors. 
# Along with the original three factors, the new model adds the concept that
# companies reporting higher future earnings have higher returns in the 
# stock market, a factor referred to as profitability. The fifth factor,
# referred to as "investment", relates the concept of internal investment 
# and returns, suggesting that companies directing profit towards major
# growth projects are likely to experience losses in the stock market.
# 
# =============================================================================





   
    

    
    
    
    
    
    
    
    
    