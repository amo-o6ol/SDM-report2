#!/usr/bin/python3

import re
                
"""def calc(A,B):
        ai=str(A)
        bi=str(B)
        p = re.compile('\d+(\.\d+)?')
        if p.match(ai) or p.match(bi):
                a=float(ai)
                b=float(bi)
                if 0<a and a<b and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1"""
def calc(ai, bi):
    # 入力が整数であるかどうかを確認
    try:
        a = float(ai)  # 入力が数値に変換可能か
        b = float(bi)  # 入力が数値に変換可能か
    except ValueError:  # ValueErrorが発生した場合は無効な入力
        return -1

    # 1 <= a <= 999 および 1 <= b <= 999 の範囲内かどうかを確認
    if not (1 <= a <= 999 and 1 <= b <= 999):
        return -1

    # 正常な場合は掛け算の結果を返す
    return a * b


                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
