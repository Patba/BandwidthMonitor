import sched
from datetime import datetime
from typing import List
import matplotlib.pyplot as mpl
import psutil
import re
import time
import log_input_output as lio
import utils

"""
s scheduling task for grabbing network data
"""


# s = sched.scheduler(time.time, time.sleep)

def create_log_li(primary_values: list[list] or list[list[str]]) -> List[str]:
    def get_bytes(option: int) -> float:
        """
        :param option: O or 1 - represents data (1)received and data sent(0)
        :return: float of data received if option == 0, float of data sent if option == 1
        """
        if -1 < option > 1:
            raise ValueError("option != 1 or 2")
        network_bytes = str(psutil.net_io_counters())
        cache = re.findall(r"[0-9]+", network_bytes)
        return float(cache[option])

    def bytes_to_megabytes(bytes_num: float) -> str:
        return str(round(bytes_num / 1048576, 2))

    if len(primary_values) == 0:
        primary_values.append(bytes_to_megabytes(get_bytes(0)))
        primary_values.append(bytes_to_megabytes(get_bytes(1)))
        return [str(utils.get_time()), "0", "0"]

    return [
        str(utils.get_time()),
        str(round(float(bytes_to_megabytes(get_bytes(1))) - float(primary_values[1]), 4)),
        str(round(float(bytes_to_megabytes(get_bytes(1))) - float(primary_values[1]), 4))]


def plot_network_graph(data: List[float]) -> None:
    """

    :param data:
    :return:
    """
    mpl.plot(data)
    mpl.ylabel("Megabytes Received")
    mpl.xlabel("Sexonds")
    mpl.show()


#
# def get_plot_data(data: list[float], time_to_clear: int):
#     temporary_data = []


def plot_data(sc, interval_data: list[float], interval: int, new_data: list[float]):
    #sc.enter(1, 0, get_plot_data, (sc,))
    #return interval_data
    pass


def main() -> None:
    # ALBO 'a' ALBO 'r' xD
    log = lio.LogInputOutput("log", ["Data", "MB_Received", "MB_Sent"], "r")

    #historical_data = []
    #
    # # s.enter(1, 0, get_plot_data(), (s,))
    # # s.run()
    #
    # log.add_csv_header()
    primary_values = []

    # for i in range(30):
    #     log.csv_writer(create_log_li(primary_values))
    #     print(utils.get_time())
    #     time.sleep(1)
    #     print("Minelo 1 sekunda, jebac biede")

    plot_network_graph(log.convert_csv_data())


if __name__ == '__main__':
    main()
