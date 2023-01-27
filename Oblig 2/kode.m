
function A=kode(n)
    A = round(rand(n,n));
        for k=1:(n-1)
            A(k,k) = 0;
                if (A(:,k) == 0)
                       A(n,k) = 1;
                end
            s = sum(A(:,k));
            A(:,k) = (1/s) * A(:,k);
        end
    A(n,n) = 0;
    if (A(:,n) == 0)
        A(1,n) = 1;
    end
    s = sum(A(:,n));
    A(:,n) = (1/s) * A(:,n);
  

kode(5)
