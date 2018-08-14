from setuptools import setup

setup(
    name = "ringrunner",
    version = '0.1',
    description = "CLI for the NLNOG Ring Network",
    author = "orme292",
    url = "https://github.com/orme292/ringrunner-dev",
    packages = ['ringrunner'],
    license = "MIT",
    install_requires = ["terminaltables","colorclass","requests"],
    entry_points = {
        'console_scripts': [
            'ringrunner = ringrunner.main'
        ]
    }
)