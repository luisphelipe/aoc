import * as path from "path";
import { readFile } from "../utils/input";
import { p, pj } from "../utils/print";

const sampleFilepath = path.join(__dirname, "sample");
const inputFilepath = path.join(__dirname, "input");

const main = () => {
  // const rawInput = readFile(sampleFilepath);
  const rawInput = readFile(inputFilepath);
  // pj(rawInput);

  const input = parseInput(rawInput);
  // pj(input);

  const result = solve(input);
  p(result);
};

const parseInput = (rawInput: string) => {
  const lines = rawInput.split("\n");

  const matrix = lines.map((line) =>
    line.split(" ").map((value) => Number(value))
  );

  return matrix;
};

const solve = (input: number[][]) => {
  let total = 0;

  for (const line of input) {
    const result = solveLine(line, true);
    total += result;
  }

  return total;
};

const solveLine = (line: number[], root = false): 1 | 0 => {
  let lastDiff = line[1] - line[0];

  for (let i = 1; i < line.length; i++) {
    const diff = line[i] - line[i - 1];

    if (Math.abs(diff) > 3 || lastDiff * diff <= 0) {
      // attempt to solve without line[i - 1] or line[i]
      if (root) {
        return (
          solveLine(removeValue(line, i - 2)) ||
          solveLine(removeValue(line, i - 1)) ||
          solveLine(removeValue(line, i))
        );
      }

      return 0;
    }

    lastDiff = diff;
  }

  return 1;
};

const removeValue = (line: number[], index: number) => {
  const copy = [...line];
  if (index >= 0) copy.splice(index, 1);
  return copy;
};

main();

export {};
