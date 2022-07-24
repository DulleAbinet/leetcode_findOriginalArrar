class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ele = []
        if len(changed)%2 != 0:
            return ele
        changed.sort()
        cont = Counter(changed)
        for pc in changed:
            if pc in cont and cont[pc]>=1 :
                cont[pc] -=1
                if (pc*2) in cont and cont[pc*2] >=1:
                    ele.append(pc)
                    cont[pc*2] -=1
        
        if len(ele)==len(changed)//2:
            return ele
        else:
            return []
