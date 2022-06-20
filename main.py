from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import requests

INTERVAL_IN_S=5
URLS = ["https://google.de", "https://heise.de", "http://localhost:8080"]

def main():
    fig, ax = plt.subplots()
    ax.set_yticklabels(URLS)
    ax.set_yticks(np.arange(0.5, len(URLS), 1))

    timestamps = []
    x = [0]
    i = 0

    print("timestamp," + ",".join(URLS))
    while True:
        time = datetime.now().strftime("%H:%M:%S")
        timestamps.append(time)
        ax.set_xticks(x)
        ax.set_xticklabels(timestamps)
        colors = []
        for n, endpoint in enumerate(URLS):
            try:
                response = requests.get(endpoint)
                color = "green" if response.status_code == 200 else "red"
            except requests.exceptions.ConnectionError:
                color = "red"
            plt.bar(i, 1, bottom=n, color=color, align='edge')
            colors.append(color)

        print(time + "," + ",".join(colors))
        i+=1
        x.append(i)
        plt.pause(INTERVAL_IN_S)

    plt.show()

if __name__ == '__main__':
    main()
