class Solution:
    # 1st solution
    # O(mn) time | O(mn) space
    # where n is the number of emails, and m is the largest length of emails
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            result = []
            for i in range(len(email)):
                if email[i] == "@":
                    break
                if email[i] == "+":
                    break
                elif email[i] == ".":
                    continue
                else:
                    result.append(email[i])

            for i in reversed(range(len(email))):
                if email[i] == "@":
                    result.append(email[i:])
                    break
            emailSet.add("".join(result))
        return len(emailSet)

    # 2nd solution, use built-in fuctions
    # O(mn) time | O(mn) space
    # where n is the number of emails, and m is the largest length of emails
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in  emails:
            x = email.split("@")
            y = x[0].split("+")
            z = y[0].replace(".", "")
            x = z + "@" + x[1]
            result.add(x)
        return len(result)