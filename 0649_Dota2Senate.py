class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R_list = []
        D_list = []
        for i, senator in enumerate(senate):
            if senator == "R":
                R_list.append(i)
            elif senator == "D":
                D_list.append(i)
        turn = 0

        while R_list and D_list:
            new_R = []
            new_D = []
            i, j = 0, 0
            while i < len(R_list) or j < len(D_list):
                R = R_list[i] if i < len(R_list) else n
                D = D_list[j] if j < len(D_list) else n
                if R < D:
                    i += 1
                    new_R.append(R)
   
                    if j < len(D_list):
                        j += 1
                    elif len(new_D) > 0:
                        new_D.pop(0)

                else:
                    j += 1
                    new_D.append(D)
                    if i < len(R_list):
                        i += 1
                    elif len(new_R) > 0:
                        new_R.pop(0)


            new_R.extend(R_list[i:])
            new_D.extend(D_list[j:])

            R_list = new_R
            D_list = new_D
            turn += 1
        
        if len(R_list) > 0:
            return "Radiant"
        return "Dire"