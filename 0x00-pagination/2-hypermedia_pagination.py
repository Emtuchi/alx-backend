import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ start and end index derivation"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a dataset that has been adjusted to a particular size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        DataSet = self.dataset()

        desired_range_of_DataSet = DataSet[start_index:end_index]

        return desired_range_of_DataSet

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing key-value pairs"""
        New_DataSet = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(New_DataSet),
            'page': page,
            'data': New_DataSet,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }
