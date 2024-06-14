from flask import Flask, jsonify, request
import requests

app = Flask("Weather application with API")

API_KEY = '4d5a84e666fbecccf811a963a32a2e92'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/weather', methods=['GET'])
def get_weather():
    city_id = request.args.get('city')

    if not city_id:
        return jsonify({'error': 'City parameter is required'}), 400

    try:
        params = {
            'id': city_id,
            'appid': API_KEY,
            'units': 'metric'
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({'error': f'Failed to fetch weather data. Status code: '
                                     f'{response.status_code}'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request failed: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
