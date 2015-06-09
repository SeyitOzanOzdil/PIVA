from scipy import stats
def chi2(dataset, row_c, column_c):

    row_total = []
    for i in range(1, row_c+1):
        tmp = 0
        for j in range(column_c):
            tmp += float(dataset.GetValue(dataset.features[j], i))
        row_total.append(tmp)

    column_total = []
    for i in range(column_c):
        tmp = 0
        for j in range(1, row_c+1):
            tmp += float(dataset.GetValue(dataset.features[i], j))
        column_total.append(tmp)

    total = sum(column_total)
    expected = []
    for k in range(column_c):
        expected.append([])
        for t in range(row_c):
            expected[k].append(0)

    for i in range(column_c):
        for j in range(row_c):
            expected[i][j] = (column_total[i]*row_total[j]/total)

    q = 0
    for j in range(column_c):
        for i in range(1, row_c+1):
            q += (float(dataset.GetValue(dataset.features[j], i))-expected[j][i-1])**2/expected[j][i-1]

    df = (row_c - 1) * (column_c - 1)

    pvalue = 1 - stats.chi2.cdf(q, df)
    return [q, df, pvalue]
