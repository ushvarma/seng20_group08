from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='seng_20_group08',
    url='https://github.com/ushvarma/seng20_group08',
    author='group 08',
    author_email='ushvarma@gmail.com',
    # Needed to package the project.
    packages=['seng_20_group08'],
    # Needed for dependencies
    install_requires=['numpy'],
    # This is the first version
    version='0.1',
    # Using MIT Licenser
    license='MIT',
    description='Group 8 Home Work 1',
)
