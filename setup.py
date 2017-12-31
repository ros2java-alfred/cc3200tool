from __future__ import print_function

import sys

from setuptools import find_packages
from setuptools import setup

if sys.version_info < (3, 5):
    print('cc3200_tool requires Python 3.5 or higher.', file=sys.stderr)
    sys.exit(1)

setup(
    name='cc3200tool',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    data_files=[
    ],
    author='Erwan Le Huitouze, Mickael Gaillard',
    author_email='erwan.lehuitouze@gmail.com, mick.gaillard@gmail.com',
    maintainer='Erwan Le Huitouze',
    maintainer_email='erwan.lehuitouze@gmail.com',
    url='https://github.com/ros2java-alfred/cc3200tool',
    download_url='https://github.com/ros2java-alfred/cc3200tool',
    keywords=['ROS', 'CC3200'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='cc3200tool is a tool to flash CC3200 board.',
    long_description="""\
""",
    license='Apache License, Version 2.0',
    entry_points={
        'console_scripts': [
            'cc3200tool = cc3200tool.cc:main',
        ],
    },
)
