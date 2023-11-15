# 알고리즘에 많이 쓰이는 Python 라이브러리 및 문법 

### 기본 문법

#### enumerate

- enumerate() 함수는 파이썬에서 반복 객체(리스트, 튜플, 문자열 등)를 파라미터로 받아 각 요소의 인덱스와 값을 포함하는 enumerate 객체로 반환
- 인덱스랑 값을 동시에 필요로하는 알고리즘 문제가 많기 때문에 유용하게 쓰인다
ex) max값을 가진 특정한 사람의 인덱스 값을 필요할 때 


```python 
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# result 

0 apple
1 banana
2 cherry

```

#### zip() 
- 두 개 이상의 반복 가능한 객체를 병렬로 묶어주는 역할
- ex) 점수 배열과 정답 배열을 요소마다 비교해야 될 때 사용

```python 
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

for item1, item2 in zip(list1, list2):
    print(item1, item2)

# result 

1 a
2 b
3 c
4 d

```


#### permutation/combinataion(순열/조합)
- 요소 중에 몇 개를 골라 나열한 모든 경우의 수
- dfs()로 직접 구현하는 거랑 뭐가 다를까? 
    - CPython 인터프리터를 사용하고 있기 때문에 함수들은 c로 작성되어있어 생각보다 빠르다
- 순열 : 순서를 고려한 경우의 수 
```python 
from itertools import permutations

letters = ['a', 'b', 'c']

# 길이가 2인 모든 순열을 생성
perms = permutations(letters, 2)

for perm in perms:
    print(perm)

# result 

('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')


```

- 조합 : 순서를 고려하지 않는 모든 경우의 수 
```python 
from itertools import combinations

letters = ['a', 'b', 'c', 'd']

# 길이가 2인 모든 조합을 생성
combs = combinations(letters, 2)

for comb in combs:
    print(comb)


# result 

('a', 'b')
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
('c', 'd')



```