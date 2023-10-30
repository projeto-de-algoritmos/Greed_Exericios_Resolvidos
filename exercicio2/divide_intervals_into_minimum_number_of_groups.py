# Passos:
# Fazer interval partitioning -> retorna a quantidade minima de grupos.


class Solution:
    def minGroups(self, intervals: [[int]]) -> int:

        # Separa os tempos de inicio e termino em listas diferentes e as ordena em ordem crescente.
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])

        start_ptr, end_ptr = 0, 0
        rooms_needed = 0
        current_rooms = 0

        while start_ptr < len(intervals):
            if start_times[start_ptr] <= end_times[end_ptr]: # Compara se o tempo de inicio é menor que o tempo de fim
                # Se for menor, não é possível colocar no mesmo grupo, então cria mais um grupo
                current_rooms += 1
                start_ptr += 1
            
            else: # Se o tempo de inicio é depois do tempo de fim, então pode tirar um sala.
                current_rooms -= 1
                end_ptr += 1

            rooms_needed = max(rooms_needed, current_rooms)

        return rooms_needed

intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
solution = Solution()
result = solution.minGroups(intervals)
print(result)