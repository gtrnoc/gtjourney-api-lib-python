from setuptools import setup

setup(
    name='gtjourney-api-lib-python',
    version='0.1.0',
    author='Georgia Tech RNOC',
    author_email='rnoc-lab-staff@lists.gatech.edu',
    description='An internal library providing support for building APIs in Python for GT Journey',
    packages=['flask_wso2apim_auth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'PyJWT',
        'cryptography'
    ],
)