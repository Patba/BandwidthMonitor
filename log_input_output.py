import csv
from typing import List


class LogInputOutput:

    def __init__(self, filename: str, header: List[str], mode: str) -> None:
        """
        :param filename: name of the csv log file
        :param data: date from def get_time , megabytes received, megabytes sent
        :param header: the header of csv file i.e. "Data, MB_Received, MB_Sent"
        """
        self.filename = filename
        self.header = header
        self.log_file = open(f"{self.filename}.csv", mode, newline='')

    def add_csv_header(self) -> None:
        """
        Initialises  csv file for logging purposes
        :return: None
        """
        log_writer = csv.writer(self.log_file, delimiter=';')
        log_writer.writerow(self.header)

    def csv_writer(self, data: List[str]) -> None:
        """
        Writes current data into csv_file_init log file
        :return: None
        """
        if self.log_file:
            log_writer = csv.writer(self.log_file, delimiter=";")
            log_writer.writerow(data)

    def convert_csv_data(self) -> List:
        reader = csv.DictReader(self.log_file, delimiter=';')
        csv_data = []
        for row in reader:
            csv_data.append(float(row['MB_Received']))

        return csv_data


        #return [float(row['MB_Received']) for row in reader]

    def close_csv(self) -> None:
        """
        Closes self.log_file
        :return: None
        """
        self.log_file.close()

    # def csv_file_init(self):
    #     with open(f"{self.filename}.csv", 'w', newline='') as self.log_file:
    #         log_writer = csv.writer(self.log_file, delimiter=';')
    #         log_writer.writerow(self.header)
    #
    # def csv_writer(self):
    #     # with open(f"{self.filename}.csv", 'a', newline='') as fw:
    #     if not self.log_file.closed:
    #         log_writer = csv.writer(self.log_file, delimiter=";")
    #         log_writer.writerow(self.data)
