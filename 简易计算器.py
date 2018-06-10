# 简易计算器
# 优化版
# 必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致

import re

# 进行加减运算
def add(s):
    temp = re.search('-?\d+\.?\d*[+-]\d+\.?\d*', s)
    if temp is None:
        return re.search('[+-]?\d+\.?\d*',s).group()
    temp = temp.group()
    if '+' in temp:
        x, y = temp.split('+')
        temp1 = str(float(x) + float(y))
    elif '-' in temp:
        if temp.count('-') == 2:
            x,y,z = temp.split('-')
            temp1 = str(0-float(y) - float(z))
        else:
            x, y = temp.split('-')
            temp1 = str(float(x) - float(y))
    return s.replace(temp, temp1)
	
	
# 进行乘除运算
def mul(s):
    temp = re.search('\d+\.?\d*[*/]-?\d+\.?\d*',s).group()
    if '*' in temp:
        x, y = temp.split('*')
        temp1 = str(float(x) * float(y))
    elif '/' in temp:
        x, y = temp.split('/')
        temp1 = str(float(x) / float(y))
    return s.replace(temp, temp1)


# 格式化字符串 主要针对出现“+-”或者“--”这种类型
def format(s):
    s = s.replace('+-','-')
    s = s.replace('-+','-')
    s = s.replace('--','+')
    s = s.replace('++','+')
    return s
	
	
# 判断输入的表达式是否正常
def judge(s):
    ret = re.sub(' ', '', s)
    if re.search('[A-Za-z]', ret) is None:
        return ret
    else:
        return None
		
		
#主函数
def computer(s):
    ret = judge(s)
    if ret is None:
        print("输入的表达式不合法")
        return
    while '(' in ret:
        temp = re.search('\([^()]+\)',ret).group()
        temp1 = temp
        while '*' in temp1 or '/' in temp1:
            temp1 = mul(format(temp1))
        while '+' in temp1 or '-' in temp1:
            temp1 = add(format(temp1))
            if temp1.split('-')[0] == '':
                break
        temp1 = re.search('(-\d+\.?\d*)|(\d+\.?\d*)',temp1).group()
        ret = ret.replace(temp,temp1)
    else:
        temp = ret
        temp1 = ret
        while '*' in temp1 or '/' in temp1:
            temp1=mul(format(temp1))
        while '+' in temp1 or '-' in temp1:
            temp1=add(format(temp1))
            if re.split('[+-]',temp1)[0] == '':
                break
        temp1 = re.search('[+-]?\d+\.?\d*',temp1).group()
        ret = ret.replace(temp, temp1)
    return ret


if __name__ == '__main__':
    s = '1 - 2 * ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * ' \
        '(-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    result = computer(s)
    print("计算结果：%s = %s" % (s, result))
