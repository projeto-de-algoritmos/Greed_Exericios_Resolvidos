# Passos:
# Fazer interval scheduling -> retorna a quantidade maxima de intervalos compativeis (numero)
# Subtrai a quantidade de intervalos compativeis do tamnho total da lista de intervalos -> retorna a quantidade
# minima a ser retirada da lista. 

class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:

        # Interval scheduling
        # Ordena os intervalos do menor tempo de termino para o maior.
        intervals.sort(key=lambda x: x[1])

        # Seleciona o primeiro intervalo
        end_time = intervals[0][1]
        non_overlapping_count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time: # Comparação para saber se os intervalos são compativeis. 
                # Tempo de inicio do intervalo atual tem que ser maior que o tempo de termino do último intervalo.
                non_overlapping_count += 1 # Para cada intervalo compativel adiciona.
                end_time = intervals[i][1] # Atualiza o tempo de termino com o valor do intervalo atual.

        # Subtrai a quantidade de intervalos compativeis do tamnho total da lista de intervalos
        return len(intervals) - non_overlapping_count
    
intervals = [[1,2],[2,3]]
solution = Solution()
result = solution.eraseOverlapIntervals(intervals)
print(result)