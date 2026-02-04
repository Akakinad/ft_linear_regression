# def load_theta(file_path="thetas.txt"):
#     with open(file_path, "r") as f:
#         lines = f.readlines()
#         theta0 = float(lines[0].strip())
#         theta1 = float(lines[1].strip())
#     return theta0, theta1

# def predict_price(theta0, theta1, km):
#     km_scaled = km / 100000  # same scaling as in training
#     return theta0 + theta1 * km_scaled

# if __name__ == "__main__":
#     theta0, theta1 = load_theta()

#     try:
#         km_input = float(input("Enter car mileage (km): "))
#         price_estimate = predict_price(theta0, theta1, km_input)
#         print(f"Estimated price: {price_estimate:.2f}")
#     except ValueError:
#         print("Invalid input! Please enter a number.")








# def load_theta(file_path="thetas.txt"):
#     with open(file_path, "r") as f:
#         lines = f.readlines()
#         theta0 = float(lines[0].strip())
#         theta1 = float(lines[1].strip())
#     return theta0, theta1

# def predict_price(theta0, theta1, km):
#     km_scaled = km / 100000  # same scaling as in training
#     return theta0 + theta1 * km_scaled

# if __name__ == "__main__":
#     # Enhancement 1: Handle missing file
#     try:
#         theta0, theta1 = load_theta()
#     except FileNotFoundError:
#         print("Error: thetas.txt not found.")
#         print("Please run train.py first to train the model.")
#         exit(1)

#     # Prediction with input validation
#     try:
#         km_input = float(input("Enter car mileage (km): "))
        
#         # Enhancement 2: Validate non-negative
#         if km_input < 0:
#             print("Error: Mileage cannot be negative.")
#             exit(1)
        
#         price_estimate = predict_price(theta0, theta1, km_input)
#         print(f"Estimated price: {price_estimate:.2f}")
#     except ValueError:
#         print("Invalid input! Please enter a number.")








def load_theta(file_path="thetas.txt"):
    """Load theta values from file, or return 0,0 if file doesn't exist."""
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            theta0 = float(lines[0].strip())
            theta1 = float(lines[1].strip())
        return theta0, theta1
    except FileNotFoundError:
        # Return default values if not trained yet
        print("(Using untrained model - theta values are 0)")
        return 0.0, 0.0

def predict_price(theta0, theta1, km):
    km_scaled = km / 100000  # same scaling as in training
    return theta0 + theta1 * km_scaled

if __name__ == "__main__":
    theta0, theta1 = load_theta()

    try:
        km_input = float(input("Enter car mileage (km): "))
        
        # Validate non-negative
        if km_input < 0:
            print("Error: Mileage cannot be negative.")
            exit(1)
        
        price_estimate = predict_price(theta0, theta1, km_input)
        print(f"Estimated price: {price_estimate:.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")