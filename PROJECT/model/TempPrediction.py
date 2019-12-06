import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt
#import seaborn as sns # for plot visualization
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# There is column named **datetime_utc** in this dataset, we are going to read that as an index.

weather_df = pd.read_csv('C:/Users/Reddy/Desktop/PROJECT/model/testset1.csv', parse_dates=['datetime_utc'], index_col='datetime_utc')

# <a>Feature Engineering</a>

# Here we are going to consider only few of the columns which seems important from some basic EDA and time series prediction's point of view. At the same time renaming with some better ones.

weather_df = weather_df.loc[:,[' _conds', ' _hum', ' _tempm']]
weather_df = weather_df.rename(index=str, columns={' _conds': 'condition', ' _hum': 'humidity', ' _pressurem': 'pressure', ' _tempm': 'temprature'})

weather_df.index = pd.to_datetime(weather_df.index)

# Not many values are missing, but it will still be great to fill the missing ones instead of removing entire row.
# will fill with previous valid value

weather_df.ffill(inplace=True)

# It is showing maximum temprature as 90 and max humidity as 243 which is non-realistic, so is an outlier. We need to treat these outliers.

weather_df = weather_df[weather_df.temprature < 50]
weather_df = weather_df[weather_df.humidity <= 100]

# ## <a>Exploratory Data Analysis & Visualizations</a>

# model traning
train_df = weather_df['1996':'2015'].resample('D').mean().fillna(method='pad')
train_df.drop(columns='humidity', axis=1, inplace=True)
test_df = weather_df['2016':'2017'].resample('D').mean().fillna(method='pad')
test_df.drop(columns='humidity', axis=1, inplace=True)


# ### Check Stationarity
# * Constant mean
# * Constant variance
# * An auto co-variance that does not depend on time


# Augmented Dickey–Fuller test
def perform_dickey_fuller_test(ts):
    result = adfuller(ts, autolag='AIC')
    print('Test statistic: ' , result[0])
    print('Critical Values:' ,result[4])


# In Dickey-Fuller test, we need only test_statics and critical_value to know if it is stationary or not

perform_dickey_fuller_test(train_df.temprature)


# We have constant Mean and Variance, and our Test statistic is less than Critical Values, so we already have stationary Time series. So our 'd' value will become 0 in ARIMA Model.
#
# Consider a case if it was non-stationary, in that case we would use below techniques to make it stationary
#
# Make Stationary
# For non-stationary to stationary conversion, we can use any of the below technique :
#
# - Decomposing
# - Differencing
#
# Here, we are preferring Differencing because it is very straight forward. We would use below co-relation plots to identify the order of differencing


# ### Timeseries Analysis (ARIMA Model)

# For prediction we are going to use one of the most popular model for time series, **Autoregressive Integrated Moving Average (ARIMA)** which is a standard statistical model for time series forecast and analysis.
# An ARIMA model can be understood by outlining each of its components as follows:
# * **Autoregression (AR) -** refers to a model that shows a changing variable that regresses on its own lagged, or prior, values.<br/>
# The notation **AR(p)** indicates an autoregressive model of order p.
#
#     *Example* — If p is 3 the predictor for X(t) will be
#         X(t) = µ + X(t-1) + X(t-2) + X(t-3) + εt
#
#     Where ε is error term.
# * **Integrated (I) -** represents the differencing of raw observations to allow for the time series to become stationary, i.e., data values are replaced by the difference between the data values and the previous values.
# * **Moving average (MA) -** incorporates the dependency between an observation and a residual error from a moving average model applied to lagged observations.
#
#     The notation **MA(q)** refers to the moving average model of order q:<br/>
#  ![image.png](attachment:image.png)
#
#     *Example* — If q is 3 the predictor for X(t) will be
#         X(t) = µ + εt + θ1.ε(t-1) + θ2.ε(t-2) + θ3.ε(t-3)
#     Here instead of difference from previous term, we take errer term (ε) obtained from the difference from past term
# Now we need to figure out the values of p and q which are parameters of ARIMA model. We use below two methods to figure out these values  -
#
# **Autocorrelation Function (ACF):** It just measures the correlation between two consecutive (lagged version). example at lag 4, ACF will compare series at time instance t1…t2 with series at instance t1–4…t2–4
#
# **Partial Autocorrelation Function (PACF):** is used to measure the degree of association between X(t) and X(t-p).


acf_lag = acf(train_df.diff().dropna().values, nlags=20)
pacf_lag = pacf(train_df.diff().dropna().values, nlags=20, method='ols')

model = ARIMA(train_df.values, order=(5,0,3))
model_fit = model.fit(disp=0)

# Plot residual errors

residuals = pd.DataFrame(model_fit.resid)

# # Forecast

fc, se, conf = model_fit.forecast(480, alpha=0.05)  # 95% conf

# Make as pandas series
fc_series = pd.Series(fc, index=test_df.index)
lower_series = pd.Series(conf[:, 0], index=test_df.index)
upper_series = pd.Series(conf[:, 1], index=test_df.index)

# converting dataframe to a csv file
df = pd.DataFrame(fc_series, columns=['values'])
df.to_csv('C:/Users/Reddy/Desktop/PROJECT/model/ModelOutput.csv',header=True)
