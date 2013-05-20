## Boolean Logic // take a string of boolean logic statements ##
## evaluate and return ##
##
## Order of operations matter!! ##
## 
##    NOT, AND, OR, XOR    ##
## 
## 'NOT' == '!' ## This NOT That -- 1 NOT 0 // 0 NOT 1
## 'AND' == '*' ## If both are T('1') then T('1')
## 'OR' == '|' ## If either is T('1') then T('1')
## 'XOR' == '^' ## If both then T('1') else F('0')
##

import sys

class LogicCalc(object):

    def boolEval(self, statement):
        op = {'^':4, '|':3, '*':2, '!':1}
        stack = [i for i in statement if i in op]
        parse = [i for i in statement if not i.isspace()]
        stack = sorted(stack, key=op.get)
        comps = 1
        while len(stack) > 0:
            new = '0'
            if (stack[0] == '^' and 
                parse[parse.index(stack[0]) - 1] == parse[parse.index(stack[0]) + 1]):
                new = '1'
            if stack[0] == '|':
                if (parse[parse.index(stack[0]) - 1] == '1' or 
                    parse[parse.index(stack[0]) + 1] == '1'):
                    new = '1'
            if (stack[0] == '*' and parse[parse.index(stack[0]) -1] == '1' and 
                parse[parse.index(stack[0]) + 1] == '1'):
                new = '1'
            if stack[0] == '!' and parse[parse.index(stack[0]) - 1] == '1':
                new = '1'
            print '%d Evaluation %s %s %s = %s' % (comps, parse[parse.index(stack[0]) - 1], 
                                                   stack[0], parse[parse.index(stack[0]) + 1], new)
            parse[parse.index(stack[0]) - 1] = new
            pos = parse.index(stack[0])
            parse.pop(pos)
            parse.pop(pos)
            stack.pop(0)
            comps += 1
            print 'Evaluation statement is now: %s' % ''.join([i for i in parse])
        print 'Outcome... ',parse[0]


if __name__ == '__main__':
    logcal = LogicCalc()
    try:
        data = sys.argv[1]
        print data
        logcal.boolEval(data)
    except IndexError:
        print 'No input was given'
