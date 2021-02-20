import streamlit as st

import requests

import numpy as np
import pandas as pd

# add all the necessary functions import (in a dedicated launch.py file?)

st.markdown("# ML Chartist")
st.markdown("**🚀 NASDAQ stocks prediction 🚀**")

st.markdown("""ML Chartist gives you the opportunity to run backtest to measure
the effectiveness of investment strategies of our""")

st.markdown("""Our (amazing, super-effective and transcendental) model gives
    ***you*** the most likely stocks to have the best positive returns""")

st.markdown("## Create a portfolio based on the NASDAQ-100 companies")

n_stock = st.slider('Select the number of companies', 1, 15, 5)



def main():
    """
    Function ran by streamlit (as you can see below in the file)

    -Ask how many stocks user want to invest in
    -Restricts to [1-10]
    -Warn that a too low number (1,2) is unlikely to give the best returns
    -Warn that a too high number (7+) is unlikely to give better returns than average
    -Show graph

    """

    print(f"User selected {n_stock} stocks for his portfolio")
    if n_stock <= 3:
        st.error("""⚠️⚠️⚠️
            The selected portfolio contains too few stocks.
            Research have shown you should add more stock in your
            portfolio in order to get a better return.
            ⚠️⚠️⚠️""")

    # Improvement idea: run the integral of the portfolio return against the
    #   index one to increase robustness of stock number selection

    if n_stock >= 7:
        st.error("""⚠️⚠️⚠️
            The selected portfolio contains too many stocks.
            In order to avoid a unoptimal return (too close from the
            average return, i.e the NASDAQ-100 one) please select a lower number
            of companies.
            ⚠️⚠️⚠️""")


    if n_stock <=10:
        url = f'https://mlchartist-server.herokuapp.com/api/backtest?companies={n_stock}'

    elif n_stock >10:
        url = f'https://mlchartist-server.herokuapp.com/api/live-backtest?companies={n_stock}'


    # Trigger API request with the number of stocks
    st.warning('👩‍💻🎩👨‍💻 Mysterious backend stuff going on 👩‍💻🎩👨‍💻')

    response = requests.get(url).json()

    # Preprocessing DataFrame
    returns_df = pd.DataFrame(response)
    returns_df['date'] = pd.to_datetime(returns_df['date'])
        # Prepare Performance DataFrame
    diff = pd.DataFrame()
    diff['ret_NDX'] = returns_df['avg_return'] - returns_df['NDX']
    returns_df.rename(columns={'NDX': 'NASDAQ-100 Index', 'avg_return':'Portfolio Predicted Returns'}, inplace=True)
    returns_df.set_index('date', inplace=True)
    returns_df = returns_df.fillna(value=1)
    viz_df = returns_df.cumprod()
    st.info('🔮🧞‍♀️🔮 Returns visualisation ready to be shown 🔮🧞‍♀️🔮')
    st.line_chart(viz_df)

    #st.markdown("""## 🏦 Portfolio Performance Compared to the NASDAQ-100 average 🏦""")
    #st.markdown("How much better than the index the portfolio predicted returns are ?")

    if diff.ret_NDX.sum() >= 0:
        st.write("The portfolio predicted returns are ",round(diff.ret_NDX.sum() * 100, 3), "%"," better than index average")
    elif diff.ret_NDX.sum() <= 0:
        st.write("The portfolio predicted returns are ",round(diff.ret_NDX.sum() * 100, 3), "% worse than index average")



if __name__ == "__main__":
    main()

