"""Setup script for IgnoreGen."""

from setuptools import setup, find_packages
import os

def get_long_description():
    """Get long description from README"""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as fh:
            return fh.read()
    return "A CLI tool and Python package for generating .gitignore files"

setup(
    name="ignoregen",
    version="1.0.0",
    author="Victor Abimbola", 
    author_email="victor.abimbola@gmail.com",
    description="Smart .gitignore generator with auto-detection capabilities",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/victorabimbola/ignoregen",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Environment :: Console",
    ],
    keywords="gitignore git ignore generator cli developer-tools automation templates",
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "ignoregen=ignoregen.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
