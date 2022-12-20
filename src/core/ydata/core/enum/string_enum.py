from enum import Enum


class StringEnum(Enum):
  @classmethod
  def _missing_(cls, value):
    if isinstance(value, str):
      upper_value = value.upper()

      key = StringEnum._key_from_str_(upper_value)
      if key is not None:
        return key

      lower_value = value.lower()

      key = StringEnum._key_from_str_(lower_value)
      if key is not None:
        return key

    raise ValueError(f"{value} is not a valid {cls.__name__}")

  @classmethod
  def _key_from_str_(cls, value: str):
    if value in cls.__members__:
      return cls(value)

    return None

  def __eq__(self, other: object) -> bool:
    return self.value == other.value
