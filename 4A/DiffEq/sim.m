
function v = simu(t, y, z)
  ylag = z ;
  v = zeros(2,1) ;
  beta = 1;
  mu1 = 6;
  m = 1 ;
  b = 0.0031 ;
  K = 0.0382 ;
  a = 6570 ;
  r = 6.96 ;
  gamma = 0.001 ;
  Q = 0.0275 ;
  k = 2.8 ;
  v(1) = exp(beta*mu1)*(m*ylag + b) - gamma*y(1) - Q; 
  v(2) = a/(1+K*y(1)^r)-k*y(2); 