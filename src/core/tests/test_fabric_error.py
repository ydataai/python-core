from operator import contains
from ydata.core.error.fabric_error import FabricError


def test_basic_error():
  basic_error = FabricError()
  basic_error.name = "BasicError"
  basic_error.description = "This is a basic test error"
  basic_error.return_value = -1

  basic_error_dict = dict(basic_error)

  assert 'name' in basic_error_dict
  assert 'description' in basic_error_dict
  assert 'return_value' in basic_error_dict

def test_full_error():
  basic_error = FabricError(context={'a': 'a'}, http_code=500, name="FullError")
  basic_error.description = "This is a full test error"
  basic_error.return_value = -1

  basic_error_dict = dict(basic_error)

  assert 'name' in basic_error_dict
  assert 'description' in basic_error_dict
  assert 'return_value' in basic_error_dict
  assert 'context' in basic_error_dict
  assert 'http_code' in basic_error_dict

def test_extended_error():
  class CustomError(FabricError):
    description = "This is extended error"
    return_value = -2

  custom_error = CustomError(context={'a': 'a'}, http_code=500)

  custom_error_dict = dict(custom_error)

  assert 'name' in custom_error_dict
  assert 'description' in custom_error_dict
  assert 'return_value' in custom_error_dict
  assert 'context' in custom_error_dict
  assert 'http_code' in custom_error_dict
