# 2-1_DeepRuningSchool
딥러닝수업

# 기말고사 강조 내용

https://eclass.dongyang.ac.kr/local/ubdoc/?id=523168&tp=m&pg=ubfile

9주차 좀 있음

12주차 

13주차 는 안나옴

14주차 TensorFlow 수업시간에 강조 한부분만

오버피팅 방지하는법 3가지 언리스탑 드롭아웃

풀링 입력값을 줄이는거 

패딩 입력값을 올리는거

# 입력층 은닉층 출력층

<img width="676" height="295" alt="스크린샷 2026-04-01 111118" src="https://github.com/user-attachments/assets/42b883ad-7b35-4672-8d83-9d180271ac7d" />
<img width="621" height="450" alt="스크린샷 2026-04-01 114512" src="https://github.com/user-attachments/assets/880b444e-58dd-4c8b-b12b-13ec06852f3b" />

| 함수               | 의미                           |
| ---------------- | ---------------------------- |
| `Sequential()`   | 모델 생성                        |
| `add()`          | 층(Layer) 추가                  |
| `Dense()`        | 완전연결층(Fully Connected Layer) |
| `Conv2D()`       | CNN 합성곱층                     |
| `MaxPooling2D()` | 풀링층                          |
| `Flatten()`      | 2D → 1D 변환                   |
| `SimpleRNN()`    | RNN 층 생성                     |
| `LSTM()`         | LSTM 층 생성                    |
| `compile()`      | 학습 방법 설정                     |
| `fit()`          | 모델 학습                        |
| `predict()`      | 예측 수행                        |
| `summary()`      | 모델 구조 출력                     |

CNN
| 함수               | 역할     |
| ---------------- | ------ |
| `Conv2D()`       | 특징 추출  |
| `MaxPooling2D()` | 크기 축소  |
| `Flatten()`      | 1차원 변환 |
| `Dense()`        | 최종 분류  |

RNN
| 함수            | 역할    |
| ------------- | ----- |
| `SimpleRNN()` | 순환신경망 |
| `Dense()`     | 출력층   |

LSTM
| 함수        | 역할       |
| --------- | -------- |
| `LSTM()`  | 장기 기억 가능 |
| `Dense()` | 출력층      |

3. 옵션(파라미터)
| 옵션                      | 의미           |
| ----------------------- | ------------ |
| `input_shape=(5,1)`     | 길이 5, 특성 1개  |
| `input_shape=(28,28,1)` | 28×28 흑백 이미지 |
| `units=64`              | 뉴런 64개       |

CNN 관련
| 옵션                  | 의미     |
| ------------------- | ------ |
| `filters=32`        | 필터 32개 |
| `kernel_size=(3,3)` | 3×3 필터 |
| `pool_size=(2,2)`   | 2×2 풀링 |

RNN LSTM 관
| 옵션                       | 의미         |
| ------------------------ | ---------- |
| `return_sequences=True`  | 모든 시점 출력   |
| `return_sequences=False` | 마지막 시점만 출력 |

활성화 함수
| 옵션                     | 의미      |
| ---------------------- | ------- |
| `activation='relu'`    | 음수 제거   |
| `activation='sigmoid'` | 0~1 확률  |
| `activation='softmax'` | 다중 분류   |
| `activation='tanh'`    | -1~1 출력 |

| 옵션                                | 의미       |
| --------------------------------- | -------- |
| `optimizer='adam'`                | 최적화 알고리즘 |
| `loss='mse'`                      | 회귀 오차 함수 |
| `loss='binary_crossentropy'`      | 이진 분류    |
| `loss='categorical_crossentropy'` | 다중 분류    |
| `metrics=['accuracy']`            | 정확도 표시   |

# 순서

| 단계              | 코드                                       | 역할                   |
| --------------- | ---------------------------------------- | -------------------- |
| **1. 모델 생성**    | `Sequential()`                           | 신경망 모델 생성            |
| **2. 레이어(함수)**  | `Flatten()`                              | 입력 데이터를 1차원으로 변환     |
|                 | `Dense()`                                | 완전연결층 생성             |
|                 | `Dropout()`                              | 일부 뉴런 비활성화 (오버피팅 방지) |
| **3. 파라미터(옵션)** | `input_shape=(28,28)`                    | 입력 데이터 형태 지정         |
|                 | `128`                                    | 뉴런 128개              |
|                 | `0.2`                                    | 20% Dropout          |
|                 | `10`                                     | 출력 노드 10개            |
| **4. 활성화 함수**   | `relu`                                   | 음수 제거, 은닉층에서 사용      |
|                 | `softmax`                                | 다중 분류 확률 계산          |
| **5. 학습 설정**    | `optimizer='adam'`                       | 최적화 알고리즘             |
|                 | `loss='sparse_categorical_crossentropy'` | 손실 함수                |
|                 | `metrics=['accuracy']`                   | 정확도 측정               |
| **6. 학습**       | `fit()`                                  | 모델 학습                |
| **7. 평가**       | `evaluate()`                             | 테스트 데이터 평가           |
| **8. 예측**       | `predict()`                              | 새로운 데이터 예측           |




