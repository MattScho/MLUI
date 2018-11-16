from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

data = pd.read_csv("../DataAndModels/Data/IrisData.csv")
X = data[["SepalLen","SepalWidth","PetalLen","PetalWidth"]]
Y= data["n"]

# create model
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))



# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model#
model.fit(X, Y, epochs=150, batch_size=10)

# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
