# civichackathon
Who Can I Vote For?

Setup
-----

Pull the repo.  Also pull any submodules:

    $ git submodule update --init --recursive

Use Python 3.4.

To regenerate the XML, from the repo root:

    $ python scripts/make_xml.py

To check the XML, from the repo root (you need `xmllint` installed):

    $ ./check-xml.sh
