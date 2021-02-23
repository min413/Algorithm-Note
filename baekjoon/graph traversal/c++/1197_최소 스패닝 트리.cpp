/*
#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <queue>
#include <algorithm>
#include <stack>
#include <cmath>
#include <functional>
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int vertex, edge, dap;
int parent[10001];
vector<pair<int, pair<int, int> > > V;

int Find(int x) {
	// 부모 노드 찾는 함수
	if (parent[x] == x) return x;
	else return parent[x] = Find(parent[x]);
}

void Union(int x, int y) {
	// x,y에 각각 부모 노드 입력
	x = Find(x);
	y = Find(y);
	// 만약 부모가 다르다면 두 노드를 연결해준다
	if (x != y) parent[y] = x;
}

bool Same_Parent(int x, int y) {
	x = Find(x);
	y = Find(y);
	// 부모 같다면 true, 다르면 false
	if (x == y) return true;
	else return false;
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> vertex >> edge;
	for (int i = 0; i < edge; i++) {
		int a, b, cost;
		cin >> a >> b >> cost;
		V.push_back(make_pair(cost, make_pair(a, b)));

	}
	sort(V.begin(), V.end());

	for (int i = 1; i <= vertex; i++) {
		// 처음에 각 노드는 자기 자신이 부모라고 초기화
		parent[i] = i;
	}
	for (int i = 0; i < edge; i++) {
		// 만약 a와 b의 부모가 다르다면?
		if (Same_Parent(V[i].second.first, V[i].second.second) == false) {
			Union(V[i].second.first, V[i].second.second);
			dap += V[i].first;
		}
	}
	
	cout << dap;
			
}

