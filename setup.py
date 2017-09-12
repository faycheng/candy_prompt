# -*- coding:utf-8 -*-

from setuptools import find_packages, setup

README = """# candy_prompt
"""


setup(
    name='candy_prompt',
    version='0.0.1',
    description='wrapper of prompt-toolkit',
    long_description=README,
    author='程飞',
    url='https://github.com/faycheng/candy_prompt.git',
    packages=find_packages(exclude=['tests']),
    install_requires=['prompt_toolkit==1.0.15', 'pytest==3.2.1'],
    entry_points={
        'console_scripts': [],
    },
    zip_safe=True,
    license='MIT License',
    classifiers=['development status :: 1 - planning', 'intended audience :: developers', 'topic :: software development :: libraries', 'programming language :: python :: 3 :: only']
)