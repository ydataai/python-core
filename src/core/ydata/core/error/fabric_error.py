from __future__ import annotations
import json
from typing import Optional


def _camelcased(value: str) -> str:
  capitalized = ''.join(x.capitalize() for x in value.split('_'))
  return capitalized[0].lower() + capitalized[1:]


class FabricError(Exception):
  context: Optional[dict[str, str]]
  description: str
  http_code: Optional[int]
  name: Optional[str]
  return_value: int

  def __init__(
      self,
      context: Optional[dict[str, str]] = None,
      http_code: Optional[int] = None,
      name: Optional[str] = None):
    self.context = context
    self.http_code = http_code
    self.name = name

  def __iter__(self):
    yield from {
      "context": self.context,
      "name": self.name if self.name else self.__class__.__name__,
      "description": self.description,
      "http_code": self.http_code,
      "return_value": self.return_value
    }.items()

  def __str__(self) -> str:
    return f'''
      {self.__class__.__name__}(name={self.name}, context={self.context}, description={self.description}, \
return_value={self.return_value})
    '''

  def __repr__(self) -> str:
    return self.__str__()

  def json(self):
    return json.dumps(self, default=lambda o: {_camelcased(k): v for k, v in dict(o).items()}, ensure_ascii=False)
