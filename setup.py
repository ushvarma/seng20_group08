from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='seng_20_group08',
    url='https://github.com/ushvarma/seng20_group08',
    author='group 08',
    author_email='ushvarma@gmail.com',
    # Needed to package the project.
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy'],
    # This is the first version
    version='1.0',
    # Using MIT Licenser
    license='MIT',
    description='Group 8 Home Work 1'
)
