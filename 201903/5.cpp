#include<bits/stdc++.h>

using namespace std;

#define MAXSIZE 10010
#define MAXNUM 0x7f7f7f7f
int graph[MAXSIZE][MAXSIZE];
bool types[MAXSIZE];
int targets[MAXSIZE];


void output(int n){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            printf("%d ",graph[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


int main(){
    
    
    int n,m,k;scanf("%d%d%d",&n,&m,&k);
    for(int i=1;i<=n;i++) scanf("%d",&types[i]);

    // for(int i=1;i<=n;i++)
    //     memset(graph[i],0x7f,sizeof(int)*(n+1));
    // for(int i=1;i<=n;i++) graph[i][i]=0;
    
    for(int i=1; i<=n; i++)
    {
        for(int j=1; j<=n; j++)
        {
            if(i==j)graph[i][j]=0;
            else graph[i][j]=MAXNUM;
        }
    }

    for(int i=0;i<m;i++){
        int u,v,w;scanf("%d%d%d",&u,&v,&w);
        if(u==v)continue;
        if(w<graph[u][v]){
            graph[u][v]=w;
            graph[v][u]=w;
        }
    }

    // output(n);

    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            for(int k=1;k<=n;k++)
                if(graph[j][i]<MAXNUM&&graph[i][k]<MAXNUM)
                    graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k]);

    // output(n);

    for(int i=1;i<=n;i++){
        memset(targets,0,(n+1)*sizeof(int));
        int top=0;
        for(int j=1;j<=n;j++){
            if(graph[i][j]<MAXNUM&&types[j]){
                targets[top++]=graph[i][j];
            }
        }
        sort(targets,targets+top);
        int count=0;
        for(int i=0;i<k&&i<top;i++){
            count+=targets[i];
        }
        printf("%d\n",count);
    }

}

