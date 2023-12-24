
# Weather Forecast Application

## Project Overview
This Weather Forecast Application is a web-based tool that provides users with current and future weather information. Utilizing APIs like Geoapify for location-based services and OpenWeatherMap for weather data, the app offers an intuitive interface with autocomplete functionality for city names.

## Interface Screenshots

Here are some screenshots of the Weather Forecast Application interface:

![Screenshot 1 Description](URL_TO_SCREENSHOT_1)
![Screenshot 2 Description](URL_TO_SCREENSHOT_2)

## Live Preview

You can access a live preview of the application hosted on Google Cloud here: [Weather Forecast Application Preview](URL_TO_GOOGLE_CLOUD_PREVIEW)


## Input/Output Model of the Backend

### Input:
- **City Name**: User inputs the name of the city for which they want weather information.

### Process:
- **Geocoding**: The app uses the Geoapify API to convert the city name into geographical coordinates (latitude and longitude).
- **Weather Data Retrieval**: Using the coordinates, the app fetches weather data from the OpenWeatherMap API.

### Output:
- **Weather Information**: The app displays weather information including temperature, humidity, wind speed, etc., for the selected location.

## Installation and Setup
Instructions on setting up the project locally. This includes steps to clone the repository, install dependencies, and any required environment setup.
To set up the Weather Forecast Application locally, follow these steps:
1. Clone the Repository (Skip this step if you have the project files already):
```bash
git clone [repository-url]
cd [project-directory]
```
2. Create a Virtual Environment:
- For Unix or MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
- For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
3.Install Dependencies
```bash
pip install -r requirements.txt
```
4.Run the Application
```bash
python run.py
```
## TO DO List (Future Enhancements)

- [ ] Implement User Authentication for personalized experiences..
- [ ] Implement additional error handling and validation for user inputs.
- [ ] Develop a mobile-responsive design.
- [ ] Optimize API usage to reduce load times
- [ ] Improve UI/UX design for a more engaging user interface.
