class Filters:
    _size: int = 15
    _page: int = 0
    _sort_by: str = ""

    def __init__(self, size, page, sort_by):
        self._size = size
        self._page = page
        self._sort_by = sort_by

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def page(self):
        return self._size

    @page.setter
    def page(self, page):
        self._page = page

    @property
    def sort_by(self):
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        self._sort_by = sort_by