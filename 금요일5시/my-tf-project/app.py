import pandas as pd
import numpy as np
import tensorflow as tf

# 데이터 로드 및 전처리
data = pd.read_csv('gpascore.csv')
data = data.dropna()

# 레이블(목표값) 추출
y_train = data["admit"].values

# 특성(입력값) 추출 - 더 효율적인 방법
x_train = data[["gre", "gpa", "rank"]].values  # 이 방법이 더 빠름!
# 또는 기존 방식:
# x_train = []
# for i, rows in data.iterrows():
#     x_train.append([rows["gre"], rows["gpa"], rows["rank"]])
# x_train = np.array(x_train)

print(f"훈련 데이터 shape: {x_train.shape}")
print(f"레이블 shape: {y_train.shape}")

# 모델 생성
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh', input_shape=(3,)),  # input_shape 명시 권장
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

# 모델 컴파일
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 모델 학습
history = model.fit(
    x_train, 
    y_train, 
    epochs=1000, 
    batch_size=32,
    validation_split=0.2,  # 검증 데이터 20% 분리 (선택사항)
    verbose=0  # 학습 과정 출력 간소화
)

print(f"\n최종 정확도: {history.history['accuracy'][-1]:.4f}")

# 예측 - ✅ NumPy 배열로 변환!
test_data = np.array([[750, 3.70, 3], [400, 2.2, 1]])
predictions = model.predict(test_data)

print("\n예측 결과:")
print(f"학생 1 (GRE:750, GPA:3.70, Rank:3) - 합격 확률: {predictions[0][0]:.2%}")
print(f"학생 2 (GRE:400, GPA:2.2, Rank:1) - 합격 확률: {predictions[1][0]:.2%}")