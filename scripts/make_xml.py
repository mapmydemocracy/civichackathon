
import codecs
import os
import sys


# TODO: remove this hack.
def fix_sys_path():
    scripts_dir = os.path.dirname(__file__)
    repo_dir = os.path.join(scripts_dir, os.pardir)
    root_dir = os.path.join(repo_dir, 'src')
    root_dir = os.path.abspath(root_dir)
    sys.path.insert(0, root_dir)


def main():
    fix_sys_path()
    from VipFormat.emitAllXml import emitAll
    xml = emitAll()
    output_path = 'SF.xml'
    with codecs.open(output_path, 'w', encoding='utf8') as f:
        f.write(xml)


if __name__ == '__main__':
    main()
