import os

def demo_test():
    return True

def get_branch():
    return os.getenv("GITHUB_REF_NAME")

assert demo_test()
print('all tests passed')
print(get_branch())