import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pj, pm } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
    const rawInput = readFile(sampleFilepath);
    // const rawInput = readFile(inputFilepath);

    const input = parseInput(rawInput);

    const result1 = solvePart1(input);
    p('Part 1:', result1);

    const result2 = solvePart2(input);
    p('Part 2:', result2);
};

const parseInput = (rawInput: string) => {
    const parsed = rawInput.split('\n');
    return parsed;
};

const solvePart1 = (input: string[]) => {
    return 0;
};

const solvePart2 = (input: string[]) => {
    return 0;
};

if (require.main === module) {
    main();
}

export { parseInput, solvePart1, solvePart2 };
