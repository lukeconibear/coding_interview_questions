function getNthFibBruteForce(n) { // time O(2^n), space O(n)
    if (n == 2) {
          return 1;
      } else if (n == 1) {
          return 0;
      } else {
          return getNthFibBruteForce(n - 1) + getNthFibBruteForce(n - 2);
      }
  }
  
  function getNthFibMemoize(n, memoize={1: 0, 2: 1}) { // time O(n), space O(n)
    if (n in memoize) {
          return memoize[n];
      } else {
          memoize[n] = getNthFibMemoize(n - 1, memoize) + getNthFibMemoize(n - 2, memoize);
          return memoize[n];
      }
  }
  
  function getNthFibCounter(n) { // time O(n), space O(1)
    const lastTwo = [0, 1];
      let counter = 3;
      while (counter <= n) {
          const nextFib = lastTwo[0] + lastTwo[1];
          lastTwo[0] = lastTwo[1];
          lastTwo[1] = nextFib;
          counter++;
      }
      return n > 1 ? lastTwo[1] : lastTwo[0]
  }
  
  exports.getNthFibBruteForce = getNthFibBruteForce;
  exports.getNthFibMemoize = getNthFibMemoize;
  exports.getNthFibCounter = getNthFibCounter;