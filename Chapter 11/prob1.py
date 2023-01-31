class C2dVec:
    def __init__(self, i,j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i,j,k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
V2d = C2dVec(5, 7)
print(V2d)
V3d = C3dVec(7, 5, 3)
print(V3d)
