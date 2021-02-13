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
	// �θ� ��� ã�� �Լ�
	if (parent[x] == x) return x;
	else return parent[x] = Find(parent[x]);
}

void Union(int x, int y) {
	// x,y�� ���� �θ� ��� �Է�
	x = Find(x);
	y = Find(y);
	// ���� �θ� �ٸ��ٸ� �� ��带 �������ش�
	if (x != y) parent[y] = x;
}

bool Same_Parent(int x, int y) {
	x = Find(x);
	y = Find(y);
	// �θ� ���ٸ� true, �ٸ��� false
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
		// ó���� �� ���� �ڱ� �ڽ��� �θ��� �ʱ�ȭ
		parent[i] = i;
	}
	for (int i = 0; i < edge; i++) {
		// ���� a�� b�� �θ� �ٸ��ٸ�?
		if (Same_Parent(V[i].second.first, V[i].second.second) == false) {
			Union(V[i].second.first, V[i].second.second);
			dap += V[i].first;
		}
	}
	
	cout << dap;
			
}

