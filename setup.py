import pathlib
from importlib_metadata import entry_points
from setuptools import setup

# The directory containing this file.
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name = "MlMetrics",
    version="1.0.0",
    description="To Evaluates Metrics of Ml Algorithms and Store into DataFrame",
    long_description=README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/chinna-babu6921/MlMetrics.git" ,
    author = "NoobyCoders",
    author_email = 'noobycoder6921@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["ClassificationModels"],
    include_package_data=True,
    install_requires=["scikit-learn","pandas"],
)