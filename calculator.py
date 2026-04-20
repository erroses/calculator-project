def sum(a, b):
    """두 수의 합을 반환합니다."""
    return a + b

def sub(a, b):
    """a에서 b를 뺀 값을 반환합니다."""
    return a - b

def mul(a, b):
    """두 수의 곱을 반환합니다."""
    return a * b

def div(a, b):
    """a를 b로 나눈 값을 반환합니다.
    b가 0이면 ValueError를 발생시킵니다.
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b