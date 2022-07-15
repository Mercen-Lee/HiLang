from sys import argv; import re

class 인터프리터:
    def __init__(self):
        global 변수, 모듈; 변수 = {}; 모듈 = []

    def 계산(self, 수식, 수 = 1):
        try:
            while 수 < len(수식) and '*' in 수식 or '/' in 수식:
                if 수식[수] in ['*','/']:
                    이전 = int(수식[수-1]); 다음 = int(수식[수+1])
                    if 수식[수] == '*': 수식[수] = str(이전 * 다음)
                    elif 수식[수] == '/': 수식[수] = str(이전 // 다음)
                    del 수식[수-1]; del 수식[수]; 수 = 1
                else: 수 += 1
            while 수 < len(수식) and '+' in 수식 or '-' in 수식:
                if 수식[수] in ['+','-']:
                    이전 = int(수식[수-1]); 다음 = int(수식[수+1])
                    if 수식[수] == '+': 수식[수] = str(이전 + 다음)
                    elif 수식[수] == '-': 수식[수] = str(이전 - 다음)
                    del 수식[수-1]; del 수식[수]; 수 = 1
                else: 수 += 1
        except TypeError: print('오류 : 자료형이 잘못되었습니다!'); return
        return 수식

    def 불러오기(self, 이름):
        try: exec('from 모듈 import ' + 이름, globals()); 모듈.append(이름)
        except ModuleNotFoundError: print('오류 : 해당 모듈이 존재하지 않습니다!')

    def 실행(self, 명령어):
        if 명령어 == '': return ''
        입력 = re.split(r'(["\'])(.*?[^\\])\1| |([\+\-\*\/])', 명령어)
        명령 = self.계산([x for x in 입력 if x not in ['\'', '"', '', None]])
        if 명령[0] == '안뇽': return 명령[1]
        elif 명령[-1] == '불러오기': self.불러오기(명령[-2])
        elif 명령[-1] == '종료': exit()
        return ''

if len(argv) == 2:
    파일 = open(argv[1], encoding = 'UTF-8').readlines()
    실행기 = 인터프리터()
    for 줄 in 파일: print(실행기.실행(줄.replace('\n','')))