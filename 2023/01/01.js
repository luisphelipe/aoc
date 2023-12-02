const { readExample, readInput } = require("../utils/input");

const main = async () => {
  //   const input = await readExample(__dirname);
  const input = await readInput(__dirname);
  solve(input);
};

const solve = (stringArray) => {
  let sum = 0;

  for (const string of stringArray) {
    const calibration = solveForLine(string);
    // console.log(`${calibration} => ${string}`);
    sum += calibration;
  }

  console.log(`total = ${sum}`);
};

const solveForLine = (string) => {
  const digits = string.replace(/[^0-9]/g, "").split("");
  const firstDigit = digits[0];
  const lastDigit = digits[digits.length - 1];
  const calibration = firstDigit + lastDigit;
  return Number(calibration);
};

main();
