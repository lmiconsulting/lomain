from setuptools import setup


DESCRIPTION = "a library of standard, oft-needed utilities"

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    LONG_DESCRIPTION = DESCRIPTION

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="lomain",
    version="0.0.1",
    author="Lucas Hurley McCabe",
    author_email="lmccabe@lmi.org",
    packages=("lomain",),
    url="https://github.com/lmiconsulting/lomain",
    license="Apache-2.0 license",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=(
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache-2.0 license",
        "Programming Language :: Python :: 3",
    ),
    zip_safe=True,
    install_requires=required,
)
