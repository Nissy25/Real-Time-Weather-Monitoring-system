import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data and plot
def visualize():
    conn = sqlite3.connect('weather_data.db')
    query = '''
        SELECT date, city, AVG(temp) AS avg_temp
        FROM weather
        GROUP BY date, city
    '''
    df = pd.read_sql(query, conn)

    for city in df['city'].unique():
        city_data = df[df['city'] == city]
        plt.plot(city_data['date'], city_data['avg_temp'], label=city)

    plt.title('Average Daily Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    conn.close()

if __name__ == '__main__':
    visualize()
