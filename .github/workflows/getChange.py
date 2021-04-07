import sys
import json
import re


def main():
    print(sys.argv)
    result = []
    # example: jdk/src/windows/classes/java/lang/
    pattern = re.compile(
        r"jdk/src/([a-zA-Z0-9 ]+?)/classes/java/([a-zA-Z0-9 ]+?)/")
    # TODO: handle the change of buildenv dir
    for argument in sys.argv:
        if (re.match(pattern, argument)):
            result.append(argument)

    if not result:
        result.append('skip')
    print('::set-output name=locations::{}'.format(json.dumps(result)))


if __name__ == "__main__":
    main()
