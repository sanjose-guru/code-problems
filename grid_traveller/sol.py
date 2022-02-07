class GridTraveller:
    def gt(self, m, n: int) -> int:
        tb = [[0 for i in range(n+1)] for j in range(m+1)]
        tb[1][1] = 1

        for i in range(m+1):
            for j in range(n+1):
                if i+1 <= m:
                    tb[i+1][j] += tb[i][j]
                if j+1 <= n:
                    tb[i][j+1] += tb[i][j]
        # print(tb)
        return(tb[m][n])


if __name__ == '__main__':
    gt = GridTraveller()
    print(gt.gt(3, 3))
