#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from cx_Freeze import setup, Executable
# ez_setup.use_setuptools()

from schemasync import syncdb, utils

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'schemasync'))

build_options = dict(
    include_files=[],
    includes=[],
    packages=[],

)

setup(
    name='SchemaSync',
    version='0.9.4',
    description='A MySQL Schema Synchronization Utility',
    author='Vincent Fei',
    install_requires=['SchemaObject >= 0.5.7'],
    entry_points={
        'console_scripts': [
            'schemasync = schemasync.schemasync:main',
        ]
    },
    keywords=["MySQL", "database", "schema", "migration", "SQL"],

    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    options=dict(build_exe=build_options),
    executables=[
        Executable(
            script='schemasync/schemasync.py',
            # base="win32gui",
            targetName='schemasync',  # 生成exe的名字
            # icon="Test.ico"  # 生成exe的的图标
        )
    ]
)
