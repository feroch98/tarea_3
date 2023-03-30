A = [1 3 ; 1.5 2 ];
b = [300 ; 350 ];
x = linsolve(A, b);
fprintf('Cantidad de fertilizante tipo A: %.2f \n', x(1));
fprintf('Cantidad de fertilizante tipo B: %.2f \n', x(2));

