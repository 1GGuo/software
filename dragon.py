import turtle

def dragon(curve, n):
    if n == 0:
        return
    
    for i in curve:
        if i == 'H':
            dragon('HLVF', n-1)
        elif i == 'V':
            dragon('FHRV', n-1)
        else:
            if i == 'F':
                turtle.fd(4)
            elif i == 'L':
                turtle.lt(90)
            elif i == 'R':
                turtle.rt(90)

turtle.speed(0) # 设置绘制速度

dragon('H', 10) # 绘制10阶龙形曲线

turtle.done()