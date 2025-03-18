m    = 6.9             ;% kg vann i beholderen              [kg]
cp   = 4184            ;% spesifik varmekapasitet i vann    [J/(kg·K)]
Tomg = 20              ;% temperatur omgivelser             [K]

T_a  = 38              ;% Desired temperature (°C)
T_0  = Tomg            ;% Initial temperature of the water bath (°C)

P0   = 800             ;% maksimalt pådrag fra varmeelement [W]
H    = 4.86            ;% varmeutvekslingskoeffisienten     [W/K]
f    = 0.5             ;% PWM frekvens

Kp   = 100             ;% Proportional gain
Ki   = 0.025           ;% Integral gain
Kd   = 0.05            ;% Derivative gain


a   = -H/(m*cp)        ;
b   =  1/(m*cp)        ;
c   =  H/(m*cp)*Tomg   ;

tau = - 1/a            ;
K   = - b/a            ;
