from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# =====================
# 1. 모델 생성
# =====================

model = Sequential()

# =====================
# 2. 입력층 + 은닉층1
# =====================

model.add(
    Dense(
        units=64,
        activation='relu',
        input_shape=(10,)
    )
)

# =====================
# 3. 은닉층2
# =====================

model.add(
    Dense(
        units=32,
        activation='relu'
    )
)

# =====================
# 4. 출력층
# =====================

model.add(
    Dense(
        units=1,
        activation='sigmoid'
    )
)

# =====================
# 5. 학습 설정
# =====================

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# =====================
# 6. 모델 구조 출력
# =====================

model.summary()

# =====================
# 7. 학습
# =====================

model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32
)

# =====================
# 8. 예측
# =====================

result = model.predict(X_test)
