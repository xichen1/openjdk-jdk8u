import sys
import json
import re


def main():
    print(sys.argv)
    result = []
    # pattern = re.compile(r"/(aaa)/([a-zA-Z0-9 ]+?)/")
    # TODO: handle the change of buildenv dir
    for argument in sys.argv:
        print(argument)

    if not result:
        result.append('skip')
    print('::set-output name=build_lists::{}'.format(json.dumps(result)))


if __name__ == "__main__":
    main()
