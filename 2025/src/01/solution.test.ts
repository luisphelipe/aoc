import * as assert from 'assert';
import * as path from 'path';
import { readFile } from '../utils/input';
import { parseInput, solvePart1, solvePart2 } from './solution';

const sampleFilepath = path.join(__dirname, 'sample');

const testPart1 = (input: string[]) => {
    const result = solvePart1(input);
    assert.strictEqual(result, 3, `Part 1: expected 3, got ${result}`);
    console.log('✓ Part 1 passed');
};

const testPart2 = (input: string[]) => {
    const result = solvePart2(input);
    assert.strictEqual(result, 6, `Part 2: expected 6, got ${result}`);
    console.log('✓ Part 2 passed');
};

const main = () => {
    const rawInput = readFile(sampleFilepath);
    const input = parseInput(rawInput);

    // testPart1(input);
    testPart2(input);

    console.log('\nAll tests passed!');
};

main();
