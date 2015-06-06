
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
    print(emitAll())


if __name__ == '__main__':
    main()
