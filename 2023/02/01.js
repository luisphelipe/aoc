const { readExample, readInput } = require("../utils/input");
const { DebugStackLog, printJson } = require("../utils/print");

const main = async () => {
  // const input = await readExample(__dirname);
  const input = await readInput(__dirname);
  solve(input);
};

const solve = (input) => {
  let sum = 0;

  const debug = new DebugStackLog();
  debug.log("starting");

  const parsed = parseInput(input);
  debug.log("parsed");
  // printJson(parsed);

  const conditionMax = {
    red: 12,
    green: 13,
    blue: 14,
  };

  for (const line of parsed) {
    sum += solveForLine(line, conditionMax);
  }
  debug.log("solved");

  console.log(`total = ${sum}`);
  debug.print();
};

const parseInput = (input) => {
  return input.map((line, index) => {
    const game = line.replace(/Game \d+: /, "").split("; ");
    const rounds = [];
    let max;

    for (const round of game) {
      const values = round.split(", ").map((val) => val.split(" "));
      const valuesEntries = values.map(([val, key]) => [key, Number(val)]);
      const parsed = Object.fromEntries(valuesEntries);

      rounds.push(parsed);
      max = updateMaxValue(max, parsed);
    }

    const id = index + 1;
    return { id, game: `Game ${id}`, rounds, max };
  });
};

const updateMaxValue = (max, parsed) => {
  if (max) {
    for (const key in parsed) {
      if (!max[key] || max[key] < parsed[key]) {
        max[key] = parsed[key];
      }
    }
  } else {
    max = { ...parsed };
  }
  return max;
};

const solveForLine = (line, conditionMax) => {
  for (const key in line.max) {
    if (line.max[key] > conditionMax[key]) {
      return 0;
    }
  }

  return line.id;
};

main();
