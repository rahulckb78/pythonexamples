import math

# Given values
mu = 175       # Mean
sigma = 6      # Standard deviation
x = 180        # Height to evaluate PDF at

# Normal distribution PDF formula
def normal_pdf(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coefficient * math.exp(exponent)

# Calculate PDF at x = 180
pdf_value = normal_pdf(x, mu, sigma)
pdf_value