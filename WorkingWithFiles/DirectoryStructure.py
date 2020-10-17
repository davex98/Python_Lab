import os


def printDirectoryStructure(path: str):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = '-' * 3 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '-' * 3 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    printDirectoryStructure("/home/kuba/Python_Lab/")
