# Project Title

Reservoir Deliverability Calculation from IPR Curves


## Description


Reservoir deliverability is defined as the oil or gas production rate achievable from a reservoir at a given bottom-hole pressure. It is a major factor affecting well deliverability and determines the types of completion and artificial lift methods to be used. A thorough knowledge of reservoir productivity is essential for production engineers, as it aids in optimizing extraction strategies and ensuring the efficiency of production operations.

In this project, the **generalized Vogel IPR model** is applied to describe well inflow from multilayer reservoirs where reservoir pressures are above oil bubble-point pressures, while wellbore pressures remain below these bubble-point pressures. By using this approach, the project examines **IPR curves** under **Steady-state**, **Pseudo–steady-state**, and **Transient** flow conditions, considering scenarios where the reservoir either reaches bubble point pressure or remains above it by the end of the operation. Given the complexity of replicating these conditions in real-world settings, the project is primarily educational and aimed at deepening understanding of reservoir inflow behavior in various conditions. Additionally, future **IPR** values are calculated to predict potential production performance over time.

## Methodology

In scenarios where the **reservoir pressure is maintained above the bubble-point pressure**, the productivity index $( J^* )$ can be calculated using various flow regimes to assess well performance. This approach is essential for evaluating well deliverability and understanding flow behavior under different operational conditions when the reservoir pressure is higher than the pressure at which gas starts to separate from oil.

1. **Transient Flow**: For a vertical well with radial transient flow, the productivity index is defined as:

   $$J^* = \frac{q}{(p_i - p_{wf})} = \frac{kh}{162.6 B_o \mu_o} \left( \log t + \log \frac{k}{\phi \mu_o c_t r_w^2} - 3.23 + 0.87S \right)$$

   where \( q \) represents the flow rate, \( p_i \) is the initial reservoir pressure, \( p_{wf} \) is the flowing bottom-hole pressure, \( k \) is the permeability, \( h \) is the thickness, \( B_o \) is the oil formation volume factor, \( \mu_o \) is the oil viscosity, \( \phi \) is the porosity, \( c_t \) is the total compressibility, \( r_w \) is the well radius, and \( S \) is the skin factor. This equation considers both formation and fluid properties to determine flow under transient conditions, capturing the impact of time on productivity.

2. **Steady-State Flow**: In radial steady-state flow around a vertical well, the productivity index can be expressed as:

   
   $$J^* = \frac{q}{(p_e - p_{wf})} = \frac{kh}{141.2 B_o \mu_o} \left( \ln \frac{r_e}{r_w} + S \right)$$

   Here, \( p_e \) is the external boundary pressure, and \( r_e \) is the drainage radius. This steady-state model is useful for conditions where pressure gradients stabilize over time, reflecting long-term reservoir deliverability.

3. **Pseudo–Steady-State Flow**: For pseudo–steady-state flow in a vertical well, the productivity index is determined by:

   
   $$J^* = \frac{q}{(\overline{p} - p_{wf})} = \frac{kh}{141.2 B_o \mu_o} \left( \frac{1}{2} \ln \frac{4A}{C_A r_w^2} + S \right)$$

   In this equation, \( \overline{p} \) is the average reservoir pressure, \( A \) is the drainage area, and \( C_A \) is a shape factor. This formula is specifically suited for cases where a pseudo-steady-state flow regime is assumed, often used when pressure stabilizes after an initial production period.

4. **Additional Calculation for Complex Flow Paths**: For conditions involving more intricate well geometries, such as horizontal wells, the productivity index can be calculated by:

   
$$J^* = \frac{q}{(p_e - p_{wf})} = \frac{k_y h}{141.2 B \mu} \left\{ \ln \left( \frac{a + \sqrt{a^2 - (L/2)^2}}{L/2} \right) + \frac{L}{a}\ln \left( \frac{L}{r_w} \right) \right\}$$

   where \( a \) and \( L \) are geometric factors specific to the horizontal section of the well. This equation adapts the productivity index for flow scenarios where a more complex well architecture influences reservoir inflow.

These formulations enable a comprehensive analysis of well productivity across different flow regimes, assisting in the optimization of production methods and providing insights into reservoir management strategies under conditions where reservoir pressure remains above the bubble point.


## Applications


This method, demonstrated through a simplified example, can be extended to more complex hydrocarbon mixtures containing various components. By utilizing the same approach with the **K-factor** calculations, along with **Peng-Robinson equation of state**, **fugacity coefficients**, and **flash calculations**, it is possible to accurately determine the phase composition of multiple components in a mixture. For each component, required parameters include the **mole fraction**, **critical temperature** and **pressure**, **acentric factor**, and **vapor pressure**. This enables accurate modeling of phase behavior in reservoirs, which is critical for optimizing production processes. The capability to calculate gas and liquid compositions under various conditions makes this approach highly applicable in reservoir simulations, facility design, and overall resource management in hydrocarbon fields.



## Results

In conclusion, the K-factors obtained from our study are as follows: for methane, the K-factor is 3.9916; for normal butane (n-C₄), it is 0.2359; and for normal decane (n-C₁₀), it is 0.0031. These values are remarkably close to those found in the literature, validating the reliability of our approach. It is important to note that the data used, including critical temperature and pressure, acentric factor, and vapor pressure, are up-to-date and essential for accurate modeling of phase behavior in reservoirs. This accuracy is critical for optimizing production processes, enabling engineers to make informed decisions regarding the management and extraction of hydrocarbons. Additionally, a code has been developed that allows for the calculation of K-factors for mixtures with a larger number of components, facilitating more complex analyses in hydrocarbon reservoir studies.

## Refrences
* McCain Jr, William D. "Properties of petroleum fluids."
* Smith, Joseph Mauk. "Introduction to chemical engineering thermodynamics."



## Authors

Ali.Karami



