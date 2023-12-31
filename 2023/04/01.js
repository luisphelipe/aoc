const { readExample, readInput } = require("../utils/input");
const { printJson } = require("../utils/print");

const main = async () => {
  const input = await readExample(__dirname);
  // const input = await readInput(__dirname);

  printJson(input);
  console.log("result:", solve(input));
};

const solve = (input) => {
  const data = parseData(input);
  // console.log("the data:");
  printJson(data);

  const result = 0;
  return result;
};

const parseData = (input) => {
  const parsed = [];

  for (const card of input) {
    if (!card) continue;

    const [cardNumber, numbers] = card.split(": ");
    const [winningNumbers, playedNumbers] = numbers.split(" | ");

    const item = {
      id: cardNumber,
      winningNumbers: numbersStringToArray(winningNumbers),
      playedNumbers: numbersStringToArray(playedNumbers),
    };

    parsed.push(item);
  }

  return parsed;
};

const solveForData = (data) => {
  let total = 0;

  for (const card of data) {
    let points = 0;

    for (const playedNumber of card.playedNumbers) {
      if (card.winningNumbers.includes(playedNumber)) {
        points = points * 2 || 1;
      }
    }

    total += points;
  }

  return total;
};

const numbersStringToArray = (numbersString) => {
  return numbersString.split(" ").map((num) => Number(num));
};

main();
