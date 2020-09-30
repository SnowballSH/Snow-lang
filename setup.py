from setuptools import setup

import re

with open('SnowLang/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# print(version)

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass


with open("docs/README.md", "r") as f:
    readme = f.read()

setup(name="SnowLang",
      packages=[
          "SnowLang",
          "SnowLang.app",
          "SnowLang.compiler",
          "SnowLang.errors",
          "SnowLang.interpreter",
          "SnowLang.lexer",
          "SnowLang.lexer.cogs",
          "SnowLang.lexer.cogs.keywords.json",
          "SnowLang.parser",
          "docs",
                ],
      author="SnowballSH",
      version=version,
      description="Snow Programming Language for beginners",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/SnowballSH/Snow-lang",
      download_url="https://github.com/SnowballSH/Snow-lang/archive/v0.5.1.8.tar.gz",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Topic :: Artistic Software"
      ], )
