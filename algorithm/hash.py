class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def get(self, key):
        hashcode = self._convert_key_to_hashcode(key)
        hash_index = hashcode % self.size

        hash_list = self.data[hash_index]
        for node in hash_list:
            if node.key == key:
                return node.value
        return None  # 해쉬테이블에 값 없음

    def put(self, key, value):
        hashcode = self._convert_key_to_hashcode(key)
        hash_index = hashcode % self.size
        hash_list = self.data[hash_index]
        node = self._search_key(hash_list, key)
        if not node:
            hash_list.append(Node(key, value))
        else:
            node.value = value

    def _convert_key_to_hashcode(self, key):
        result = 0
        for s in str(key):
            result += ord(s)
        return result

    def _search_key(self, hash_list, key):
        for node in hash_list:
            if node.key == key:
                return node
        return None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


if __name__ == '__main__':
    hash_table = HashTable(3)
    hash_table.put('hoyoung', 22)
    hash_table.put('A', 'a입니다') # 아스키 65 , % 3 == 2
    hash_table.put('B', 'b입니다.')  # 아스키 65 , % 3 == 2

    print(hash_table.data)

    print(hash_table.get('hoyoung'))
    print(hash_table.get('A'))
    print(hash_table.get('B'))
    print(hash_table.get('C')) # 없음

