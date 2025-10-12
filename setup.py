#!/usr/bin/env python3.4

from distutils.core import setup

fr8_manpages = ["man/fr/man8/pydhcp.8.gz"]
fr3_manpages = [
    "man/fr/man3/pydhcplib3.3.gz",
    "man/fr/man3/pydhcplib3.DhcpBasicPacket.3.gz",
    "man/fr/man3/pydhcplib3.DhcpPacket.3.gz",
    "man/fr/man3/pydhcplib3.hwmac.3.gz",
    "man/fr/man3/pydhcplib3.ipv4.3.gz",
    "man/fr/man3/pydhcplib3.strlist.3.gz",
]
en3_manpages = [
    "man/man3/pydhcplib3.strlist.3.gz",
    "man/man3/pydhcplib3.3.gz",
    "man/man3/pydhcplib3.ipv4.3.gz",
]
en8_manpages = ["man/man8/pydhcp.8.gz"]

setup(
    name="pydhcplib3",
    version="0.7.1",
    license="GPL v3",
    description="Dhcp client/server library",
    author="Mathieu Ignacio",
    author_email="mignacio@april.org",
    maintainer="Allan Clark",
    maintainer_email="allanc@chickenandpork.com",
    # url="http://pydhcplib3.tuxfamily.org/",
    packages=["pydhcplib3"],
    scripts=["scripts/pydhcp"],
    data_files=[
        ("share/man/man8", en8_manpages),
        ("share/man/fr/man8", fr8_manpages),
        ("share/man/fr/man3", fr3_manpages),
        ("share/man/man3", en3_manpages),
    ],
)
