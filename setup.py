import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="remita-billing-gateway",
    version="3.0.0",
    author="SystemSpecs Limited",
    author_email="ipgtechnologyteam@gmail.com",
    description="Python SDK for Remita Billing Gateway Service simple APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RemitaNet/billing-gateway-sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    requests='>=2.22.0',
)