def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequencies = dict()
    for num in nums:
        if num not in frequencies:
            frequencies[num] = 0
        frequencies[num]+=1
    items = list(frequencies.items())
    items.sort(key=lambda item: item[1], reverse=True)
    return [item[0] for item in items[0:k]]

result = topKFrequent(nums = [1], k = 1)
print(result)