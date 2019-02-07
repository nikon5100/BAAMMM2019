import main
print("global")
print(__name__)
if __name__ == "__main__":
    print('local')
    

# __name__ = 'test' 혹은 '__main__'
# 이 구조는 test에서 시작하여, main을 불러와서 main에서 다시 새로운 test를 불러와서 실행
