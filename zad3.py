"""
Listy.
Mając listę temperatur: [0.6, 1.2, -1.4, -1.2, 1.6, 1.5]
podaj maksymalną, minimalną temperaturę oraz średnią temeperaturę.
"""

if __name__ == '__main__':
    temperatures = [0.6, 1.2, -1.4, -1.2, 1.6, 1.5]

    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    avg_temperature = sum(temperatures) / len(temperatures)

    print(f'Max temperature:', max_temperature)
    print(f'Min temperature:', min_temperature)
    print(f'Avg temperature:', avg_temperature)
    print(f'Rounded avg temperature:', round(avg_temperature,2))