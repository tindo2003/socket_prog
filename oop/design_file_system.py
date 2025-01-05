from collections import defaultdict


class FileSystem:
    """
    @param path: the path to be created
    @param val: path associated value
    @return: the result of create
    """

    def __init__(self):
        self.my_dict = {}
        self.my_dict = {"/": {}}
        self.storage = defaultdict(int)

    def createPath(self, path: str, val: int) -> bool:
        path_lst = path.split("/")
        N = len(path_lst)
        cur_dict = self.my_dict["/"]
        if len(path_lst[0]):
            return False
        for item in path_lst[1 : N - 1]:
            if len(item) == 0:
                return False
            if not item.isalpha():
                return False
            if item not in cur_dict:
                return False
            cur_dict = cur_dict[item]

        if path_lst[-1] in cur_dict:
            return False
        else:
            cur_dict[path_lst[-1]] = {}
            self.storage[path] = val
        return True

    """
    @param path: the path of retrieve
    @return: path associated value
    """

    def get(self, path: str) -> int:
        if path in self.storage:
            return self.storage[path]
        return -1


def main():
    fs = FileSystem()
    print(fs.get("/sunt"))
    print(fs.createPath("/consectetur", 1))
    print(fs.get("/consequatur/consectetur"))
    print(fs.createPath("/sequi/consequatur", 2))
    print(fs.createPath("/consectetur/sunt/consectetur", 3))
    print(fs.get("/consectetur"))
    print(fs.get("/sunt/consequatur"))
    print(fs.createPath("/consectetur/sequi/sequi", 4))
    print(fs.createPath("/sequi", 5))
    print(fs.createPath("/aliquid/consectetur", 6))
    print(fs.get("/aliquid/consectetur/sequi"))
    print(fs.get("/consectetur/aliquid/consequatur"))
    print(fs.get("/consectetur/consectetur/sunt"))
    print(fs.get("/sequi"))
    print(fs.createPath("/consequatur", 7))
    print(fs.createPath("/consequatur", 8))
    print(fs.get("/sequi"))
    print(fs.get("/consequatur/sunt/sunt"))
    print(fs.get("/consectetur/sequi/consequatur"))
    print(fs.createPath("/aliquid/consectetur", 9))
    print(fs.get("/sunt/aliquid"))
    print(fs.get("/sequi/sequi"))
    print(fs.createPath("/sunt", 10))
    print(fs.get("/consequatur"))
    print(fs.createPath("/sequi/consequatur", 11))
    print(fs.createPath("/sequi", 12))
    print(fs.get("/sunt/consectetur/consectetur"))
    print(fs.get("/aliquid"))
    print(fs.get("/consectetur/aliquid"))
    print(fs.get("/consequatur/consequatur"))
    print(fs.createPath("/consectetur/sunt", 13))
    print(fs.get("/consequatur/consectetur/consequatur"))
    print(fs.get("/consequatur/sequi"))
    print(fs.createPath("/consequatur/aliquid", 14))


if __name__ == "__main__":
    main()
