from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent.resolve()
root = here.parent.parent.resolve()

long_description = (root / 'README.md').read_text(encoding='utf-8')
version = (root / 'VERSION').read_text().rstrip("\n")

setup(name='ydata-datascience',
      version=version,
      description='Data science functionalities for all python packages at YData',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='YData',
      author_email='developers@ydata.ai',
      classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      url='https://github.com/ydataai/python-core',
      packages=find_packages(exclude=['ydata', 'tests']),
      include_package_data=True,
      options={"bdist_wheel": {"universal": True}})
