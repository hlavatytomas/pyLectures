import numpy as np

# vector     #0 1 2  3 ===> 1D pole
a = np.array([1,2,2,-4])

# print(a)
# print(a.shape)
# print(len(a))
# print(a.ndim)

# print(a[0]) # prvni prvek
# print(a[:]) # vsechny prvky
# print(a[1:]) # od 2. vsechny
# print(a[-1]) # posledni
# print(a[:-1]) # vsechny krome posledniho 
# print(a[:-2]) # vsechny krome poslednich 2
# 
# print(a[::-1]) # otoci pole

# matice ===> 2D pole (tabulka)
A = np.array( 
    [  # 0  1  2  3
        [2, 4, 4, 1], # 0
        [1, 0, 9, 3], # 1 
        [8, 7, 3, 4], # 3
    ]
)   

a = np.array([1,2,2,-4])

# print(a[-1])
# print(a)
# print(A[0,1])
# print(A[:,0])
# print(A[1:,1:].shape)

# print(np.sum(a))
# print(a.sum())
# print(np.max(a))
# print(np.mean(a))
# print(np.median(a))
# print(np.abs(a))



# b = np.linspace(0, 1, 3)   # rovnomerne rozdeleni
# c = np.arange(10,1,-1)          # cela cisla v defaultu
# # print(range(1,10,-1))
# c = np.zeros((4,2))
# print(b)


# print(A.reshape((-1,3)))
# print(a.reshape((2,-1)))
# print(np.max(A,axis=0))
# print(np.argmax(A,axis=0))

# print(np.argmax(a))
# print(np.sort(a))
# print(np.argsort(a))

# mista = np.where(a <= 1)

# print(a[mista])