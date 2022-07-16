import json
import os

from setuptools import setup

REQUIRES = [
    "requests>=2.28.1,<3",
]

DOCS_REQUIRE = [
    "mkdocs-material>=8.3.9,<9",
    "mkdocstrings[python]>=0.19.0",
]

EXTRAS_REQUIRE = {
    "docs": DOCS_REQUIRE
}

if os.path.exists("package-data.json"):
    with open("package-data.json") as file:
        data = json.loads(file.read())
else:
    data = {}

# we still specify requirements in here so PyCharm will pick them up.
if __name__ == "__main__":
    setup(install_requires=REQUIRES, extras_require=EXTRAS_REQUIRE, **data)
