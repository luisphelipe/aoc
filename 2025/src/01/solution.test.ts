import * as path from 'path';
import { readFile } from '../utils/input';
import { parseInput, solvePart1, solvePart2 } from './solution';

const sampleFilepath = path.join(__dirname, 'sample');

const runTests = (tests: [string, unknown, unknown][]) => {
    let passed = 0;
    let failed = 0;

    for (const [desc, value, expected] of tests) {
        if (value != expected) {
            console.log(`✗ ${desc}: expected ${expected}, got ${value}`);
            failed++;
        } else {
            console.log(`✓ ${desc}`);
            passed++;
        }
    }

    console.log(`\n${passed} passed, ${failed} failed`);
};

const main = () => {
    const rawInput = readFile(sampleFilepath);
    const input = parseInput(rawInput);

    const tests: [string, unknown, unknown][] = [
        ['Part 1', solvePart1(input), 3],
        ['Part 2', solvePart2(input), 6],
    ];

    runTests(tests);
};

main();
