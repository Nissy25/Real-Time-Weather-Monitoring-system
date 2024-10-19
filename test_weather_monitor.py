import unittest
from weather_monitor import fetch_weather, create_db

class TestWeatherMonitor(unittest.TestCase):

    def setUp(self):
        self.conn = create_db()

    def test_fetch_weather(self):
        data = fetch_weather('Delhi')
        self.assertIn('main', data)
        self.assertIn('temp', data['main'])

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
