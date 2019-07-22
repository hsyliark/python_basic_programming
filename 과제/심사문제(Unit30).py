## Unit 30
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수,
# 평균 점수가 출력되게 만드세요. 평균 점수는 실수로 출력되어야 합니다.

korean, english, mathematics, science = map(int, input().split())
set_score = dict(zip(['korean','english','mathematics','science'],
                     [korean,english,mathematics,science]))
import numpy as np
def get_min_max_score(*score):
    minScore = min(score)
    maxScore = max(score)
    return minScore, maxScore
def get_average(korean, english, mathematics, science):
    score = list(korean, english, mathematics, science)
    avgScore = np.mean(score)
    return avgScore

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))




