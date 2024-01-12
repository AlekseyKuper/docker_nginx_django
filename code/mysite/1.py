def get():
        data = []
        for i in range(10):
            value = ''.join([choice(ascii_letters) for _ in range(10)])
            data.append(value)
        return data
print(data)