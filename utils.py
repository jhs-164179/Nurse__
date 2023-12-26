# 연령대 변수 생성
def cage(age):
    if age >= 70:
        return 7
    elif age >= 60:
        return 6
    elif age >= 50:
        return 5
    else:
        return 4


# 현재 흡연율 변수 생성
def sm_present(bs1_1, bs3_1):
    result = 0
    if (bs1_1 in [1, 2] and bs3_1 in [1, 2, 3]) or bs1_1 == 3:
        result = 1 if bs1_1 == 2 and bs3_1 in [1, 2] else 0
    return result


# 스트레스 인지율 변수 생성
def mh_stress(bp1):
    if bp1 in [1, 2, 3, 4]:
        return 1 if bp1 in [1, 2] else 0


# 삶의 질 변수 생성
def eq_5d(lq_1eql, lq_2eql, lq_3eql, lq_4eql, lq_5eql):
    if lq_1eql == 1 and lq_2eql == 1 and lq_3eql == 1 and lq_4eql == 1 and lq_5eql == 1:
        return 1

    m2 = m3 = sc2 = sc3 = ua2 = ua3 = pd2 = pd3 = ad2 = ad3 = n3 = 0

    if lq_1eql in [1, 2, 3]:
        m2 = int(lq_1eql == 2)
        m3 = int(lq_1eql == 3)

    if lq_2eql in [1, 2, 3]:
        sc2 = int(lq_2eql == 2)
        sc3 = int(lq_2eql == 3)

    if lq_3eql in [1, 2, 3]:
        ua2 = int(lq_3eql == 2)
        ua3 = int(lq_3eql == 3)

    if lq_4eql in [1, 2, 3]:
        pd2 = int(lq_4eql == 2)
        pd3 = int(lq_4eql == 3)

    if lq_5eql in [1, 2, 3]:
        ad2 = int(lq_5eql == 2)
        ad3 = int(lq_5eql == 3)

    if all(lq in [1, 2, 3] for lq in [lq_1eql, lq_2eql, lq_3eql, lq_4eql, lq_5eql]):
        n3 = int(any(lq == 3 for lq in [lq_1eql, lq_2eql, lq_3eql, lq_4eql, lq_5eql]))

    result = 1 - (0.05 + 0.096 * m2 + 0.418 * m3 + 0.046 * sc2 + 0.136 * sc3 +
                  0.051 * ua2 + 0.208 * ua3 + 0.037 * pd2 + 0.151 * pd3 +
                  0.043 * ad2 + 0.158 * ad3 + 0.05 * n3)

    return result
