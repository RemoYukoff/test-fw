# Testing Framework

## Getting Started

To get started with this testing framework, follow these steps:

### Prerequisites

1. Python 3.x: Make sure you have Python 3.x installed on your system.
2. Poetry: Install Poetry to manage project dependencies. You can install it using pip:

   ```bash
   pip install poetry
   ```

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/remox129/<update>
   ```

2. Navigate to the project directory.

   ```bash
   cd test-fw
   ```

3. Use Poetry to install project dependencies.

   ```bash
   poetry install
   ```

### Configuration

- Configure Selenium 4 for your preferred web browser.

### Usage

- Execute your tests using Pytest.

   ```bash
   poetry run pytest
   ```

## API Tests

The API tests were implemented using Postman. The selected API for testing is [WeatherAPI](https://rapidapi.com/weatherapi/api/weatherapi-com). Follow these steps to run the tests:

- Import the `postman/WeatherAPI.postman_collection.json` and `postman/WeatherAPI.postman_environment.json` into your Postman application.
- Reeplace `X-RapidAPI-Key` in the environment with your API key from [RapidAPI](https://rapidapi.com/)
- Run the collection to execute the API tests.
