class Dict2:
    def __init__(self):
        self.key_value_pairs = []

    def __getitem__(self, key):
        for k, v in self.key_value_pairs:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found.")

    def __setitem__(self, key, value):
        for pair in self.key_value_pairs:
            if pair[0] == key:
                pair[1] = value
                break
        else:
            self.key_value_pairs.append([key, value])

    def __iter__(self):
        return iter([pair[0] for pair in self.key_value_pairs])

class DictKeyNotFoundError(Exception):
    pass

if __name__ == "__main__":
    obj = Dict2()
    obj['a'] = 1
    obj['b'] = 2
    obj['c'] = 3

    try:
        val = obj['d']
    except KeyError as e:
        print(e)  # Outputs: Key 'd' not found.

    for k in obj:
        print(f'key: {k}')
