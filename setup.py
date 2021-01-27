import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="converter-nmurphy101",
    version="1.0.0",
    author="Nicholas Murphy",
    author_email="nicholas.murphy@mnsu.edu",
    description="Takes an input and converts it to any number of potential options.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nmurphy101/converter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)