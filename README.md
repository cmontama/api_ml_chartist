# Le Wagon Bootcamp Team Project

## Project Abstract
- **Project:** mlchartist (Web interface repository see [marcin-sobocinski/mlchartist](https://github.com/marcin-sobocinski/mlchartist) for main repository & [kerins18/mlchartist-server](https://github.com/kerins18/mlchartist-server) for the api)
- **Description:** Technical-based analysis of NASDAQ100 stocks to identify companies providing best financial returns in order to form an attractive stock portfolio
- **Data Source:**  stooq.com/db/h
- **Type of analysis:** Classification with Deep Learning (Neural Network)

## Process Description
- **Data Aquisition & Preparation** :
  - company stocks history CSV file download
  - financial technical indicators computation (chartist analysis)
  - financial returns computation
  - merging of selected stocks into a single Pandas Dataframe

- **Data preprocessing:** data formating to arrays of windows upon selected stride (see full_dataset_randomised_arrays function):
  - split stock to X and y set per company
  - outliers removal
  - data scaling
  - shuffle the companies X and y set to model X and y

- **LSTM Neural Network Model (Keras):**
  - *model tuning:* L1 and L2 Regularizers, batch normalization, dropout, 0.8 threshold for accuracy and precision, early stopping, reduce on plateau
  - *complexity:* 11 layers with more than 140 000 parameters
  - *performance\*(for non-specialist see below for accuracy and precision meaning):*
    - train set: 77% of accuracy & 93% of precision
    - validation set: 65% of accuracy & 90% of precision
    - **test set: 45% of accuracy & 60% of precision**

- **API :** Flask & Heroku

- **Web Interface:** Heroku & Streamlit

## Outcome
[Click here](http://ml-chartist.herokuapp.com/) to see the (minimalist) project output




## *Note*
- **Model Accuracy :**
  - The accuracy is the ratio of correct predictions
  - ex: for 45% accuracy, 45% of stocks returns were correctly predicted to be less than 5%, and the 55% others were incorrectly predicted to be lower than 5%
  - Accuracy ~ 1 - *rate of missed opportunities* (in our case not using good stock returns)

- **Model Precision :**
  - The precision measures the ratio of correct predictions of **a class**
  - ex: for 60% precision, 60% of stocks returns were correctly predicted to be more than 5% but the 40% others were incorrectly predicted to be higher than 5%
  - Precision ~ 1 - *rate of false positive* (in our case using bad stock returns)
