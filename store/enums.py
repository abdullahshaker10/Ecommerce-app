import enum


class CategoryTypes(enum.Enum):
    SPORTS = "Sports"
    ELECTRONICS = "Electronics"
    BOOK = "Book"

    @classmethod
    def choices(cls):
        [(category, category.value) for category in cls]
