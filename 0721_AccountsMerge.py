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
        
        for neighbor in adjacent[email]:
            if neighbor not in visited:
                self.DFS(mergedAccount, neighbor, adjacent, visited)

# 3rd solution
# O(nk*log(nk)) time | O(nk) sapce
# where n is the number of accounts and k is the maximum length of an account
class DSU:    
    def __init__(self, sz):
        self.representative = [i for i in range(sz)]
        self.size = [1] * sz
    
    # Finds the representative of group x
    def findRepresentative(self, x):
        if x == self.representative[x]:
            return x
        
        # This is path compression
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]
    
    # Unite the group that contains "a" with the group that contains "b"
    def unionBySize(self, a, b):
        representativeA = self.findRepresentative(a)
        representativeB = self.findRepresentative(b)
        
        # If nodes a and b already belong to the same group, do nothing.
        if representativeA == representativeB:
            return
        
        # Union by size: point the representative of the smaller
        # group to the representative of the larger group.
        if self.size[representativeA] >= self.size[representativeB]:
            self.size[representativeA] += self.size[representativeB]
            self.representative[representativeB] = representativeA
        else:
            self.size[representativeB] += self.size[representativeA]
            self.representative[representativeA] = representativeB

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountListSize = len(accounts)
        dsu = DSU(accountListSize)
        
        # Maps email to their component index
        emailGroup = {}
        
        for i in range(accountListSize):
            accountSize = len(accounts[i])
            
            for j in range(1, accountSize):
                email = accounts[i][j]
                accountName = accounts[i][0]
                
                # If this is the first time seeing this email then
                # assign component group as the account index
                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    # If we have seen this email before then union this
                    # group with the previous group of the email
                    dsu.unionBySize(i, emailGroup[email])
        
        # Store emails corresponding to the component's representative
        components = {}
        for email, group in emailGroup.items():
            groupRep = dsu.findRepresentative(group)
            
            if groupRep not in components:
                components.setdefault(groupRep, [])
            
            components[groupRep].append(email)
        
        # Sort the components and add the account name
        mergedAccounts = []
        for group, component in components.items():
            component.sort() 
            component.insert(0, accounts[group][0])
            mergedAccounts.append(component)
        
        return mergedAccounts