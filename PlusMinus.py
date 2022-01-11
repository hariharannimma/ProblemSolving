arr = [1, 1, 0, -1, -1]
postive_count = 0
negitive_count = 0
zeros_count = 0
for i in arr:
    if i > 0:
        postive_count += 1
    if i < 0:
        negitive_count += 1
    if i == 0:
        zeros_count += 1

postive_ratio = postive_count/len(arr)
negitive_ratio = negitive_count/len(arr)
zeros_ratio = zeros_count/len(arr)
print("{:.6f}".format(postive_ratio), "{:.6f}".format(
    negitive_ratio), "{:.6f}".format(zeros_ratio))
