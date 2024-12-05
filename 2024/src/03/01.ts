import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pj } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
        // const rawInput = readFile(sampleFilepath);
        const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // p(...input);

        const result = solve(input);
        pj(result);
};

const parseInput = (rawInput: string) => {
        const parsed = rawInput.matchAll(/mul\(\d+,\d+\)/g);
        const matches = [];
        const result = [];
        for (const match of parsed) {
                matches.push(match[0]);
                const args = match[0].match(/\d+,\d+/);
                const numbers = args?.[0]?.split(',');
                const parsed = numbers
                        ?.map((item) => Number(item))
                        ?.filter((item) => !Number.isNaN(item));

                if (numbers?.length !== 2 || parsed?.length !== 2) {
                        throw new Error(`numbers.length !== 2`);
                }
                result.push(parsed);
        }
        // pj(matches);
        return result;
};

const solve = (input: number[][]) => {
        let total = 0;
        for (const pair of input) {
                total += pair[0] * pair[1];
        }
        return total;
};

main();

export {};
