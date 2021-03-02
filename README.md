Jacobi method using Python.

From [Wikipedia](https://en.wikipedia.org/wiki/Jacobi_method):
    
    In numerical linear algebra, the Jacobi method is an iterative algorithm for determining the solutions of a strictly diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges.

[Pseudocode](https://en.wikipedia.org/wiki/Jacobi_method#Algorithm):

```
    k=0
    while convergence not reached do
        for i := 1 step until n do
            {\displaystyle \sigma =0}\sigma =0
            for j := 1 step until n do
                if j ≠ i then
                    {\displaystyle \sigma =\sigma +a_{ij}x_{j}^{(k)}}{\displaystyle \sigma =\sigma +a_{ij}x_{j}^{(k)}}
                end
            end
            {\displaystyle x_{i}^{(k+1)}={{\frac {1}{a_{ii}}}\left({b_{i}-\sigma }\right)}}{\displaystyle x_{i}^{(k+1)}={{\frac {1}{a_{ii}}}\left({b_{i}-\sigma }\right)}}
        end
        {\displaystyle k=k+1}k=k+1
    end
```
