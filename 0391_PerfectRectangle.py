# 1st solution
# O(n) time | O(n) space
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        s = set() # corners set
        for x1, y1, x2, y2 in rectangles:
            # b-bottom, l-left, t-top, r-right
            bl, br, tl, tr = (x1,y1,'bl'), (x2,y1,'br'), (x1,y2,'tl'), (x2,y2,'tr')
            for corner in (bl,br,tl,tr):
                if corner in s:return False # overlap, but this cannot detect all overlap
                s.add(corner) 
            # if these 4 corners and previously added corners form a line, remove them
            if (x1, y1, 'tl') in s:
                s.remove((x1, y1, 'tl'))
                s.remove(bl) # current bl and preivous tl formed one line on the left, whose share point is (x1,y1), remove these two corners
            elif (x1, y1, 'br') in s:
                s.remove((x1, y1, 'br'))
                s.remove(bl) # current bl and preivous br formed one line on the bottom, whose share point is (x1,y1), remove these two corners
            if (x2, y1, 'tr') in s:
                s.remove((x2, y1, 'tr'))
                s.remove(br)
            elif (x2, y1, 'bl') in s:
                s.remove((x2, y1, 'bl'))
                s.remove(br)
            if (x1, y2, 'bl') in s:
                s.remove((x1, y2, 'bl'))
                s.remove(tl)
            elif (x1, y2, 'tr') in s:
                s.remove((x1, y2, 'tr'))
                s.remove(tl)
            if (x2, y2, 'br') in s:
                s.remove((x2, y2, 'br'))
                s.remove(tr)
            elif (x2, y2, 'tl') in s:
                s.remove((x2, y2, 'tl'))
                s.remove(tr)
        return len(s) == 4