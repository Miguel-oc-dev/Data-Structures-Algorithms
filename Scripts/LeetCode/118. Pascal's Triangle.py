class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [] # Lista final que contendra todas las filas del triangulo 
        previous = [] # Lista temporal que almacena la fila anterior

        for _ in range(numRows):
            ps = len(previous) # Tamaño de la fila anteror
            current = [] # Nueva fila

            # Construimos la fila actual elemento por elemento
            for i in range(ps + 1): # Una fila siempre tiene una longitud más que la anterior
                if i == 0 or i == ps:
                    current.append(1) # Los extremos de cada fila, siempre son 1
                else:
                    # Cada elemento interno es la suma de los dos superiores
                    current.append(previous[i-1] + previous[i])
            result.append(current)
            previous = current # La fila actual se convierte en la anterior
        return result