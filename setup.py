from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

from frappe_list_unassign_from import __version__ as version

setup(
    name='frappe_list_unassign_from',
    version=version,
    description='A Frappe plugin that adds the support of unassign from for multiple selection in list.',
    author='Ameen Ahmed (Level Up)',
    author_email='kid1194@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
