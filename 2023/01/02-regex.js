const { readExample, readInput } = require("../utils/input");
const { printDebug, colorMatch } = require("../utils/print");

const DEBUG = false;

const main = async () => {
  // const input = await readExample(__dirname);
  // const input = await readInput(__dirname, { filename: "example2" });
  const input = await readInput(__dirname);

  solve(input);
};

const solve = (stringArray) => {
  const solutions = [];

  for (const string of stringArray) {
    const lineSolution = solveForLine(string);
    solutions.push(lineSolution);
  }

  const sum = solutions.reduce((a, b) => a + b, 0);
  console.log(`total = ${sum}`);

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
  const match = [...Object.keys(digits), ...digits].join("|");
  const matches = matchesWithIndex(string, match);
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

const matchesWithIndex = (string, match) => {
  const pattern = `(?=(${match}))`; // with lookahead matching to work with overlaps
  const regex = new RegExp(pattern, "g");
  const matches = [...string.matchAll(regex)].map((item) => ({
    value: toNumber(item[1]),
    index: item.index,
  }));
  return matches;
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
