#look at the gameutils package to take this structure.
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ajn-lambdata-package",
    version="0.0.2",
    author="Alex JN",
    author_email="ajenkneary@gmail.com",
    description="Lambda Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/alexmjn/ajn-lambdata-package",
    packages=find_packages() # ["game_utils"]
)
