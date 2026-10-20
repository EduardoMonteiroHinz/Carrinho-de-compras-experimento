from math import isfinite


class Carrinho:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, nome, preco, quantidade=1):
        if (
            isinstance(preco, bool)
            or not isinstance(preco, (int, float))
            or not isfinite(preco)
            or preco < 0
        ):
            raise ValueError("O preço deve ser um número finito não negativo.")
        if isinstance(quantidade, bool) or not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um inteiro positivo.")

        for item in self._itens:
            if item["nome"] == nome:
                item["quantidade"] += quantidade
                return

        self._itens.append(
            {"nome": nome, "preco": float(preco), "quantidade": quantidade}
        )

    def remover_item(self, nome):
        for index, item in enumerate(self._itens):
            if item["nome"] == nome:
                del self._itens[index]
                return
        raise ValueError(f"Item não encontrado: {nome}")

    def show(self):
        return [item.copy() for item in self._itens]

    def total(self):
        if not self._itens:
            return 0.00

        subtotal = sum(item["preco"] * item["quantidade"] for item in self._itens)
        if subtotal >= 500:
            desconto = 0.15
        elif subtotal >= 200:
            desconto = 0.10
        else:
            desconto = 0

        valor_com_desconto = subtotal * (1 - desconto)
        frete = 0 if valor_com_desconto >= 150 else 20
        return round(valor_com_desconto + frete, 2)