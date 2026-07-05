from setuptools import setup, find_packages
import os

# 确保能安全读取到 README.md
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="proxyvero_utils", 
    version="1.0.1",  # 💡 核心：版本号必须往上加，改成 1.0.1
    author="YourName",
    description="A utility pipeline to mitigate retry multipliers and proxy scraping errors in Python.",
    long_description=long_description,  # 💡 确保这里传入了读取到的变量
    long_description_content_type="text/markdown",  # 💡 告诉 PyPI 这是 Markdown 格式
    url="https://www.proxyvero.com", 
    project_urls={
        "Rotating Proxy Service": "https://www.proxyvero.com",  # 🔥 侧边栏词一
        "Are Free Proxies Safe": "https://www.proxyvero.com/guide/are-free-proxies-safe/", # 🔥 侧边栏词二
        "Residential Proxies": "https://www.proxyvero.com/guide/what-is-a-rotating-proxy/", # 🔥 侧边栏词三
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)