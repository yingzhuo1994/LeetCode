# 1st solution
class OrderedStream:
    def __init__(self, n: int):
        self.a = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.a[idKey] = value
        start = self.ptr
        while self.ptr < len(self.a) and self.a[self.ptr]:
            self.ptr += 1
        return self.a[start: self.ptr]
