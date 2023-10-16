#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="django-otp-signal",
    version="0.1.0",
    description="A django-otp plugin that delivers tokens via Signal",
    author="arjan5",
    author_email="github@anymore.nl",
    url="https://github.com/arjan-s/django-otp-signal",
    project_urls={
        "Documentation": "https://django-otp-signal.readthedocs.io/",
        "Source": "https://github.com/arjan-s/django-otp-signal",
    },
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["django-otp >= 0.9.2", "pysignalclirestapi >= 0.3.21"],
)
