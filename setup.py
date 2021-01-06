import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-reservedseating',
    version='0.0.3',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="CPAL-1.0",
    url="https://mindpowered.dev/",
    description="ReservedSeating",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['reservedseating'],
    packages=['mindpowered_reservedseating'],
    package_dir={'mindpowered_reservedseating': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
