/**
 * Calculates the nth Fibonacci number using recursion.
 *
 * @param {number} n - The position in the sequence (starting from 0).
 * @returns {number} The Fibonacci number at position n.
 */
function fibonacci(n) {
  if (n <= 1) {
    return n;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// Example usage:
const num = 6;
console.log(`Fibonacci of ${num} is: ${fibonacci(num)}`);


// some comment 
console.log('No more comments')