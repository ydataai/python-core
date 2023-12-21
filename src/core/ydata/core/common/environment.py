import os
from argparse import ArgumentParser
from enum import Enum

from dotenv import load_dotenv


class Environment(Enum):
  DEV = "development"
  PROD = "production"

  @classmethod
  def detect(cls, parser: ArgumentParser = ArgumentParser(description='parse environment')):
    parser.add_argument('--env', type=str, required=False)

    args, _ = parser.parse_known_args()
    env_string = args.env or 'prod'

    if env_string in ('dev', 'development'):
      env_string = 'development'
    elif env_string in ('prod', 'production'):
      env_string = 'production'
    else:
      raise ValueError('missing environment')

    return cls(env_string)

  def load(self):
    # load the file specific to the environment
    load_dotenv(f'.env.{str(self.name).lower()}')
    load_dotenv(f'.env.{self.value}')

    # Load the .env file if exists with default values
    load_dotenv()

  @staticmethod
  def get(key: str, default=None):
    return os.getenv(key, default=default)

  @staticmethod
  def set(key: str, value: str):
    os.environ[key] = value
