#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
from setuptools import setup
from pip.req import parse_requirements
from pip.exceptions import InstallationError
from setuptools.command.install import install

from oshino_jmx.version import get_version


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        from scripts.download_agent import fetch_jar
        fetch_jar()
        if not os.path.exists("etc/"):
            os.makedirs("etc")
            shutil.copy("scripts/etc/jmxconfig.yml", "etc/jmxconfig.yml")
        install.run(self)

try:
    install_reqs = list(parse_requirements("requirements.txt", session={}))
except InstallationError:
    # There are no requirements
    install_reqs = []

setup(name="oshino_jmx",
      version=get_version(),
      description="Collect JMX metrics from JVM services",
      author="Šarūnas Navickas",
      author_email="zaibacu@gmail.com",
      packages=["oshino_jmx"],
      install_requires=[str(ir.req) for ir in install_reqs],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"],
      cmdclass={"install": PostInstallCommand}
      )
