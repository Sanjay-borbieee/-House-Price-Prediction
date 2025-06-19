from sklearn.linear_model import LinearRegression
import numpy as np


area = np.array([500, 1000, 1500, 2000, 2500, 3000]).reshape(-1, 1)
price = np.array([150000, 250000, 350000, 450000, 550000, 650000])


model = LinearRegression()
model.fit(area, price)


try:
    user_input = float(input("Enter the area of the house in square feet: "))
    test_area = np.array([[user_input]])
    

    predicted_price = model.predict(test_area)
    print(f"Predicted price for {user_input} sqft is ₹{int(predicted_price[0])}")
except ValueError:
    print("❌ Please enter a valid number for the area.")
