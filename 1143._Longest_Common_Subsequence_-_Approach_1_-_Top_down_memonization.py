        self.mat=[[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        def lcs(text1,text2):
            # print(self.mat,len(text1),len(text2))
            if self.mat[len(text1)][len(text2)] != -1:
                return self.mat[len(text1)][len(text2)]
            if len(text1) == 0 or len(text2) ==0 :
                self.mat[len(text1)][len(text2)] = 0
                return self.mat[len(text1)][len(text2)]
            else:
                if text1[-1] ==text2[-1]:
                    self.mat[len(text1)][len(text2)] = 1+(lcs(text1[:len(text1)-1], text2[:len(text2)-1]))
                    return self.mat[len(text1)][len(text2)]
                else:
                    self.mat[len(text1)][len(text2)] = max(lcs(text1[:len(text1)-1], text2), lcs(text1,text2[:len(text2)-1]))
                    return self.mat[len(text1)][len(text2)]
        return lcs(text1,text2)
