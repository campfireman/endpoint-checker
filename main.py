from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import requests
import argparse


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('urls', type=str, nargs='+',
                        help='The endpoints to check')
    parser.add_argument('--interval_in_s', 
                        default=5, type=int,
                        help='The seconds between each batch of requests to wait')
    args = parser.parse_args()
    fig, ax = plt.subplots()
    ax.set_yticklabels(args.urls)
    ax.set_yticks(np.arange(0.5, len(args.urls), 1))

    timestamps = []
    x = [0]
    i = 0

    print("timestamp," + ",".join(args.urls))
    while True:
        time = datetime.now().strftime("%H:%M:%S")
        timestamps.append(time)
        ax.set_xticks(x)
        ax.set_xticklabels(timestamps)
        colors = []
        for n, endpoint in enumerate(args.urls):
            try:
                response = requests.get(endpoint, verify=False)
                color = "green" if response.status_code == 200 else "red"
            except requests.exceptions.ConnectionError:
                color = "red"
            plt.bar(i, 1, bottom=n, color=color, align='edge')
            colors.append(color)

        print(time + "," + ",".join(colors))
        i+=1
        x.append(i)
        plt.pause(args.interval_in_s)

    plt.show()

if __name__ == '__main__':
    main()
