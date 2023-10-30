# [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/)

Você recebe uma matriz de inteiros 2D chamada "intervals", onde intervals[i] = [lefti, righti] representa o intervalo inclusivo [lefti, righti].

Você precisa dividir os intervalos em um ou mais grupos de forma que cada intervalo esteja exatamente em um grupo e nenhum intervalo em um mesmo grupo se sobreponha a outro.

Retorne o número mínimo de grupos necessários.

Dois intervalos se sobrepõem se houver pelo menos um número em comum entre eles. Por exemplo, os intervalos [1, 5] e [5, 8] se sobrepõem.

> Exemplo:
> 
> Entrada: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
> 
> Saída: 3