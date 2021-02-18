import streamlit as st
# add all the necessary functions import

st.markdown("# ML Chartist")
st.markdown("**🚀 NASDAQ stocks prediction (attempt) 🚀**")

st.markdown("""ML Chartist gives you the opportunity to run backtest to measure
the effectiveness of investment strategies of our""")

st.markdown("""Our (amazing, super-effective and transcendental) model gives
    ***you*** the most likely stocks to have the best positive returns""")

st.markdown("## Create a portfolio based on the NASDAQ100 companies")


# Ask how many stocks user want to invest in
    # Restric to [1-10]
    # Warn that a too low number (1,2) is unlikely to give the best returns
    # Warn that a too high number (7+) is unlikely to give better returns than average
    # Show graph

n_stock = st.slider('Select the number of companies', 1, 10, 5)


def main():
    """Ask how many stocks user want to invest in
    Restricts to [1-10]
    Warn that a too low number (1,2) is unlikely to give the best returns
    Warn that a too high number (7+) is unlikely to give better returns than average
    Show graph"""
    print(f"User selected {n_stock} stocks for his portfolio")
    if n_stock <= 3:
        st.markdown("⚠️⚠️⚠️")
        st.markdown("The selected portfolio contains too few stocks")
        st.markdown("""Research have shown you should add more stock in your
            portfolio in order to get a better return""")

    if n_stock >= 7:
        st.markdown("⚠️⚠️⚠️")
        st.markdown("The selected portfolio contains too few stocks")
        st.markdown("""Research have shown you should add more stock in your
            portfolio in order to get a better return""")




# Evaluate probality of positive returns for previously hold stocks to
    # Ask stocks
    # Ask price and date user bought it



if __name__ == "__main__":
    main()
