import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pd, pj, pm } from '../utils/print';

const inputFilepath = path.join(__dirname, 'input');

const main = () => {
    const rawInput = readFile(inputFilepath);

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

const solvePart1 = (input: string[], debug = false) => {
    let val = 50,
        count = 0;
    pd(input);
    for (const instruction of input) {
        const move = instruction[0];
        const ammount = Number(instruction.slice(1));
        if (move === 'L') val -= ammount;
        if (move === 'R') val += ammount;
        if (val < 0) val = 100 - (Math.abs(val) % 100);
        if (val >= 100) val = val % 100;
        if (val === 0) count++;
        pd({ instruction, move, ammount, val, count });
    }

    return count;
};

const solvePart2 = (input: string[]) => {
    let current = 50,
        count = 0;

    for (const instruction of input) {
        const dir = instruction[0];
        const increment = dir === 'L' ? -1 : 1;
        let value = Number(instruction.slice(1));

        if (value > 100) {
            count += Math.floor(value / 100);
            value %= 100;
        }

        while (value > 0) {
            current += increment;
            if (current > 99) current = 0;
            if (current < 0) current = 99;
            if (current === 0) count++;
            value--;
        }
    }

    return count;
};

if (require.main === module) {
    main();
}

export { parseInput, solvePart1, solvePart2 };
