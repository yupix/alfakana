from setuptools import find_packages, setup
import pathlib


description = 'alphabet to katakana formatting library'
readme_file = pathlib.Path(__file__).parent/'README.md'
with readme_file.open(encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='alfakana',
    version='0.0.1',
    install_requires=["pysqlite3"],
    url='https://github.com/yupix/alfakana',
    author='yupix',
    author_email='yupi0982@outlook.jp',
    license='MPL 2.0',
    python_requires='>=3.8, <4.0',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.9.6',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ]
)
