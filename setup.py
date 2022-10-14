from pathlib import Path
from setuptools import setup, find_namespace_packages

here = Path(__file__).parent.resolve()

version = (here / 'VERSION').read_text().rstrip("\n")

setup(name='ydata-core',
      version=version,
      description='Core functionality for all python packages at YData',
      author='YData',
      author_email='developers@ydata.ai',
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      url='https://github.com/ydataai/python-core',
      package_dir={'': 'src'},
      packages=find_namespace_packages('src'),
      include_package_data=True,
      options={"bdist_wheel": {"universal": True}})
