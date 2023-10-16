#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="django-otp-messagebird",
    version="0.2.1",
    description="A django-otp plugin that delivers tokens via MessageBird's SMS service.",
    author="arjan5",
    author_email="arjan.schrijver@foxcrypto.com",
    url="https://github.com/arjan-s/django-otp-messagebird",
    project_urls={
        "Documentation": "https://django-otp-messagebird.readthedocs.io/",
        "Source": "https://github.com/arjan-s/django-otp-messagebird",
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
    install_requires=["django-otp >= 0.9.2", "messagebird"],
)
