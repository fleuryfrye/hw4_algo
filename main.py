def main():
    print("hello world")


def div_and_conq(n, k):
    if(k == 0):
        return 1
    if(n == k):
        return 1

    if(0 < k < n):
        return (div_and_conq(n-1, k) + div_and_conq(n-1, k-1))


def bottom_up(n, k):
    storage = [1]  ##base case
    if (k == 0):
        return 1
    if (n == k):
        return 1

    result = 0

    for i in range(n):
        if (i + 1 == 1):  ##base case
            result = storage[i - 1]
        else:
            result = (i + 1) * storage[i - 1]
            storage.append(result)

    combination = result / (storage[k - 1] * storage[n - k - 1])
    return combination


def memoization_work(n, k, storage):
    if (n == 0 or n == 1):
        return 1

    result = n * memoization_work(n-1, k, storage)
    storage.append(result)
    return storage[n-1]

def memoization(n, k):

    storage = [1] ##base case is 0! = 1
    memoization_work(n, k, storage)
    return (storage[n-1] / (storage[k-1] * storage[n-k-1]))

if __name__ == "__main__":
    print(div_and_conq(5, 2))
    print(bottom_up(5, 2))
    print(memoization(5, 2))

