from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    merged = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            merged[key] += value
    sorted_merged = dict(sorted(merged.items(), key=lambda item: item[1], reverse=True))
    return sorted_merged

def merge_with_counter(*dicts):
    merged = Counter()
    for d in dicts:
        merged.update(d)
    sorted_merged = dict(merged.most_common())
    return sorted_merged
