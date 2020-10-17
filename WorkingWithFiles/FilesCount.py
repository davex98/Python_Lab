import os


def countFilesInDirectory(path: str):
    return len(os.listdir(path))


if __name__ == '__main__':
    print("/dev consists of {} files.".format(countFilesInDirectory("/dev")))
