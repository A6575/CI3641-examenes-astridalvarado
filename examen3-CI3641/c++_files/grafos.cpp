#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include<map>
#include<algorithm>

using namespace std;

struct Grafo{
    map<int, vector<int> > lista_adyacencia;
};

class Busqueda{
    public:
        virtual int buscar(int H, int D, const Grafo &G) = 0;
};

class DFS : public Busqueda {
public:
    int buscar(int H, int D, const Grafo &graph) override{
        stack<int> stack;
        vector<bool> visitado(graph.lista_adyacencia.size(), false);
        vector<int> camino;
        stack.push(H);
        while (!stack.empty()) {
            int nodo = stack.top();
            stack.pop();
            if (nodo == D) {
                return camino.size(); // Cantidad de nodos explorados
            }
            if (!visitado[nodo]) {
                visitado[nodo] = true;
                camino.push_back(nodo);
                for (auto vecino : graph.lista_adyacencia.at(nodo)) {
                    if (!visitado[vecino]) {
                        stack.push(vecino);
                    }
                }
            }
        }
        return -1; // Nodo H no alcanzable desde D
    }
};

class BFS : public Busqueda {
public:
    int buscar(int H, int D, const Grafo& graph) override{ 
        queue<int> cola;
        vector<bool> visitado(graph.lista_adyacencia.size(), false);
        vector<int> camino;
        cola.push(H);
        while (!cola.empty()) {
            int nodo = cola.front();
            cola.pop();
            if (nodo == D) {
                return camino.size(); // Cantidad de nodos explorados
            }
            if (!visitado[nodo]) {
                visitado[nodo] = true;
                camino.push_back(nodo);
                for (auto vecino : graph.lista_adyacencia.at(nodo)) {
                    if (!visitado[vecino]) {
                        cola.push(vecino);
                    }
                }
            }
        }
        return -1; // Nodo H no alcanzable desde D
    }
}; 

int main(){
    Grafo grafoEjemplo;
    grafoEjemplo.lista_adyacencia = {{1, {2, 3}},{2, {4,5}},{3, {6}},{6, {7}},{4,{}},{5,{}},{7,{}}};
    DFS dfs;
    cout << "Cantidad de nodos visitados en DFS:\n" << dfs.buscar(1,7,grafoEjemplo)<<endl;
    BFS bfs;
    cout << "Cantidad de nodos visitados en BFS:\n" << bfs.buscar(1,7,grafoEjemplo)<<endl;
    return 0;
}