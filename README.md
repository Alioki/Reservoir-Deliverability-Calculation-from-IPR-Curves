# Project Title

Reservoir Deliverability Calculation from IPR Curves


## Description


Reservoir deliverability is defined as the oil or gas production rate achievable from a reservoir at a given bottom-hole pressure. It is a major factor affecting well deliverability and determines the types of completion and artificial lift methods to be used. A thorough knowledge of reservoir productivity is essential for production engineers, as it aids in optimizing extraction strategies and ensuring the efficiency of production operations.

In this project, the **generalized Vogel IPR model** is applied to describe well inflow from multilayer reservoirs where reservoir pressures are above oil bubble-point pressures, while wellbore pressures remain below these bubble-point pressures. By using this approach, the project examines **IPR curves** under **Steady-state**, **Pseudo–steady-state**, and **Transient** flow conditions, considering scenarios where the reservoir either reaches bubble point pressure or remains above it by the end of the operation. Given the complexity of replicating these conditions in real-world settings, the project is primarily educational and aimed at deepening understanding of reservoir inflow behavior in various conditions. Additionally, future **IPR** values are calculated to predict potential production performance over time.


## Required

To run this code, the **NumPy** and **Matplotlib** libraries must be installed on your system. These libraries are used for numerical computations and plotting IPR curves, respectively. You can install them using the following command:

*install matplotlib*
```
pip install matplotlib
```
*install numpy*
```
pip install numpy
```




This can be added to the documentation or description to clearly indicate the requirements.

## Methodology


**single-phase**

In scenarios where the **reservoir pressure is maintained above the bubble-point pressure**, the productivity index $( J^* )$ can be calculated using various flow regimes to assess well performance. This approach is essential for evaluating well deliverability and understanding flow behavior under different operational conditions when the reservoir pressure is higher than the pressure at which gas starts to separate from oil.

1. **Transient Flow**: For a vertical well with radial transient flow, the productivity index is defined as:

   $$J^* = \frac{q}{(p_i - p_{wf})} = \frac{kh}{162.6 B_o \mu_o} \left( \log t + \log \frac{k}{\phi \mu_o c_t r_w^2} - 3.23 + 0.87S \right)$$

   where $\( q \)$ represents the flow rate, $\( p_i \)$ is the initial reservoir pressure, $\( p_{wf} \)$ is the flowing bottom-hole pressure, $\( k \)$ is the permeability, $\( h \)$ is the thickness, $\( B_o \)$ is the oil formation volume factor, $\( \mu_o \)$ is the oil viscosity, $\( \phi \)$ is the porosity, $\( c_t \)$ is the total compressibility, $\( r_w \)$ is the well radius, and $\( S \)$ is the skin factor. This equation considers both formation and fluid properties to determine flow under transient conditions, capturing the impact of time on productivity.

2. **Steady-State Flow**: In radial steady-state flow around a vertical well, the productivity index can be expressed as:

   
   $$J^* = \frac{q}{(p_e - p_{wf})} = \frac{kh}{141.2 B_o \mu_o} \left( \ln \frac{r_e}{r_w} + S \right)$$

   Here, $\( p_e \)$ is the external boundary pressure, and $\( r_e \)$ is the drainage radius. This steady-state model is useful for conditions where pressure gradients stabilize over time, reflecting long-term reservoir deliverability.

3. **Pseudo–Steady-State Flow**: For pseudo–steady-state flow in a vertical well, the productivity index is determined by:

   
   $$J^* = \frac{q}{(\overline{p} - p_{wf})} = \frac{kh}{141.2 B_o \mu_o} \left( \frac{1}{2} \ln \frac{4A}{\gamma C_A r_w^2} + S \right)$$

   In this equation, $\(\overline{p}\)$  is the average reservoir pressure, $\( A \)$ is the drainage area, and $\( C_A \)$ is a shape factor. This formula is specifically suited for cases where a pseudo-steady-state flow regime is assumed, often used when pressure stabilizes after an initial production period.

