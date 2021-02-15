#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
using namespace std;
int vertex, edge, dap = 0;
int parent[1001];
vector<pair<int, pair<int, pair<int,int> > > > V;
vector<int> imsi;
int Find(int x) {
	if (parent[x] == x) return x;
	else return parent[x] = Find(parent[x]);
}

void Union(int x, int y) {
	x = Find(x);
	y = Find(y);
	if (x != y) parent[y] = x;
}

bool Same_Parent(int x, int y) {
	x = Find(x);
	y = Find(y);
	if (x == y) return true;
	else return false;
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> vertex >> edge;
	for (int i = 0; i < edge; i++) {
		int a, b, c, cost = 0;
		cin >> a >> b >> c;
		
		V.push_back(make_pair(cost, make_pair(a, make_pair(b,c))));
	}
	
	sort(V.begin(), V.end());

	for (int i = 1; i <= vertex; i++) {
		parent[i] = i;
	}
	
	for (int i = 0; i < edge; i++) {
		if (Same_Parent(V[i].second.first, V[i].second.second) == false) {
			Union(V[i].second.first, V[i].second.second);
			
			imsi.push_back(V[i].first);
		}
	}
	
	for(int i = 0; i < imsi.size() - 1; i++){
		dap = dap + imsi[i];
	}
	cout << dap; 
	
}



