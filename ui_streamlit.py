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

n_stock = st.slider('Select the number of companies', 1, 10, 5)


def built_comp_list(predictions, n=1):
    cmp_dict = {}
    for dt in predictions.columns:
        dt_serie = predictions[dt].sort_values(ascending=False)
        dt_serie_non_zero = dt_serie[dt_serie != 0]
        comp_list = list(dt_serie_non_zero.head(n).index)
        cmp_dict[dt.strftime('%Y-%m-%d')] = comp_list
    return cmp_dict

def bckt_time_window(dt, bck_test_df, comp_list):
    comp_series = {}
    for comp in bck_test_df.columns:
        if comp in comp_list:
            comp_series[comp] = bck_test_df[comp][dt:].head(10).sort_index(ascending=False)
        else:
            comp_series[comp] = pd.Series(index=bck_test_df[dt:].head(10).index, data = np.nan)
    return pd.DataFrame(comp_series)



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
        # st.markdown("The selected portfolio contains too few stocks")
        # st.markdown("""Research have shown you should add more stock in your
        #     portfolio in order to get a better return""")
        # st.markdown("⚠️⚠️⚠️")


    # Improvement idea: run the integral of the portfolio return against the
    #   index one to increase robustness of stock number selection

    if n_stock >= 7:
        st.error("""⚠️⚠️⚠️
            The selected portfolio contains too many stocks.
            In order to avoid a unoptimal return (too close from the
            average return, i.e the NASDAQ100 one) please select a lower number
            of companies.
            ⚠️⚠️⚠️""")
        # st.markdown("⚠️⚠️⚠️")
        # st.markdown("The selected portfolio contains too many stocks")
        # st.markdown("""In order to avoid a unoptimal return (too close from the
        #     average return, i.e the NASDAQ100 one) please select a lower number
        #     of companies""")
        # st.markdown("⚠️⚠️⚠️")


    url = f'https://mlchartist-server.herokuapp.com/api/backtest?companies={n_stock}'
    st.warning('👩‍💻🎩👨‍💻 Mysterious backend stuff going on 👩‍💻🎩👨‍💻')

    # Trigger API request with the number of stocks
    response = requests.get(url).json()
    st.info('Getting JSON data')

    # Preprocessing DataFrame
    returns_df = pd.DataFrame(response)
    returns_df['date'] = pd.to_datetime(returns_df['date'])
        # Prepare Performance DataFrame
    diff = pd.DataFrame()
    diff['ret_NDX'] = returns_df['avg_return'] - returns_df['NDX']
    returns_df.rename(columns={'NDX': 'NASDAQ-100 Index', 'avg_return':'Portfolio Predicted Returns'})
    returns_df.set_index('date', inplace=True)
    returns_df = returns_df.fillna(value=1)
    viz_df = returns_df.cumprod()
    st.info('🔮🧞‍♀️🔮 Returns visualisation ready to be shown 🔮🧞‍♀️🔮')
    st.line_chart(viz_df)

    st.markdown("""## 🏦 Portfolio Performance Compared to the NASDAQ-100 average 🏦""")
    st.markdown("How much better than the index the portfolio predicted returns are ?")

    if diff.ret_NDX.sum() >= 0:
        st.write("The portfolio predicted returns are ",round(diff.ret_NDX.sum() * 100, 3), "%"," better")
    elif diff.ret_NDX.sum() <= 0:
        st.write("The portfolio predicted returns are ",round(diff.ret_NDX.sum() * 100, 3), "% worse")



if __name__ == "__main__":
    main()

