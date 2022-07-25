import enum


class CategoryTypes(enum.Enum):
    SPORTS = "Sports"
    ELECTRONICS = "Electronics"
    BOOK = "Book"

    @classmethod
    def choices(cls):
        return [(category.name, category.value) for category in cls]
