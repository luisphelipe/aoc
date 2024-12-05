import * as path from 'path';
import { readFile } from '../utils/input';
import { pj, pm } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
        // const rawInput = readFile(sampleFilepath);
        const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // pm(input);

        const result = solve(input);
        pj(result);
};

const parseInput = (rawInput: string) => {
        const parsed = rawInput.split('\n');
        const matrix = parsed.map((line) => line.split(''));
        return matrix;
};

const solve = (input: string[][]) => {
        let matches = 0;
        for (let row = 1; row < input.length - 1; row++) {
                for (let col = 1; col < input[0].length - 1; col++) {
                        matches += solveFor(input, row, col);
                }
        }
        return matches;
};

const solveFor = (input: string[][], row: number, col: number) => {
        if (
                input[row][col] === 'A' &&
                ['M', 'S'].includes(input[row - 1][col - 1]) &&
                ['M', 'S'].includes(input[row + 1][col + 1]) &&
                input[row - 1][col - 1] !== input[row + 1][col + 1] &&
                ['M', 'S'].includes(input[row - 1][col + 1]) &&
                ['M', 'S'].includes(input[row + 1][col - 1]) &&
                input[row - 1][col + 1] !== input[row + 1][col - 1]
        ) {
                return 1;
        }

        return 0;
};

main();

export {};
