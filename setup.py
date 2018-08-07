# pylint: disable=missing-docstring
from setuptools import setup

with open("README.md", "r") as README:
    LONG_DESCRIPTION = README.read()

setup(
    name="fortlit",
    version="0.0.1",
    author="Marvin Steadfast",
    author_email="marvin@xsteadfastx.org",
    description=(
        "A fortune like program that displays a quote from literature "
        "where the actual time is mentioned"
    ),
    long_description=LONG_DESCRIPTION,
    package_dir={"": "src"},
    packages=["fortlit"],
    package_data={"fortlit": ["data/times.json"]},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        fortlit=fortlit:entrypoint
    """,
)
