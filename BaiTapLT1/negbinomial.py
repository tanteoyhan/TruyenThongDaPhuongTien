import math

def prob(n, p, k):
    return nCk(n-1, k-1) * (p ** k) * ((1 - p) ** (n - k))

def nCk(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def infoMeasure(n, p, k):
    return -math.log2(prob(n, p, k))

def sumProb(n, p, r):
    '''
    Khi n tiến đến vô cùng, hàm phân bố tích luỹ F(X) sẽ luôn có giá trị tiến đến 1
    Ở đây, với giá trị n càng lớn, số lần thử nhiều với giá trị xác suất luôn nhỏ hơn 1 khiến tổng tích luỹ tiến đến 1
    '''
    sum = 0
    for i in range(r, n+1):
        sum += prob(i, p, r)

    return sum

def approxEntropy(n, p, r):
    '''
    Entropy của nguồn tin là có giới hạn vậy nên bằng việc tăng giá trị n tiến đến vô cùng,
    xác suất p hội tụ (gần như không đổi), ta có thể tính gần đúng giá trị entropy
    S = I(X) * p(X)
    Thực nghiệm với p = 1/2:
        approxEntropy(10, 0.5, 10)  = 0.0097
        approxEntropy(20, 0.5, 10)  = 2.25
        approxEntropy(50, 0.5, 10)  = 4.1507
    '''
    apxEntr = 0
    for i in range(r,n+1):
        apxEntr += infoMeasure(i, p, r)*prob(i, p, r)
    return apxEntr

if __name__ == "__main__":
    p = 0.5
    r = 10
    for i in range (r, 50):
        print("n: ", i, " r: ", r , " p: ", p )
        print("prob: ", prob(i,p,r))
        print("infoMeasure: " ,infoMeasure(i, p, r))
        print("sumProb: " ,sumProb(i, p, r))
        print("approxEntropy: " ,approxEntropy(i, p, r))