# [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/)

O TinyURL é um serviço de encurtamento de URL onde você insere uma URL, como https://leetcode.com/problems/design-tinyurl, e ele retorna uma URL curta, como http://tinyurl.com/4e9iAk. Projete uma classe para codificar uma URL e decodificar uma URL curta.

Não há restrições sobre como seu algoritmo de codificação/decodificação deve funcionar. Você só precisa garantir que uma URL possa ser codificada em uma URL curta e que a URL curta possa ser decodificada para a URL original.

Implemente a classe Solution:

    Solution() Inicializa o objeto do sistema.
    String encode(String longUrl) Retorna uma URL curta para a longUrl fornecida.
    String decode(String shortUrl) Retorna a URL longa original para a shortUrl fornecida. É garantido que a shortUrl fornecida foi codificada pelo mesmo objeto.

> Exemplo:
> 
> Entrada: url = "https://leetcode.com/problems/design-tinyurl"
> 
> Saída: "https://leetcode.com/problems/design-tinyurl"
