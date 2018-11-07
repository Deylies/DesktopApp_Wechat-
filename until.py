import os

def Path(*par):
    abs_path = os.getcwd()
    return os.path.join(abs_path,*par)

if __name__ == '__main__':
    print(Path('static','icon'))