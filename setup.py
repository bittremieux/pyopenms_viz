from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyopenms_viz",
    version="0.1.0",
    author="OpenMS Contributors",
    author_email="your.email@example.com",
    description="Visualization tools for pyOpenMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcharkow/pyopenms-viz/",
    packages=find_packages(where="pyopenms_viz"),
    package_dir={"": "pyopenms_viz"},
    include_package_data=True,
    install_requires=[
        "pandas",
        "bokeh>=3.4.1",
        # Add other dependencies here
    ],
    entry_points={
        "pandas_plotting_backends": [
            "ms_bokeh = pyopenms_viz._bokeh",
            "ms_plotly = pyopenms_viz._plotly",
            "ms_matplotlib = pyopenms_viz._matplotlib",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.9",
)
