import setuptools

with open('README.md','r', encoding='utf-8') as file:
    long_description = file.read()
    
setuptools.setup(
    name="get-artifactory-delivery",
    version='0.0.1',
    description="download and deployment of file in artifactory",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts':[
            'getartifactorydelivery=getartifactorydelivery.main',
        ],
    },
    install_requires=[
        'requests==2.27',
        'beautifulsoup4==4.10'
    ]
)