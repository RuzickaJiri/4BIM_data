
function v = ex4f(t, y, z)
  ylag = z ;
  v = zeros(2,1) ;
  beta = 2.3;
  mu1 = 1;
  m = 1 ;
  b = 0.05 ;
  K = 0.0382 ;
  a = 6570 ;
  r = 6.96 ;
  gamma = 0.001 ;
  Q = 0.0275 ;
  k = 2.8 ;
  S0 = 0.00031*ylag(2)
  v(1) = exp(beta*mu1)*S0 - gamma*y(1) - Q; 
  v(2) = a/(1+K*(y(1))^r)-k*y(2); 
  
  % exp(beta*mu1)*