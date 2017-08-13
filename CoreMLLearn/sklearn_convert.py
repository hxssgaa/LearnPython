from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('real_estate.csv')
X_train = data[["Size", "Bathrooms", "Bedrooms"]]
y_train = data["Price"]

# Train a model
model = LinearRegression()
model.fit(X_train, y_train)
print("Mean squared error: %.2f"
      % np.mean((model.predict(X_train) - y_train) ** 2))
print('Variance score: %.2f' % model.score(X_train, y_train))

# Convert and save the scikit-learn model
import coremltools
coreml_model = coremltools.converters.sklearn.convert(model, ["size", "bathroom", "bedroom"], "price")

# Set model metadata
coreml_model.author = 'David Huang'
coreml_model.license = 'BSD'
coreml_model.short_description = 'Predicts the price of a house.'

# Set feature descriptions manually
coreml_model.input_description['bedroom'] = 'Number of bedrooms'
coreml_model.input_description['bathroom'] = 'Number of bathrooms'
coreml_model.input_description['size'] = 'Size (in square feet)'

# Set the output descriptions
coreml_model.output_description['price'] = 'Price of the house'

# Save the model
coreml_model.save('HousePricer.mlmodel')

# Make predictions
# predictions_ml = coreml_model.predict({'bedroom': 1.0, 'bathroom': 1.0, 'size': 1240})
predictions_lg = model.predict(np.matrix([1500, 1.0, 1.0]))
# print "CoreML Predicts:", predictions_ml
print "LinearRegression Predicts:", predictions_lg
# plt.scatter(X_train, y_train, color='black')
# plt.plot(X_train, model.predict(X_train), color='blue',
#          linewidth=3)

# plt.show()
