class Anagram:
    def __init__(self, word):
        lttrs = [lttr for lttr in word]
        self.lttrs_sorted = sorted(lttrs)
    
    def match(self, the_list):
        matches_list = []
        for item in the_list:
            the_lttrs = [lttr for lttr in item]
            the_lttrs_sorted = sorted(the_lttrs)
            if the_lttrs_sorted == self.lttrs_sorted:
                matches_list.append(item)
        return matches_list