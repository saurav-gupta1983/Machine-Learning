from numpy import *
from computeCost import computeCost
import pdb

def gradientDescent(X, y, theta, alpha, num_iters):
  #GRADIENTDESCENT Performs gradient descent to learn theta
  #   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by
  #   taking num_iters gradient steps with learning rate alpha

  # Initialize some useful values
  m = len(y) # number of training examples
  J_history = zeros((num_iters, 1))

  for iteration in range(num_iters):

      # ====================== YOUR CODE HERE ======================
      # Instructions: Perform a single gradient step on the parameter vector
      #               theta.
      #
      # Hint: While debugging, it can be useful to print out the values
      #       of the cost function (computeCost) and gradient here.
      #
      # use "pdb.set_trace()" to drop into the debugger at this point




      # ============================================================

      # Save the cost J in every iteration
      J_history[iteration] = computeCost(X, y, theta)
      #J_history(iter)

  return (theta, J_history)
