const { readInput } = require("../utils/input");
const { printJson } = require("../utils/print");

const main = async () => {
  // const input = await readExample(__dirname);
  const input = await readInput(__dirname);
  printJson(input);
  solve(input);
};

const solve = (input) => {
  const data = buildSolutionData(input);
  // console.log("the data:");
  // printJson(data);

  const result = buildSolutionFromData(input, data);
  console.log("result:", result);
};

const buildSolutionData = (input) => {
  const gridMap = {};

  for (let i = 0; i < input.length; i++) {
    gridMap[i] = {};
    let flag = false;

    for (let subI = 0; subI < input[i].length; subI++) {
      // end of number (flag)
      if (flag && !isNumber(input[i][subI])) {
        // console.log("found end of number", { i, subI, input: input[i][subI] });
        flag = false;
        continue;
      }

      // current index as a number
      if (flag) {
        continue;
      }

      // when we find a number
      if (isNumber(input[i][subI])) {
        gridMap[i] = { ...gridMap[i], ...getNumberMap(input[i], i, subI) };
        flag = true;
      }
    }
  }

  return gridMap;
};

const buildSolutionFromData = (input, data) => {
  const allAdjacent = [];

  // console.log("data");
  // printJson(data);

  for (let row = 0; row < input.length; row++) {
    for (let col = 0; col < input[row].length; col++) {
      if (isSymbol(input[row][col])) {
        console.log("symbold at", { row, col, symb: input[row][col] });
        allAdjacent.push(...selectAdjacent(data, row, col));
      }
    }
  }

  // sum, keeping track of duplicates
  const keys = [];
  let sum = 0;

  for (const item of allAdjacent) {
    if (!keys.includes(item.id)) {
      keys.push(item.id);
      sum += item.value;
    }
  }

  return sum;
};

const selectAdjacent = (data, row, col) => {
  const adjacent = [];

  for (let r = -1; r < 2; r++) {
    for (let c = -1; c < 2; c++) {
      if (!r && !c) continue;
      const ri = row + r;
      const ci = col + c;

      if (data[ri]?.[ci]) {
        adjacent.push(data[ri][ci]);
      }
    }
  }

  return adjacent;
};

const getNumberMap = (line, prefix, index) => {
  let indexes = [];
  let number = "";
  while (index < line.length && isNumber(line[index])) {
    number += line[index];
    indexes.push(index);
    index++;
  }

  const intNumber = Number(number);
  const map = {};
  for (const ind of indexes) {
    map[ind] = { id: `${prefix}_${index}`, value: intNumber };
  }

  // console.log("result of numberMap", { intNumber, line, index, map });

  return map;
};

const isSymbol = (char) => {
  return char !== "." && !isNumber(char);
};

const isNumber = (char) => {
  const numbers = "0987654321".split("");
  return numbers.includes(char);
};

main();
