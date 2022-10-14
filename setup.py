import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="template-python",  # Replace with your own username
    version="0.0.1",
    author="Roboflow",
    author_email="jacob@roboflow.com",
    description="<INSERT_DESCRIPTION>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<INSERT_URL>",
    install_requires=[
      # list your requires
    ],
    packages=find_packages(exclude=("tests",)),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
