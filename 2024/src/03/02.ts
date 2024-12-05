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
        const parsed = rawInput.matchAll(/(mul\(\d+,\d+\)|do\(\)|don't\(\))/g);
        const matches = [];
        const result = [];
        for (const match of parsed) {
                matches.push(match[0]);

                if (match[0] === 'do()') {
                        result.push(true);
                        continue;
                }

                if (match[0] === "don't()") {
                        result.push(false);
                        continue;
                }

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

const solve = (input: (number[] | boolean)[]) => {
        let isActive = true;
        let total = 0;
        for (const value of input) {
                if (typeof value === 'boolean') {
                        isActive = value;
                } else if (isActive) {
                        total += value[0] * value[1];
                }
        }
        return total;
};

main();

export {};
