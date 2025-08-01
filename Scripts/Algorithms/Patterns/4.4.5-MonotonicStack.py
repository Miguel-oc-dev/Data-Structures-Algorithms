class MonotonicStack:
    def nex_element(self, nums):
        n = len(nums)
        # Inicializa el resultado con -1 para todos los elementos
        result = [-1] * n 
        stack=[] # Pila que almacena indices de los elementos

        # Recorremos todos los elementos
        for i in range(n):
            # Mientras la pila no este vacia y el elemento sea mayor
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop() # Sacamos el indice cuyo elemento mayor ya fue encontrado
                result[index] = nums[i] # Guardamos el valor actual como el "siguiente" para ese indice
            stack.append(i)
        return result