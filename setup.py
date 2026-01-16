from setuptools import setup

setup(
    name="seo-audit",
    version="0.1.0",
    py_modules=["seo_audit"],
    install_requires=[
        "playwright",
        "beautifulsoup4",
        "lxml",
    ],
    entry_points={
        "console_scripts": [
            "seo-audit=seo_audit:main",
        ],
    },
)
