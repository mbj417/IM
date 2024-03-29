from setuptools import setup, find_packages

setup(
    name='osm_im',
    description='OSM Information Model',
    long_description = open('README.rst').read(),
    version_command=('git describe --tags --long --dirty --match v*', 'pep440-git-full'),
    author='Mike Marchetti',
    author_email='mmarchetti@sandvine.com',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-version-command'],
    test_suite='nose.collector',
)
