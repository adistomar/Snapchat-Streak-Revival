# coding: utf-8
from setuptools import setup


with open('README.md') as readme_file:
   long_description = readme_file.read()


setup(
   name="snapstreak_revive",
   version="0.0.2",
   author="RoastSea8 (Aditya Tomar)",
   author_email="aditya26042005@gmail.com",
   description="Automatically enters required information on the Snapchat support website to retrieve snapstreaks.",
   license="MIT",
   keywords=['snapchat', 'streaks', 'revive streaks', 'chromedriver', 'automation', 'selenium'],
   url="https://github.com/RoastSea8/Snapchat-Streak-Revival",
   packages=["snapstreak_revive"],
   entry_points = {
        'console_scripts': ['revive_streak=snapstreak_revive.command_line:revive_streak'],
   },
   install_requires=['selenium', 'chromedriver_autoinstall'],
   long_description_content_type="text/markdown",
   long_description=long_description,
   python_requires=">=3.6",
   classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Topic :: Software Development :: Testing",
      "Topic :: System :: Installation/Setup",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: Microsoft :: Windows",
   ],
)