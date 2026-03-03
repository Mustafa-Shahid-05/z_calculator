# Gas Z-Factor Correlation Toolkit

Python implementation of commonly used gas compressibility factor (Z) correlations in petroleum engineering.

Implemented Correlations
- Papay
- Hall–Yarborough (Newton-Raphson solution)
- Dranchuk–Abu–Kassem (nonlinear numerical solution)

Inputs

- Reduced Pressure (Ppr)

- Reduced Temperature (Tpr)

Output
Gas compressibility factor (Z)

Structure
zFactor.py     (Correlation implementations)
main.py        (Execution script)
mainUi.py      (Simple user interface)
Example

z = zFactor(ppr=5, tpr=3)

print(z.papayJ())
print(z.hallYarbough())
print(z.dranchukAbuKassem())
