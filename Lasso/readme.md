## Lasso method
Lasso is another extension built on regularized linear regression, but with a small twist. The loss function of Lasso is in the form:

L = ∑( Ŷi– Yi)2 + λ∑ |β|

Ridge regression is in absolute value. But this difference has a huge impact on the trade-off. Lasso method overcomes the disadvantage of Ridge regression by not only punishing high values of the coefficients β but actually setting them to zero if they are not relevant. Therefore, ending up with fewer features included in the model than you started with, which is a huge advantage.
