# 1st solution
import itertools
class Solution:
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUFVWXYZ')
    digit = set('0123456789')
    
    def strongPasswordChecker(self, s: str) -> int:
        characters = set(s)
        
        # Check rule (2)
        needs_lowercase = not (characters & self.lowercase)
        needs_uppercase = not (characters & self.uppercase)
        needs_digit = not (characters & self.digit)
        num_required_type_replaces = int(needs_lowercase + needs_uppercase + needs_digit)
        
        # Check rule (1)
        num_required_inserts = max(0, 6 - len(s))
        num_required_deletes = max(0, len(s) - 20)
        
        # Check rule (3)
        # Convert s to a list of repetitions for us to manipulate
        # For s = '11aaabB' we have groups = [2, 3, 1, 1]
        groups = [len(list(grp)) for _, grp in itertools.groupby(s)]
        
        # We apply deletions iteratively and always choose the best one.
        # This should be fine for short passwords :)
        # A delete is better the closer it gets us to removing a group of three.
        # Thus, a group needs to be (a) larger than 3 and (b) minimal wrt modulo 3.
        def apply_best_delete():
            argmin, _ = min(
                enumerate(groups),
                # Ignore groups of length < 3 as long as others are available.
                key=lambda it: it[1] % 3 if it[1] >= 3 else 10 - it[1],
            )
            groups[argmin] -= 1
        
        for _ in range(num_required_deletes):
            apply_best_delete()
        
        # On the finished groups, we need one replace per 3 consecutive letters.
        num_required_group_replaces = sum(
            group // 3
            for group in groups
        )
        
        return (
            # Deletes need to be done anyway
            num_required_deletes
            # Type replaces can be eaten up by inserts or group replaces.
            # Note that because of the interplay of rules (1) and (2), the required number of group replaces
            # can never be greater than the number of type replaces and inserts for candidates of length < 6.
            + max(
                num_required_type_replaces,
                num_required_group_replaces,
                num_required_inserts,
            )
        )

# 2nd solution
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # character check (replace)
        containsUpper, containsLower, containsDigit = 0, 0, 0
        for c in password:
            if not containsUpper and c.isupper():
                containsUpper = 1
            if not containsLower and c.islower():
                containsLower = 1
            if not containsDigit and c.isdigit():
                containsDigit = 1
        
        c_swaps = (3 - (containsUpper + containsLower + containsDigit))
        
        # repeating check (replace)
        i, j, reps = 0, 1, list()
        while i < n:
            while j < n and password[i] == password[j]:
                j += 1
            reps.append(j-i)
            i, j = j, j+1
            
        # length (addition, subtraction)
        if n < 6:
            adds = 6 - n
            return max(adds, c_swaps)
        elif n <= 20:
            r_swaps = sum([elem // 3 for elem in reps])
            return max(c_swaps, r_swaps)
        else:
            subs = n - 20
            r = len(reps)
            for i in range(r):
                if subs >= 1 and reps[i] % 3 == 0:
                    reps[i] -= 1
                    subs -= 1
            for i in range(r):
                if subs >= 2 and reps[i] % 3 == 1 and reps[i] > 3:
                    reps[i] -= 2
                    subs -= 2
            for i in range(r):
                if subs > 0 and reps[i] > 2:
                    removed = min(subs, reps[i] - 2)
                    reps[i] -= removed
                    subs -= removed
                    
            r_swaps = sum([elem // 3 for elem in reps])
            return max(c_swaps, r_swaps) + (n - 20)