const fibonacci = require('../../questions/javascript/fibonacci');
const chai = require('chai');

chai.expect(fibonacci.getNthFibBruteForce(6)).to.deep.equal(5);
chai.expect(fibonacci.getNthFibMemoize(6)).to.deep.equal(5);
chai.expect(fibonacci.getNthFibCounter(6)).to.deep.equal(5);