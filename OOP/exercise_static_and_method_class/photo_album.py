from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self.build_pages()

    def build_pages(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count: int):
        new_pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(new_pages)

    def add_photo(self, label: str):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f'{label} photo added successfully on page {row + 1} slot {len(page)}'

        return f'No more free slots'

    def display(self):
        delimiter = '-' * 11
        result = delimiter

        for page in self.photos:
            page_str = ' '.join(['[]' for _ in page])
            result += '\n' + page_str + '\n' + delimiter
        return result