4. **Additional Calculation for Complex Flow Paths**: For conditions involving more intricate well geometries, such as horizontal wells, the productivity index can be calculated by:

   
![image](https://github.com/user-attachments/assets/c1bdc5d7-8d3f-4e8f-9156-1f499f0f8a0c)


   where $\( a \)$ and $\( L \)$ are geometric factors specific to the horizontal section of the well. This equation adapts the productivity index for flow scenarios where a more complex well architecture influences reservoir inflow.
![image](https://github.com/user-attachments/assets/5a4e390d-0f20-4ed2-b519-b70db0c41de6)

![image](https://github.com/user-attachments/assets/95a8117b-9b96-476b-b8fb-77ffde4b0ab5)



These formulations enable a comprehensive analysis of well productivity across different flow regimes, assisting in the optimization of production methods and providing insights into reservoir management strategies under conditions where reservoir pressure remains above the bubble point.

**two-phase**

 *Vogel’s Equation
 
Vogel’s equation is still widely used in the industry. It is written as:

![image](https://github.com/user-attachments/assets/20cd449a-8ccb-4221-8894-d6d0cc453696)

![image](https://github.com/user-attachments/assets/b19cd486-8d04-4773-a004-7cc72f061609)



where $\( q_{\text{max}} \)$ is an empirical constant, and its value represents the maximum possible value of reservoir deliverability, or AOF (Absolute Open Flow). The $\( q_{\text{max}} \)$ can be theoretically estimated based on reservoir pressure and productivity index above the bubble-point pressure. 

###  Conditions

When the pressure is below the bubble point pressure, the behavior of the reservoir changes, and it becomes essential to consider the impacts of gas separation. The formula for $\( q_{\text{max}} \)$ under such conditions can be expressed as follows:

![image](https://github.com/user-attachments/assets/aaca1b1c-550e-49a3-98c6-89678226097d)


The pseudo–steady-state flow follows the $\( q_{\text{max}} \)$ formula as shown in the image above.


**Future IPR**



The future Inflow Performance Relationship (IPR) is an essential tool for predicting how a well's production capacity will evolve over time as reservoir pressure decreases. By utilizing empirical methods such as Vogel’s and Fetkovich’s, engineers can estimate future flow rates based on current reservoir conditions and historical performance data. These predictions consider factors like changes in reservoir pressure, fluid properties, and phase behavior, allowing for better management and optimization of production strategies. Accurately forecasting future IPR enables operators to anticipate potential declines in deliverability and make informed decisions regarding well interventions, enhanced oil recovery techniques, and overall reservoir management.

![image](https://github.com/user-attachments/assets/afefc09b-6b41-467b-890b-9293021b02e1)

![image](https://github.com/user-attachments/assets/de5313c8-af1f-4125-b746-631fd2363ac5)


## Applications




The application of reservoir deliverability calculations from Inflow Performance Relationship (IPR) curves is vital for effective reservoir management and optimization of production strategies. IPR curves provide a graphical representation of the relationship between flow rates and bottom-hole pressures, enabling operators to assess the current performance of a well and predict future deliverability under varying reservoir conditions. By analyzing historical production data and employing methods like Vogel’s and Fetkovich’s, engineers can generate future IPR curves that forecast the expected performance of the reservoir as it depletes over time. Importantly, this code can be utilized to calculate deliverability for different pressure conditions and a range of reservoir properties, such as viscosity, permeability, and fluid composition. These predictions inform decision-making processes regarding well interventions, enhanced oil recovery techniques, and overall reservoir management, ultimately leading to improved economic outcomes and sustained production efficiency.


## Results


In this project, we developed a code using the Vogel method that can obtain the IPR curve for conditions where the reservoir pressure is above the bubble point as well as for conditions where the reservoir pressure is below the bubble point. This code allows us to analyze the reservoir's production behavior in both scenarios, facilitating better decision-making for reservoir management. Additionally, a Future IPR code was also developed, providing accurate predictions of the reservoir's future performance and aiding in the optimization of production strategies. These tools can assist engineers in enhancing well performance and making more effective use of oil resources.

**Reservoir pressure above the bubble point**

![pseudosteady state flow](https://github.com/user-attachments/assets/54a56433-08ba-40d9-b16c-a08451acf88f)

![steady state flow](https://github.com/user-attachments/assets/b46c3b01-89e2-40be-83f9-58c5ba79011f)

![transient flow](https://github.com/user-attachments/assets/57eabca6-bb89-4dfd-a229-94b726a19d24)

**Reservoir pressure under the bubble point**

![Vogel’s equation pseudosteady state flow](https://github.com/user-attachments/assets/c82a0566-67a7-483f-8ef4-a511a7db3d00)

![Vogel’s equation steady state flow](https://github.com/user-attachments/assets/faec2101-0e95-4c8f-8c8a-c2109fef558c)

![Vogel’s equation transient flow](https://github.com/user-attachments/assets/9857630a-6766-4aef-97e0-5c42a9db3239)

**Future IPR**

![future IPR](https://github.com/user-attachments/assets/6f9e117f-efbb-4d8b-916d-5eae92bf99fb)










## Refrences
* Ahmed, Tarek. Reservoir engineering handbook. Gulf professional publishing
* Terry, Ronald E., J. Brandon Rogers, and Benjamin Cole Craft. Applied petroleum reservoir engineering.
* Guo, Boyun. Petroleum production engineering, a computer-assisted approach



## Authors

Ali.Karami



