# Utilizing Monte Carlo Simulations to Forecast Stock Prices: A Detailed Theoretical Approach

## Introduction

Monte Carlo simulations are a cornerstone of computational finance, particularly useful for modeling and predicting complex systems such as stock price movements. This discussion focuses on the derivation of the model used in these simulations and the rationale for selecting specific probability distributions.

## Theoretical Derivation of the Stock Price Model

### Geometric Brownian Motion (GBM)

The stock price model typically employed in Monte Carlo simulations is based on Geometric Brownian Motion (GBM), which is a continuous-time stochastic process. GBM is widely used in financial modeling because it has properties that are consistent with real-world stock price movements, such as the log-normality of prices, the stochastic nature of returns, and the non-negativity of prices.

#### The Model

The GBM model for stock prices is given by the differential equation:

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$

Where:

- $\(S_t\)$: the stock price at time \(t\),
- \(\mu\): the drift coefficient representing the expected return,
- \(\sigma\): the volatility coefficient,
- \(dW_t\): the increment of a Wiener process (standard Brownian motion), which introduces the random variation.

#### Solution to the GBM Differential Equation

The solution to this stochastic differential equation is:

$$
S_t = S_0 \times e^{(\mu - \frac{1}{2} \sigma^2) t + \sigma W_t}
$$

This expression shows that the stock price \(S_t\) at any future time \(t\) is log-normally distributed, which means the logarithm of the stock price is normally distributed. The term \((\mu - \frac{1}{2} \sigma^2)\) adjusts the drift to account for the variance drag (the Jensen's inequality effect on exponential growth processes).

## Probability Distribution and Its Implications

### Normal Distribution and the Wiener Process

In the GBM model, \(W_t\), which represents a Wiener process (or Brownian motion), is characterized by increments that are normally distributed. This normal distribution is essential because it models the random shocks to the logarithm of the stock price, reflecting daily market volatility. This random fluctuation is captured through the stochastic term \(\sigma W_t\) in the differential equation.

### Log-Normal Distribution of Stock Prices

Under GBM, while the increments \(W_t\) of the Wiener process are normally distributed, the stock prices themselves are modeled to be log-normally distributed. This follows because if a variable \(X\) is normally distributed, then \(e^X\) is log-normally distributed. Thus, the stock price \(S_t\) at any future time \(t\), given by:

$$
S_t = S_0 \times e^{(\mu - \frac{1}{2} \sigma^2) t + \sigma W_t}
$$

is log-normally distributed because \((\mu - \frac{1}{2} \sigma^2) t + \sigma W_t\) is normally distributed. This results from the exponential transformation applied to the linear combination of normally distributed terms.

#### Importance of the Log-Normal Distribution

The log-normal distribution is particularly suited for modeling stock prices for several reasons:

- **Non-negativity**: It ensures that stock prices cannot go below zero, a necessary physical constraint in the financial markets.
- **Skewness and heavy tails**: It captures the observed skewness and heavier tails in stock price distributions compared to a normal distribution. This means there is a greater probability of observing extreme values, reflecting the reality of stock price movements during volatile market conditions.

## Conclusion

The theoretical framework of Geometric Brownian Motion, combined with the probabilistic modeling via the Wiener process, provides a solid basis for the Monte Carlo simulations used in stock price forecasting. Understanding the derivation of this model and the distributions involved is essential for effectively applying Monte Carlo methods in financial analyses, ensuring that the simulations reflect the complexity and stochastic nature of financial markets.

$\S_t$

$\ S_t $

$\S_t$

