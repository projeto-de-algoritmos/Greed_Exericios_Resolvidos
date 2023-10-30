import heapq
import collections

class Codec:
    def __init__(self):
        self.url_mapping = {}
        self.heap = []
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # Verifica se ja exeiste mapeamento
        if longUrl in self.url_mapping:
            return self.url_mapping[longUrl]
        
        # Cria a arvore
        def build_huffman_tree(counts):
            heap = [[weight, [char, ""]] for char, weight in counts.items()]
            heapq.heapify(heap)
            while len(heap) > 1:
                lo = heapq.heappop(heap)
                hi = heapq.heappop(heap)
                for pair in lo[1:]:
                    pair[1] = '0' + pair[1]
                for pair in hi[1:]:
                    pair[1] = '1' + pair[1]
                heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
            return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

        counts = collections.Counter(longUrl) # Conta a frequencia de cada caracter
        huffman_tree = build_huffman_tree(counts)
        huffman_codes = {char: code for char, code in huffman_tree} # Cria código de huffman para cada caractere a partir da arvore de huffman
        encoded_url = ''.join([huffman_codes[char] for char in longUrl]) # Cria código de huffman para a url de acordo com o mapeamento de caracteres
        self.url_mapping[longUrl] = encoded_url
        return encoded_url


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for longUrl, encoded_url in self.url_mapping.items():
            if encoded_url == shortUrl:
                return longUrl


url = "https://leetcode.com/problems/design-tinyurl"
solution = Codec()
encoded_url = solution.encode(url)
decoded_url = solution.decode(encoded_url)
print(decoded_url)
