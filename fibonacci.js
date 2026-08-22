/**
 * Calculates the nth Fibonacci number (0-indexed).
 * @param {number} n - The position in the sequence (starting from 0).
 * @returns {number} The Fibonacci number at position n.
 */
// ponytail: iterative to avoid O(2^n) recursion and stack overflow; memoization only if huge n needed
function fibonacci(n) {
  let [a, b] = [0, 1];
  for (let i = 0; i < n; i++) [a, b] = [b, a + b];
  return a;
}

// Example usage:
const num = 6;

console.log(`Fibonacci of ${num} is: ${fibonacci(num)}`);
