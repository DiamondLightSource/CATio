CATio
===========================

|code_ci| |docs_ci| |coverage| |pypi_version| |license|

Beckhoff produces a range of EtherCAT I/O terminals that can be connected to one
of their industrial PCs running TwinCAT. This gives real-time polling of the
EtherCAT bus, with set, get and monitor via the ADS protocol. CATio is designed
to run on a different machine, introspecting the I/O chain, and making a Device
for each of them automatically. It uses FastCS to create these Devices, which
means the resultant control system integration can use the EPICS or Tango
backends.

.. note::

    This repository is in an early stage of development, and doesn't currently do the above!

============== ==============================================================
PyPI           ``pip install catio``
Source code    https://github.com/DiamondLightSource/CATio
Documentation  https://DiamondLightSource.github.io/CATio
Releases       https://github.com/DiamondLightSource/CATio/releases
============== ==============================================================

.. |code_ci| image:: https://github.com/DiamondLightSource/CATio/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/DiamondLightSource/CATio/actions/workflows/code.yml
    :alt: Code CI

.. |docs_ci| image:: https://github.com/DiamondLightSource/CATio/actions/workflows/docs.yml/badge.svg?branch=main
    :target: https://github.com/DiamondLightSource/CATio/actions/workflows/docs.yml
    :alt: Docs CI

.. |coverage| image:: https://codecov.io/gh/DiamondLightSource/CATio/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/DiamondLightSource/CATio
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/CATio.svg
    :target: https://pypi.org/project/CATio
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

See https://DiamondLightSource.github.io/CATio for more detailed documentation.
