const program = require('../../questions/javascript/fibonacci');
const chai = require('chai');

chai.expect(program.getNthFibBruteForce(6)).to.deep.equal(5);
chai.expect(program.getNthFibMemoize(6)).to.deep.equal(5);
chai.expect(program.getNthFibCounter(6)).to.deep.equal(5);