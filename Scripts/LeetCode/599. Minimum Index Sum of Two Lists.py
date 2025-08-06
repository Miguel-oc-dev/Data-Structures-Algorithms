"""
599. Minimum Index Sum of Two Lists

Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.
A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order.

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Guardamos la posicion de cada palabraa de lis1 en un diccionario
        index_map = {word: i for i, word in enumerate(list1) }
        min_sum = float('inf')
        res = [] # Lista de palabras con la minima suma

        # Recorre list2 y busca coincidencias con list1
        for j, word in enumerate(list2):
            if word in index_map:
                index = j + index_map[word] # Suma de indices

                if index < min_sum:
                    # Nuevo valor minimo, reiniciamos la lista de resultados
                    min_sum = index
                    res = [word]
                elif index == min_sum:
                    # Empate en la suma minima, se agrega a la lista
                    res.append(word)
        return res