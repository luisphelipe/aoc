import * as path from 'path';
import { readFile } from '../utils/input';
import { pj } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
        const rawInput = readFile(sampleFilepath);
        // const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // pj(input);

        const result = solve(input);
        pj(result);
};

const parseInput = (rawInput: string) => {
        const parsed = rawInput.split('\n');
        return parsed;
};

const solve = (input: string[]) => {
        const result = 'Working';
        return result;
};

main();

export {};
