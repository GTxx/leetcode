class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        ac = C - A
        eg = G - E
        width_overlap = ac + eg - (max(C, G) - min(A, E))
        bd = D - B
        fh = H - F
        height_overlap = bd + fh - (max(D, H) - min(B, F))
        overlap_area = width_overlap * height_overlap if width_overlap > 0 and height_overlap > 0 else 0
        return ac * bd + eg * fh - overlap_area


if __name__ == "__main__":
    s = Solution()
    # print(s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2))
    print(s.computeArea(-2,-2,2,2,-4,-2,-2,2))
