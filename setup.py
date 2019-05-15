import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VLC-radio",
    version="0.0.1",
    author="martinbarker99",
    author_email="martinbarker99@gmail.com",
    description="export VLC metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MartinBarker/VLC-Radio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)