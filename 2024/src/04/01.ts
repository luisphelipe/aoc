import * as path from 'path';
import { readFile } from '../utils/input';
import { pj, pm } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const TARGET = ['X', 'M', 'A', 'S'];

const DIRECTIONS = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
];

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
        for (let row = 0; row < input.length; row++) {
                for (let col = 0; col < input[0].length; col++) {
                        for (const direction of DIRECTIONS) {
                                matches += solveFor(input, row, col, direction, 0);
                        }
                }
        }
        return matches;
};

const solveFor = (
        input: string[][],
        row: number,
        col: number,
        direction: number[],
        ind: number,
) => {
        if (ind >= TARGET.length) return 1; // completed match

        const targetChar = TARGET[ind];

        if (row < 0 || col < 0 || row >= input.length || col >= input[0].length) {
                return 0; // out of bounds
        }

        if (input[row][col] !== targetChar) return 0; // didn't match

        return solveFor(input, row + direction[0], col + direction[1], direction, ind + 1);
};

main();

export {};
