# coding: utf-8

"""
    MINT Data Catalog

    API Documentation for MINT Data Catalog  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: danf@usc.edu
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "datacatalog-api"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="MINT Data Catalog",
    author_email="danf@usc.edu",
    url="https://pypi.org/project/datacatalog-api/",
    keywords=["OpenAPI", "OpenAPI-Generator", "MINT Data Catalog"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    API Documentation for MINT Data Catalog  # noqa: E501
    """
)
