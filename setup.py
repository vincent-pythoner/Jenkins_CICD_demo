from setuptools import setup, find_packages

setup(
    name='Jenkins_CICD_demo',  # Name of the package
    version='0.1.0',          # Version of the package
    author='Vincent_Wang',       # Your name
    author_email='yttest1122@gmail.com',  # Your email
    description='A simple calculator package for Jenkins CI/CD demo',  # Short description
    long_description=open('README.md').read(),  # Read long description from README
    long_description_content_type='text/markdown',
    url='https://github.com/vincent-pythoner/Jenkins_CICD_demo',  # Repository URL
    packages=find_packages(where='src'),  # Packages found in the 'src' directory
    package_dir={'': 'src'},  # Package directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[         # Dependencies (if any)
        # Add dependencies if needed
    ],
)

