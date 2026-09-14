class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1_done, l2_done = False, False
        l1, l2 = 0, 0
        turn = 0
        final = ""
        while l1_done == False or l2_done == False:
            if turn % 2 == 0 and l1_done == False:
                final += word1[l1]
                l1 += 1
                turn +=1
                if l1 == len(word1):
                    l1_done = True
            elif turn % 2 == 1 and l2_done == False:
                final += word2[l2]
                l2 += 1
                turn +=1
                if l2 == len(word2):
                    l2_done = True
            else:
                if turn % 2 == 1:
                    final += word1[l1]
                    l1 += 1
                    if l1 == len(word1):
                        return final
                else:
                    final += word2[l2]
                    l2 += 1
                    if l2 == len(word2):
                        return final
        return final
        