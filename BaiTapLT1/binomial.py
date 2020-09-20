import math

def prob(n, p, N):
    return nCk(N, n) * (p ** n) * (1 - p) ** (N - n)

def nCk(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))

def sumProb(n, p, N):
    '''
    Khi n tiến đến vô cùng, hàm phân bố tích luỹ F(X) sẽ luôn có giá trị tiến đến 1
    Ở đây, với giá trị n càng lớn, số lần thử nhiều với giá trị xác suất luôn nhỏ hơn 1 khiến tổng tích luỹ tiến đến 1
    '''
    sum = 0
    for i in range(1, n+1):
        sum += prob(i, p, N)

    return sum

def approxEntropy(n, p, N):
    '''
    Entropy của nguồn tin là có giới hạn vậy nên bằng việc tăng giá trị n tiến đến vô cùng,
    xác suất p hội tụ (gần như không đổi), ta có thể tính gần đúng giá trị entropy
    S = I(X) * p(X)
    Thực nghiệm với p = 1/2:
         approxEntropy(5, 0.5)  = 0.00255
         approxEntropy(10, 0.5) = 1.8245
         approxEntropy(20, 0.5) = 3.2077
    '''
    apxEntr = 0
    for i in range(1,n+1):
        apxEntr += infoMeasure(i, p, N)*prob(i, p, N)
    return apxEntr

if __name__ == "__main__":
    p = 0.5
    for i in range (20,21):
        for j in range (1, i + 1):
            print("n: ", j, " N: ", i , " p: ", p)
            print("infoMeasure: " ,infoMeasure(j, p, i))
            print("sumProb: " ,sumProb(j, p, i))
            print("approxEntropy: " ,approxEntropy(j, p, i))