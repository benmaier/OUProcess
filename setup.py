from setuptools import setup

setup(name='ouprocess',
      version='0.1',
      description='Simulates an Ornstein-Uhlenbeck process in periodic boundary conditions',
      url='https://www.github.com/benmaier/ouprocess',
      author='Benjamin F. Maier',
      author_email='bfmaier@physik.hu-berlin.de',
      license='MIT',
      packages=['ouprocess'],
      install_requires=[
          'numpy',
      ],
      dependency_links=[
          ],
      zip_safe=False)
