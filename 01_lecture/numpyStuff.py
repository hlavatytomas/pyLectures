import numpy as np

# vector     #0 1 2  3 ===> 1D pole
a = np.array([1,2,2,-4])

print(a)
print(a.shape)
print(a.ndim)

print(a[0]) # prvni prvek
print(a[:]) # vsechny prvky
print(a[1:]) # od 2. vsechny
print(a[-1]) # posledni
print(a[:-1]) # vsechny krome posledniho 
print(a[:-2]) # vsechny krome poslednich 2

print(a[0:])
print(a[:3]) # trochu zvlastni tady !!!
print(a[1:3])

print(a[::-1]) # otoci pole

# matice ===> 2D pole (tabulka)
A = np.array( 
    [  # 0  1  2  3
        [2, 4, 4, 1], # 0
        [1, 0, 9, 3], # 1 
        [8, 7, 3, 4], # 3
    ]
)   
print(A)
print(A.shape)
print(A.ndim)

print(A[0])
print(A[0,0])
print(A[0,:])
print(A[0,1:])
print(A[0,-1])
print(A[0,:-1])
print(A[:,:])
print(A[1:,1:])

print("np fce")

# numpy funkce -- 1D
print(np.sum(a))
print(a.sum())
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.abs(a))
print(np.argmax(a))
print(np.argmin(a))
print(np.argmin(a))
print(np.sort(a))
print(np.sort(a)[::-1])
print(np.argsort(a))
print(np.where(a == 1))
print(np.where(a < 2))
print(a[np.where(a < 2)])
print(a[a < 2])

# numpy funkce -- 2D
print(np.sum(A))
print(np.sum(A, axis = 0))
print(np.sum(A, axis = 1))
print(np.sum(A[:,-1]))
print(np.sum(A[-1,:]))
print(A.reshape((2,6)))
print(A.reshape((2,-1)))
print(A.reshape((-1,2)))
print(A.T)

# jine inicializace
b = np.linspace(0, 1, 10)   # rovnomerne rozdeleni
c = np.arange(10)           # cela cisla v defaultu
d = np.arange(10,1,-1)      # odkud, kam, krok
e = np.arange(0,1,0.2)      # odkud, kam, krok
f = np.zeros((2))
g = np.zeros((2,4))

print(b)
print(c)
print(d)
print(e)
print(f)
print(g)