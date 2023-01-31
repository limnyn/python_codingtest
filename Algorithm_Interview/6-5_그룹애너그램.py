# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

import collections
texts = ["eat", "tea", 'tan', "ate", "nat", "bat"]
result = collections.defaultdict(list)
for text in texts:
    result[''.join((sorted(text)))].append(text)

print(list(result.values()))