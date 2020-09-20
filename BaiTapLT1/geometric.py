import math
def prob(n, p = 1/2):
    return pow(p, n)
def infoMeasure(n, p = 1/2):
    return -math.log2(prob(n, p))
def sumProb(n, p):
    '''
    Khi n tiến đến vô cùng, hàm phân bố tích luỹ F(X) sẽ luôn có giá trị tiến đến 1
    Ở đây, với giá trị n càng lớn, số lần thử nhiều với giá trị xác suất luôn nhỏ hơn 1 khiến tổng tích luỹ tiến đến 1
    '''
    sum = 0
    for i in range(1, n+1):
        sum += prob(i, p)
    return sum
def approxEntropy(n, p):
    '''
    Entropy của nguồn tin là có giới hạn vậy nên bằng việc tăng giá trị n tiến đến vô cùng,
    xác suất p hội tụ (gần như không đổi), ta có thể tính gần đúng giá trị entropy
    S = I(X) * p(X)
    Thực nghiệm với p = 1/2:
         approxEntropy(1, 0.5)  = 0.5
         approxEntropy(5, 0.5)  = 1.781
         approxEntropy(10, 0.5) = 1.988
         approxEntropy(50, 0.5) = 1.999
    '''
    apxEntr = 0
    for i in range(1,n+1):
        apxEntr += infoMeasure(i, p)*prob(i, p)
    return apxEntr
if __name__ == "__main__":
    for i in range (1,100):
        print("n: ", i)
        print("infoMeasure: " ,infoMeasure(i, 0.5))
        print("sumProb: " ,sumProb(i,0.5))
        print("approxEntropy: " ,approxEntropy(i, 0.5))
