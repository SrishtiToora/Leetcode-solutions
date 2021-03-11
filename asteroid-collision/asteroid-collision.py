class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for ast in asteroids:
            if not res:
                res.append(ast)
            else:
                if ast > 0:
                    res.append(ast)
                else: # ast < 0
                    if res[-1] < 0:
                        res.append(ast)
                    else: #res[-1] > 0:
                        while res and res[-1] > 0 and res[-1] < abs(ast):
                            res.pop()
                        if res and res[-1] > 0 and res[-1] == abs(ast):
                            res.pop()
                        elif res and res[-1] < 0 or not res:
                            res.append(ast)
        return res