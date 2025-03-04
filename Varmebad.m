clc; clear; close all;

% Define system parameters
H = 10;       % Heat loss coefficient (W/°C)
m = 1;        % Mass of water (kg)
cp = 4186;    % Specific heat capacity of water (J/kg°C)
T_omg = 25;   % Ambient temperature (°C)
P0 = 500;     % Maximum heater power (W)
T_a = 38;     % Desired temperature (°C)
T_0 = 23;     % Initial temperature of the water bath (°C)

% Compute system coefficients
a = -H / (m * cp);
b = P0 / (m * cp);
c = (H / (m * cp)) * T_omg;

% Define system state-space representation
A = a;
B = b;
C = 1;
D = 0;

sys = ss(A, B, C, D);

% PID Controller Design (Initial values, can be tuned)
Kp = 2;   % Proportional gain
Ki = 0.1; % Integral gain
Kd = 0.05; % Derivative gain
pid_controller = pid(Kp, Ki, Kd);

% Closed-loop system with feedback
closed_loop_sys = feedback(pid_controller * sys, 1);

% Time vector for simulation
t = 0:1:600; % Simulate for 10 minutes (600 seconds)

% Define initial condition
x0 = T_0 - T_a; % Initial deviation from setpoint

% Simulate step response with initial condition
[y, t, x] = initial(closed_loop_sys, x0, t);

% Convert output temperature response back from deviation to absolute values
y_actual = y + T_a;

% Plot response
figure;
plot(t, y_actual, 'b', 'LineWidth', 2);
hold on;
yline(T_a, 'r--', 'Setpoint', 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('Temperature (°C)');
title('PID-Controlled Water Bath Temperature (PWM Duty Cycle)');
grid on;
legend('Temperature Response', 'Setpoint');
