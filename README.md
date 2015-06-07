# Who Can I Vote For?

This project contains a Python script to generate an XML file of open
elections data about the [November 2015 Municipal Election][sfelections]
in San Francisco.  The XML file conforms to version 5.0 of the
[Voting Information Project's][vip] election data spec, which is nearly
finalized.

The Voting Information Project is a partnership between Pew Charitable
Trusts and Google.  Google uses the VIP format when pulling in data
about jurisdictions to power its Google Civic API.


Setup
-----

Pull the repo.  Also pull any submodules:

    $ git submodule update --init --recursive

Use Python 3.4.

To regenerate the XML, from the repo root:

    $ python scripts/make_xml.py

To check the XML, from the repo root (you need `xmllint` installed):

    $ ./check-xml.sh


[sfelections]: http://www.sfgov2.org/index.aspx?page=599
[vip]: https://github.com/votinginfoproject/vip-specification
