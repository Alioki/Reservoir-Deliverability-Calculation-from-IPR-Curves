# Project Title

Reservoir Deliverability Calculation from IPR Curves


## Description
Determining the proportions of gas and liquid in hydrocarbon reservoirs is essential for optimizing field production. Understanding the phase composition of each component in gas and liquid phases enables engineers to develop better strategies for production, management, and maintenance of hydrocarbon fields. One common method for estimating this composition is by using the K-factor, derived from the Peng-Robinson equation of state and fugacity coefficient calculations. Combined with flash calculations, this approach provides the equilibrium conditions between gas and liquid phases for specific mixtures, allowing precise determination of phase composition.

In this study, we examined a mixture containing three components—methane (CH₄), normal butane (n-C₄), and normal decane (n-C₁₀)—with molar fractions of 0.5301 for methane, 0.1055 for n-C₄, and 0.3644 for n-C₁₀. At a pressure of 1000 psi and temperature of 210°F, we employed flash calculations to determine the phase composition of each component in both the gas and liquid phases. Additionally, we accounted for binary interaction coefficients, setting values of 0.02 for methane-n-butane, 0.04 for methane-n-decane, and 0 for n-butane-n-decane. These coefficients are critical for accurately representing the non-ideal interactions between components in the Peng-Robinson model.

## Methodology

This code utilizes several equations to achieve accurate phase behavior predictions for hydrocarbon mixtures. The primary equation used is the **Peng-Robinson equation of state**, which is employed to predict the phase behavior of hydrocarbons under various temperature and pressure conditions. The Peng-Robinson equation is given as follows:

$\[
P = \frac{RT}{V - b} - \frac{a \alpha}{V(V + b) + b(V - b)}
\]$

where $\( P \)$ is the pressure, $\( T \)$ is the temperature, $\( V \)$ is the molar volume, $\( R \)$ is the universal gas constant, $\( a \)$ and $\( b \)$ are parameters related to the components of the mixture, and $\( \alpha \)$ is a temperature-dependent function calculated based on the reduced temperature and the acentric factor of the components.

Additionally, the **fugacity coefficient** is used to quantify the escape tendency of each component in both gas and liquid phases, ensuring that phase equilibrium between these phases is maintained. The fugacity coefficient for each component in the liquid and gas phases is calculated as follows:

$\phi =\exp \left(Z-1-\ln \left(Z-B\right)-\frac{A}{2\sqrt{2}B}\ln \left(\frac{Z+\left(1+\sqrt{2}\right)B}{Z+\left(1-\sqrt{2}\right)B}\right)\right)$

where $\( \phi \)$ represents the fugacity coefficient, \( Z \) is the compressibility factor, and \( A \) and \( B \) are constants related to the equation of state and the composition of the mixture.

The code also implements **flash calculations**, which are used to determine the phase distribution of each component (gas and liquid). These calculations involve determining the distribution ratio, or \( K \)-factor, for each component, which is given by:

$\[
K = \frac{y}{x}
\]$

where $\( y \)$ is the mole fraction of the component in the gas phase, and $\( x \)$ is the mole fraction of the component in the liquid phase.

By using these equations and incorporating input parameters like critical temperature, critical pressure, and acentric factor for each component, the code enables more detailed analysis and prediction of phase behavior in complex mixtures. This method can be extended to handle multi-component systems, supporting a wide range of hydrocarbon reservoir modeling applications.

It is important to note that these relationships are presented in a general overview. To gain a deeper understanding of the relationships, it is essential to consult the referenced sources.
## Applications


This method, demonstrated through a simplified example, can be extended to more complex hydrocarbon mixtures containing various components. By utilizing the same approach with the **K-factor** calculations, along with **Peng-Robinson equation of state**, **fugacity coefficients**, and **flash calculations**, it is possible to accurately determine the phase composition of multiple components in a mixture. For each component, required parameters include the **mole fraction**, **critical temperature** and **pressure**, **acentric factor**, and **vapor pressure**. This enables accurate modeling of phase behavior in reservoirs, which is critical for optimizing production processes. The capability to calculate gas and liquid compositions under various conditions makes this approach highly applicable in reservoir simulations, facility design, and overall resource management in hydrocarbon fields.



## Results

In conclusion, the K-factors obtained from our study are as follows: for methane, the K-factor is 3.9916; for normal butane (n-C₄), it is 0.2359; and for normal decane (n-C₁₀), it is 0.0031. These values are remarkably close to those found in the literature, validating the reliability of our approach. It is important to note that the data used, including critical temperature and pressure, acentric factor, and vapor pressure, are up-to-date and essential for accurate modeling of phase behavior in reservoirs. This accuracy is critical for optimizing production processes, enabling engineers to make informed decisions regarding the management and extraction of hydrocarbons. Additionally, a code has been developed that allows for the calculation of K-factors for mixtures with a larger number of components, facilitating more complex analyses in hydrocarbon reservoir studies.

## Refrences
* McCain Jr, William D. "Properties of petroleum fluids."
* Smith, Joseph Mauk. "Introduction to chemical engineering thermodynamics."



## Authors

Ali.Karami



