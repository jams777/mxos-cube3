# Copyright (c) 2016 MXCHIP Limited, All Rights Reserved
# SPDX-License-Identifier: Apache-2.0

# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License.

# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied.

# updated Jams777<jams7777@gmail.com> : Reimplemented for Python 3.
# publish : https://pypi.org/project/mxos-cube3/

import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mxos-cube3",
    version="0.1.2",
    description="MXCHIP MXOS command line tool for python3.\n mxos-cube3 enables repositories version control, publishing and updating code from remotely hosted repositories, and invoking MXOS own build system and export functions, among other operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jams777/mxos-cube3',
    author='jams777',
    author_email='jams7777@gmail.com',
    packages=["mxos"],
    entry_points={
        'console_scripts': [
            'mxos=mxos.mxos:main',
            'mxos-cube=mxos.mxos:main',
        ]
    },
    python_requires='>=3,<4',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
