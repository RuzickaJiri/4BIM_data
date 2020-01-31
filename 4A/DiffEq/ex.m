
%% 

sol = dde23('ex1f', [1,0.2], ones(3,1), [0,5]) ;

plot(sol.x, sol.y)
title('Figure1')
xlabel('time t')
ylabel('y(t)')
legend()
  
%% 

sol = dde23('ex2f', [14], [0.5], [0,300]) ;
plot(sol.y, sol.yp)
title('Figure2')
legend()

%% 

sol = dde23('ex2f', [14], [0.5], [0,300]) ;
t = linspace(14,300,1000);
y = deval(sol, t);
ylag = deval(sol,t-14);
plot(y, ylag)
title('Figure2')
legend()

%% 

sol = dde23('ex3f', [1], [80,30], [0,100]) ;
t = linspace(1,100,1000);
x = deval(sol.x, t);
y = deval(sol.y, t);
plot(x, y, t)
title('Figure3')
legend()

%% 
sol = dde23('ex3f', [1], [80,30], [0,100]) ;
t = linspace(1,100,1000);
y = deval(sol, t);
ylag = deval(sol,t-1);
plot(y, ylag)
title('Figure5')
legend()                                            



%% 

% Article simulation

sol = dde23('ex4f', [6], [3.325,10], [0,300]) ;
t = linspace(1,300,1000);
figure()
plot(sol.x, sol.y(1,:), 'LineWidth',4)
ylim([3.3 3.505])
title('Évolution de M(t) en fonction du temps')
xlabel('Temps (jours)')
ylabel('Population des érythrocytes (x10^{11})')

figure()
plot(sol.x, sol.y(2,:), 'LineWidth',4)
xlim([-1 300])
title('Évolution de E(t) en fonction du temps')
xlabel('Temps (jours)')
ylabel('Érythropoïetine (mUml^{−1})')


