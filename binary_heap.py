class MinHeap:
    def __init__(self, initial_data=None):
        self.data = list(initial_data) if initial_data else []


    def _parent_index(self, i):
        return (i - 1) // 2


    def _left_index(self, i):
        return 2 * i + 1


    def _right_index(self, i):
        return 2 * i + 2


    def _sift_up(self, index):
        while index > 0:
            p_idx = self._parent_index(index)
            if self.data[index] < self.data[p_idx]:

                self.data[index], self.data[p_idx] = (
                    self.data[p_idx],
                    self.data[index],
                )

                index = p_idx
            else:
                break


    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)


    def display_relations(self):
        n = len(self.data)
        for i in range(n):
            val = self.data[i]

            # родитель
            if i > 0:
                p_idx = self._parent_index(i)
                parent_val = self.data[p_idx]
            else:
                parent_val = "Нет"

            # левый потомок
            l_idx = self._left_index(i)
            left_val = self.data[l_idx] if l_idx < n else "Нет"

            # правый потомок
            r_idx = self._right_index(i)
            right_val = self.data[r_idx] if r_idx < n else "Нет"

            print(f"Элемент [{i}]: значение = {val:<4} | "
                  f"Родитель = {str(parent_val):<4} | "
                  f"Левый потомок = {str(left_val):<4} | "
                  f"Правый потомок = {str(right_val):<4}")