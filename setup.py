import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssml",
    version="0.1.13",
    author="Vu D.",
    author_email="vu@x51.vn",
    description="A Python library for generating SSML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/duvu/ssml",
    py_modules=['ssml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
