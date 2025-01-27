import * as path from 'path';
import { readFile } from '../utils/input';
import { pj } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
        // const rawInput = readFile(sampleFilepath);
        const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // pj(input);

        const result = solve(input);
        pj(result);
};

const parseInput = (rawInput: string) => {
        const matrix: number[][] = [[], []];

        for (const line of rawInput.split('\n')) {
                const values = line.split(/\s+/);
                for (let i = 0; i < values.length; i++) {
                        matrix[i].push(Number(values[i]));
                }
        }

        return matrix;
};

const solve = (input: number[][]) => {
        // 1. sort
        for (let i = 0; i < input.length; i++) {
                input[i] = input[i].sort((a, b) => a - b);
        }

        // 2. build "occurrences" map
        const occurrenceTimesMap: { [key: number]: number } = {};
        for (const number of input[1]) {
                if (!occurrenceTimesMap[number]) occurrenceTimesMap[number] = 0;
                occurrenceTimesMap[number] += 1;
        }

        // 3. sum for each number
        let total = 0;
        for (let i = 0; i < input[0].length; i++) {
                const number = input[0][i];
                const occurrenceTimes = occurrenceTimesMap[number] || 0;
                total += number * occurrenceTimes;
        }

        // 4. return total sum
        return total;
};

main();

export {};
