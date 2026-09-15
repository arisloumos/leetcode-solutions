class Solution(object):
    def compress(self, chars):
        write = 0
        for i in range(len(chars)):
            if i == 0:
                current_group = chars[i]
                count = 1
            elif chars[i] == current_group:
                count += 1
            else:
                chars[write] = current_group
                write += 1
                if count > 1:
                    for j in range(len(str(count)), 0, -1):
                        chars[write] = str(count // 10**(j - 1))
                        count -= (count // 10**(j - 1)) * 10**(j - 1)
                        write += 1
                current_group = chars[i]
                count = 1

            if i == len(chars) - 1:
                chars[write] = current_group
                write += 1
                if count > 1:
                    for j in range(len(str(count)), 0, -1):
                        chars[write] = str(count // 10**(j - 1))
                        count -= (count // 10**(j - 1)) * 10**(j - 1)
                        write += 1

        return write