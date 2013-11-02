#!/usr/bin/python3
import os

def diskUsage(path):
    """
    Returns the number of bytes used by a directory and its descendants.
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childPath = os.path.join(path, filename)
            total += diskUsage(childPath)
    print('{0:<7} bytes'.format(total), path)
    return total

if __name__ == '__main__':
    path = '/home/harvey/code'
    diskUsage(path)
