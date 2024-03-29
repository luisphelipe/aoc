const { readExample, readInput } = require("../utils/input");
const { DebugStackLog, printDebug, colorMatch } = require("../utils/print");

const DEBUG = false;

const main = async () => {
  const debugLog = new DebugStackLog("[01/02]");
  debugLog.log("starting");

  // const input = await readExample(__dirname);
  // const input = await readInput(__dirname, { filename: "example2" });
  const input = await readInput(__dirname);
  debugLog.log("read input");

  const solution = solve(input);
  debugLog.log("completed solve");
  debugLog.print();
  console.log(`solution = ${solution}`);
};

const solve = (stringArray) => {
  const solutions = [];

  for (const string of stringArray) {
    const lineSolution = solveForLine(string);
    solutions.push(lineSolution);
  }

  const sum = solutions.reduce((a, b) => a + b, 0);

  return sum;
};

const digits = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
];

const solveForLine = (string) => {
  const match = [...Object.keys(digits), ...digits];
  const matches = matchesWithIndex(string, match);

  // console.log(string);
  // console.log(matches);

  const sorted = matches.sort((a, b) => (a.index < b.index ? -1 : 1));

  const first = sorted[0];
  const last = sorted[sorted.length - 1];

  const value = first.value * 10 + last.value;

  printDebug(string, DEBUG);
  printDebug(first, DEBUG);
  printDebug(last, DEBUG);
  printDebug(value, DEBUG);

  return value;
};

const matchesWithIndex = (string, options) => {
  // console.log(options);
  const matches = [];

  for (let ind = 0; ind < string.length; ind++) {
    for (const substring of options) {
      if (match(string, ind, substring)) {
        matches.push({
          value: toNumber(substring),
          index: ind,
        });
        break;
      }
    }
  }

  return matches;
};

const match = (string, baseIndex, substring) => {
  for (let ind = 0; ind < substring.length; ind++) {
    if (string[baseIndex + ind] !== substring[ind]) {
      return false;
    }
  }

  return true;
  // return string.slice(0, substring.length) === substring;
};

const toNumber = (spelled) => {
  if (!Number.isNaN(Number(spelled))) {
    return Number(spelled);
  }

  for (const [index, spell] of digits.entries()) {
    if (spelled === spell) return index;
  }
};

main();
