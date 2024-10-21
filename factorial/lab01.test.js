// File: lab01.test.js

const { factorial } = require('./lab01');


test('factorial function should return the factorial of a positive number', () => {
  expect(factorial(5)).toBe(120);
  expect(factorial(3)).toBe(6);
  expect(factorial(10)).toBe(3628800);
});

test('factorial function should return 1 for factorial of zero', () => {
  expect(factorial(0)).toBe(1);
});

test('factorial function should return null for negative numbers', () => {
  expect(factorial(-1)).toBe(null);
  expect(factorial(-5)).toBe(null);
});
