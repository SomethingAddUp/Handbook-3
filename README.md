# Portfolio #3: Current Weather App

## Description
A simple GUI application that displays the current temperature, weather emoji and description for
a given city. The application retrieves data from OpenWeatherMAP API, includes proper HTTP status
code validation, and contains retry logic to handle potential network instability.

## Tech Stack
- Python 3.14, PyQt5 (GUI)
- Requests (API Communication)

## API Source
- OpenWeatherMAP API : https://openweathermap.org/api

## Features
1. Accepts city name input with unlimited queries.
2. Retrieves the current temperature and weather condition with a single button click.
3. Display weather conditions using both text description and emoji.
4. Implements API error handling for invalid city input or server issues.

## Challenges
- Maintain consistent UI display styles between successful responses and error states.
- Simplify production code and handle API errors with helper functions.

## Setup & Run
1. Clone the repository to your local machine
   - git clone https://github.com/SomethingAddUp/Handbook-3.git
   - cd Handbook-3
2. Install dependencies required for the tests
   - pip install -r requirements.txt
3. Run the application
   - python app/weather.py
