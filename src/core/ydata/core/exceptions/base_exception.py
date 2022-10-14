import json
from typing import Optional


def __camelcased(value: str) -> str:
    c = ''.join(x.capitalize() for x in value.split('_'))
    return c[0].lower() + c[1:]


class BaseException(Exception):
    context: dict
    description: str
    http_code: int
    name: Optional[str]
    return_value: int

    def __init__(self, context: dict={}, name=None):
        self.context = context
        self.http_code = 0

    def __iter__(self):
        yield from {
            "context": self.context,
            "name": self.name if self.name else self.__class__.__name__,
            "description": self.description,
            "http_code": self.http_code if self.http_code else None,
            "returnValue": self.return_value
        }.items()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(name={self.name}, context={self.context} description={self.description}, return_value={self.return_value})'

    def __repr__(self) -> str:
        return self.__str__()

    def json(self):
        return json.dumps(error, default=lambda o: { __camelcased(k):v for k,v in dict(o).items() }, ensure_ascii=False)
