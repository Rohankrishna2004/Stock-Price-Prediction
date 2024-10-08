#Stock Price prediction using python

# install libraries
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.style.use("bmh")
# load files
from google.colab import files
uploaded = files.upload()
# store the data in data frames
df =pd.read_csv('TSLA.csv')
df.head(6)
# get the no.of trading days
df.shape
#visualize the closing price data
plt.figure(figsize=(16,8))
plt.title("TESLA")
plt.xlabel('days')
plt.ylabel('Close Price USD$')
plt.plot(df['Close'])
plt.show()
# geting closing price data
df = df[['Close']]
df.head(4)
# creating variables to predict future days 
future_days = 30
df['Prediction'] = df[['Close']].shift(-future_days)
df.tail(4)
x = np.array(df.drop(['Prediction'], 1))[:-future_days]
print(x)
y = np.array(df['Prediction'])[:-future_days]
print(y)
# spliting of data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)
## create the models 
# create the desicion tree regessor model
# create linear regression model 
tree = DecisionTreeRegressor().fit(x_train,y_train)
lr = LinearRegression().fit(x_train,y_train)
#  getting of further projected data
x_future = df.drop(['Prediction'],1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
x_future
# model tree prediction
tree_prediction = tree.predict(x_future)
print(tree_prediction)
print()
# model  linear tree prediction
lr_prediction = lr.predict(x_future)
print(lr_prediction)
# visualizing and predicting data
predictions = tree_prediction
valid = df[x.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price USD$')
plt.plot(df['Close'])
plt.plot(valid[['Close','Predictions']])
plt.legend(['Orig','Val','Pred'])
plt.show()
# visualizing and predicting data
predictions = lr_prediction
valid = df[x.shape[0]:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price USD$')
plt.plot(df['Close'])
plt.plot(valid[['Close','Predictions']])
plt.legend(['Orig','Val','Pred'])
plt.show()
