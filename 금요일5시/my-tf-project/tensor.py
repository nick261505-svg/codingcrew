import tensorflow as tf

키=170
신발=260

#신발=키 * a + b

a=tf.Variable(0.1)
b=tf.Variable(0.2)

def 손실함수():
    예측값=키 * a + b
    return tf.square(260 - 예측값)

# 2. 옵티마이저 (Adam) 선언
# tf.keras. 뒤에 optimizers.Adam() 까지 완성해 보세요.
opt = tf.keras.optimizers.Adam(learning_rate=0.01) 
# 4. 학습 루프 (300번 반복)
for i in range(300):
    
    # --- 이 부분이 핵심입니다 (TF 2.x 방식) ---
    with tf.GradientTape() as tape:
        loss = 손실함수() # 손실값(오차) 계산

    # 'loss'를 'a'와 'b'로 미분하여 기울기(grads) 계산
    grads = tape.gradient(loss, [a, b])

    # 옵티마이저가 기울기를 바탕으로 a와 b를 업데이트
    opt.apply_gradients(zip(grads, [a, b]))
    # -------------------------------------

    # 10번에 한 번씩 현재 값과 오차 출력
    if i % 10 == 0:
        # .numpy()를 붙여야 텐서 안의 실제 값을 볼 수 있습니다.
        print(f"Step {i}: a={a.numpy():.4f}, b={b.numpy():.4f}, Loss={loss.numpy():.4f}")

print("\n--- 학습 완료 ---")
print(f"최종 a: {a.numpy():.4f}")
print(f"최종 b: {b.numpy():.4f}")
print(f"170cm일 때 예측 신발 사이즈: {(키 * a + b).numpy():.1f}")