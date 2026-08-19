class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogCol = image[sr][sc]
        def change(sr,sc,ogCol):
            if sr < 0 or sc < 0 or sr > (len(image)-1) or sc > (len(image[0])-1) or image[sr][sc] != ogCol:
                return None
            image[sr][sc] = color
            #up
            change(sr-1,sc,ogCol)
            #down
            change(sr+1,sc,ogCol)
            #left
            change(sr,sc-1,ogCol)
            #right 
            change(sr,sc+1,ogCol)
        # leads to infinite loop if color is same as og 
        if ogCol == color:
            return image

        change(sr,sc,ogCol)
        return image
