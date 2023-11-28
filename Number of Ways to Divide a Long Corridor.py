class Solution:
    def numberOfWays(self, corridor: str) -> int:
         x = 1 
         y = 0 
         z = 0 
         for char in corridor:
             if char == 'S':
                 x, y, z = 0, x + z, y
             else:
                 x, y, z = x + z, y, z
         return z % (10**9+7) 
