# Diamond Price Predictor

![diamondpricepredictor](https://github.com/tejangupta/DiamondPricePredictor/assets/89571912/ad83a692-a9a8-4575-8f28-58fdf358e65c)

This project is a web application
that predicts the price of a diamond based on various features and characteristics of a diamond.
Users can input the carat, depth, table, dimensions, cut, color, and clarity of the diamond,
and the application will provide an estimated price based on the best model chosen from linear regression,
lasso regression, ridge regression, and elastic net regression

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Input form for users to enter diamond details such as carat, depth, table, dimensions, cut, color, and clarity.
- Validation to ensure all required fields are filled and have valid input.
- Prediction model that estimates the price of the diamond based on the provided inputs.
- Display of the estimated price to the user.
- Error handling for server communication and invalid input.

## Installation

To run the Diamond Price Prediction application locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/tejangupta/DiamondPricePredictor.git
 ````
or
```bash
git clone git@github.com:tejangupta/DiamondPricePredictor.git
```

2. Navigate to the project directory:

```bash
cd DiamondPricePredictor 
```

3. Install the required libraries or dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

4. Start the flask server: 

```bash
flask run
```

5. Open your web browser and visit `http://localhost:5000` to access the application.

## Usage 

1. Fill out the form with the details of the diamond you want to predict the price for.
2. Click the "Submit" button to initiate the prediction.
3. Wait for the estimated price to be displayed on the screen.
4. If any errors occur, such as missing fields or invalid input, appropriate error messages will be shown.

## Technologies 

The Diamond Price Prediction application is built using the following technologies:

- HTML, CSS, and JavaScript for the front-end user interface
- Flask for the server-side application
- Linear Regression (My Best Model) for predicting diamond prices
- Fetch API for communicating with the server
- Bootstrap for styling and responsive design

## Contribution 

Contributions to the Diamond Price Prediction project are welcome!
If you have any suggestions, bug reports, or feature requests, please open an issue on the project repository.
If you would like to contribute code, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/new-feature
```

3. Make your changes and commit them:

```bash
git commit -m "Add new feature"
```

4. Push the changes to your forked repository:

```bash
git push origin feature/new-feature
```

5. Open a pull request on the main repository, describing your changes and referencing the related issue if applicable.

## License

This project is licensed under the MIT License.

```arduino
Feel free to customize and modify this template to suit the specific details and requirements of your project. Provide detailed information about installation, usage, technologies used, and how others can contribute. Also, consider adding sections on troubleshooting, frequently asked questions, or any additional information that might be useful for users and contributors.
```
