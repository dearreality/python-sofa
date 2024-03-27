from setuptools import setup, find_packages
from os import getenv


version = getenv("PYTHON_SOFA_VERSION", "0.0.0")

setup(
    name="dr-python-sofa",
    version=version,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["numpy", "scipy>=1.2.0", "netcdf4", "datetime"],
    author="Jannika Lossner",
    author_email="jnlossner@gmail.com",
    description="Python SOFA API (Dear Reality Fork)",
    long_description=open("README.rst").read(),
    license="MIT",
    keywords="audio SOFA acoustics".split(),
    url="http://github.com/dearreality/python-sofa/",
    platforms="any",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
    ],
    zip_safe=True,
)
