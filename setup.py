import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tractor", # Replace with your own username
    version="0.0.1",
    author="Matt Wilber",
    description="Tractor card game implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mwilbz/tractor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'eventlet',
        'flask',
        'flask-socketio',
        'pytest',
        'shortuuid>=1.0.1'
    ]
)
