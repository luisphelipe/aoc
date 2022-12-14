import sys
import json
from functools import reduce


class File:
    def __init__(self, name, size):
        self.type = "file"
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def toJson(self):
        return {
            'name': self.name,
            'type': self.type,
            'size': self.size
        }


class Folder:
    def __init__(self, name):
        self.type = "folder"
        self.name = name
        self.size = 0
        self.children = {}

    def addChild(self, line):
        if line[:3] == 'dir':
            name = line[4:]
            if not self.children.get(name):
                self.children[name] = Folder(name)
        else:
            [size, name] = line.split(" ")
            if not self.children.get(name):
                self.children[name] = File(name, int(size))

    def getSize(self):
        if self.size:
            return self.size

        children_size = [0, 0]

        for key, child in self.children.items():
            children_size.append(child.getSize())

        size = reduce(lambda x, y: x + y, children_size)
        self.size = size

        return self.size

    def getFoldersSizeList(self):
        folders_size = [self.size]
        for key, child in self.children.items():
            if (child.type == "file"):
                continue
            folders_size.extend(child.getFoldersSizeList())
        return folders_size

    def toJson(self):
        return {
            'name': self.name,
            'size': self.size,
            'type': self.type,
            'children': [child.toJson() for child in self.children.values()]
        }


class Filesystem:
    def __init__(self):
        self._node = Folder('/')
        self.active_path = "/"
        self.size = 0
        self.total_size = 70000000

    def build(self):
        line = sys.stdin.readline()

        while line:
            self.processLine(line[:-1])
            line = sys.stdin.readline()

        self.size = self._node.getSize()

    def processLine(self, line):
        if line[:4] == '$ cd':
            self.cd(line[5:])
        elif line[:4] == '$ ls':
            pass
        else:
            self.addItem(line)

    def cd(self, path):
        DEBUG = False
        DEBUG and print(f"[{path}]:", self.active_path, end=" => ")

        if path == '/':
            self.active_path = '/'
        elif path == '..':
            separator = '/'
            path_parts = list(filter(None, self.active_path.split('/')))
            DEBUG and print(path_parts, "=> ", end="")
            new_path = '/' + separator.join(path_parts[:-1])
            if new_path != '/':
                new_path += '/'
            self.active_path = new_path
        else:
            self.active_path += path + '/'

        DEBUG and print(self.active_path)

    def addItem(self, line):
        node = self.getNodeFromPath()
        node.addChild(line)

    def getNodeFromPath(self):
        node = self._node
        path_parts = filter(None, self.active_path.split('/'))
        for part in path_parts:
            node = node.children[part]
        return node

    def listFoldersBySize(self):
        sizes = self._node.getFoldersSizeList()
        print(f"{len(sizes)} total folders")
        under_100001 = list(filter(lambda x: x < 100001, sizes))
        total_sum = reduce(lambda x, y: x + y, under_100001)
        print(f"{len(under_100001)} folders under 100001, totaling {total_sum} in size")

    def selectFolderToDelete(self):
        necessary_size = 30000000 - (self.total_size - self.size)
        sizes = self._node.getFoldersSizeList()
        sizes = sorted(sizes)
        for size in sizes:
            if size > necessary_size:
                print(size)
                return

    def print(self):
        json_three = json.dumps(self._node.toJson(), indent=2)
        print(json_three)


def main():
    filesystem = Filesystem()
    filesystem.build()
    #  filesystem.print()
    #  filesystem.listFoldersBySize()
    filesystem.selectFolderToDelete()


main()
