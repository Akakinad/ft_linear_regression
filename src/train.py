# import pandas as pd

# def load_data(path):
#     data = pd.read_csv(path)
#     return data

# if __name__ == "__main__":
#     dataset_path = "data/raw/data.csv"
#     data = load_data(dataset_path)
#     #print(data.head())

#     # Extract features and target
#     km = data["km"].values
#     price = data["price"].values

#     # Number of data points
#     m = len(km)

#     # Initialize parameters
#     theta0 = 0.0
#     theta1 = 0.0

#     print(f"Number of samples (m): {m}")
#     print(f"Initial theta0: {theta0}")
#     print(f"Initial theta1: {theta1}")






# import pandas as pd

# def load_data(path):
#     data = pd.read_csv(path)
#     return data

# def estimate_price(theta0, theta1, km):
#     return theta0 + theta1 * km

# if __name__ == "__main__":
#     dataset_path = "data/raw/data.csv"
#     data = load_data(dataset_path)

#     # Extract and scale features
#     km = data["km"].values
#     km = km / 100000  # scale down for stability
#     price = data["price"].values
#     m = len(km)

#     theta0 = 0.0
#     theta1 = 0.0

#     learning_rate = 0.01  # reasonable small step
#     iterations = 1000

#     for _ in range(iterations):
#         predictions = estimate_price(theta0, theta1, km)
#         errors = predictions - price

#         tmp_theta0 = learning_rate * (1 / m) * errors.sum()
#         tmp_theta1 = learning_rate * (1 / m) * (errors * km).sum()

#         # Simultaneous update
#         theta0 = theta0 - tmp_theta0
#         theta1 = theta1 - tmp_theta1

#     print("Training completed")
#     print(f"theta0: {theta0}")
#     print(f"theta1: {theta1}")

# # Save theta values
# with open("thetas.txt", "w") as f:
#     f.write(f"{theta0}\n")
#     f.write(f"{theta1}\n")









import pandas as pd
import numpy as np

def load_data(path):
    data = pd.read_csv(path)
    return data

def estimate_price(theta0, theta1, km):
    return theta0 + theta1 * km

if __name__ == "__main__":
    dataset_path = "data/raw/data.csv"
    data = load_data(dataset_path)

    # Extract and scale features
    km = data["km"].values
    km = km / 100000  # scale down for stability
    price = data["price"].values
    m = len(km)

    theta0 = 0.0
    theta1 = 0.0

    learning_rate = 0.01
    iterations = 1000

    # Track errors over iterations
    error_history = []

    for iteration in range(iterations):
        predictions = estimate_price(theta0, theta1, km)
        errors = predictions - price

        mse = (1 / m) * (errors ** 2).sum()
        error_history.append(mse)

        tmp_theta0 = learning_rate * (1 / m) * errors.sum()
        tmp_theta1 = learning_rate * (1 / m) * (errors * km).sum()

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    # Save error history for visualization
    np.savetxt("error_history.txt", error_history)

    print("Training completed")
    print(f"theta0: {theta0}")
    print(f"theta1: {theta1}")

    # Save theta values
    with open("thetas.txt", "w") as f:
        f.write(f"{theta0}\n")
        f.write(f"{theta1}\n")
