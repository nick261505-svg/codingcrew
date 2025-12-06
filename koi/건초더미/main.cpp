#include <iostream>
#include <vector>
#include <ranges>
#include <span>      // C++20: 배열의 부분 범위를 복사 없이 참조

using namespace std;

int solve(span<long long> D, long long P) {
	int count = -1; //파괴한 건초 더미 개수
	
	size_t n = D.size();

	//DP테이블
	//dp[i] : i번째 건초 더미까지 고려했을 때, 파괴하는 건초 더미의 최대 개수
	vector<long long> dp(n + 1, 0);

	
	for (auto defense : D) {
		// 역순으로 업데이트해야 같은 건초를 중복 사용하지 않음
		// 예: dp[2]를 업데이트할 때 이미 업데이트된 dp[1]을 사용하지 않도록
		for (size_t k = n; k >= 1; --k) {
			// 전이 공식:
			// - 이전에 k-1개로 dp[k-1]의 힘을 처리할 수 있었다면
			// - 현재 건초(defense)를 k번째로 추가하면:
			//   * 처음 k-1개가 dp[k-1]의 힘을 감소시킴
			//   * 마지막 건초(defense)에서 멈춤 (defense 이하의 힘이면 멈춤)
			//   * 따라서 총 dp[k-1] + defense의 힘까지 처리 가능
			//
			// 예: dp[1] = 6, defense = 5인 경우
			//     dp[2] = 6 + 5 = 11
			//     (힘 11 → 5로 6 감소 → 6에서 멈춤)
			dp[k] = max(dp[k], dp[k - 1] + defense);
		}
	}

	// target_power를 멈출 수 있는 최소 k 찾기
	// dp[k] >= target_power인 최소 k를 반환
	for (size_t k = 1; k <= n; ++k) {
		if (dp[k] >= P) {
			return static_cast<int>(k);
		}
	}

	// 모든 건초를 사용해도 막을 수 없는 경우
	return -1;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, Q;
	cin >> N >> Q;

	//건초 방어력 입력
	vector<long long> D(N);
	for (long long& val:D) {
		cin >> val;
	}

	//Q개의 쿼리 처리
	for (int i = 0; i < Q; i++) {
		int X; //위치
		long long P;//화살 힘
		cin >> X >> P;

		//벡터 D의 데이터 중 앞에서부터 X개 만큼만 바라보는 가상의 뷰(View)를 생성
		//D.data() : 벡터D의 메모리 시작주소(포인터)
		//static_cast<size_t>(X) : (개수)	X를 size_t 타입으로 변환
		//span의 길이는 음수가 될 수 없으므로 size_t 타입을 요구하는데,
		//X가 int라면 경고를 없애기 위해 명시적으로 형변환을 해준 것
		span<long long> available{D.data(), static_cast<size_t>(X)};
		int result = solve(available, P);
		cout << result << '\n';
	}


	return 0;
}