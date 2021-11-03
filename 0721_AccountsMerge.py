# 1st solution
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

# 2nd solution
# O(nk*log(nk)) time | O(nk) sapce
# where n is the number of accounts and k is the maximum length of an account
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjacent = {}

        for account in accounts:
            accountSize = len(account)
            
            # Building adjacency list
            # Adding edge between first email to all other emails in the account
            accountFirstEmail = account[1]
            for j in range(2, accountSize):
                accountEmail = account[j]
                
                if accountFirstEmail not in adjacent:
                    adjacent.setdefault(accountFirstEmail, [])

                adjacent[accountFirstEmail].append(accountEmail)
                
                if accountEmail not in adjacent:
                    adjacent.setdefault(accountEmail, [])

                adjacent[accountEmail].append(accountFirstEmail)
        
        # Traverse over all th accounts to store components
        mergedAccounts = []
        for account in accounts:
            accountName = account[0]
            accountFirstEmail = account[1]
            
            # If email is visited, then it's a part of different component
            # Hence perform DFS only if email is not visited yet
            if accountFirstEmail not in visited:
                mergedAccount = []
                # Adding account name at the 0th index
                mergedAccount.append(accountName)
                
                self.DFS(mergedAccount, accountFirstEmail, adjacent, visited)
                mergedAccount[1:] = sorted(mergedAccount[1:])
                mergedAccounts.append(mergedAccount)
            
        return mergedAccounts
    
    def DFS(self, mergedAccount, email, adjacent, visited):
        visited.add(email)
        # Add the email vector that contains the current component's emails
        mergedAccount.append(email)
        
        if email not in adjacent:
            return
        
        for neighbor in adjacent[email]:
            if neighbor not in visited:
                self.DFS(mergedAccount, neighbor, adjacent, visited)