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
    let val = 50,
        count = 0;

    pd(input);
    for (const instruction of input) {
        const dir = instruction[0];
        const mv = Number(instruction.slice(1));
        const new_val = val + mv * (dir === 'L' ? -1 : 1);

        if (val > 0 && new_val <= 0) count++;

        count += Math.floor(Math.abs(new_val) / 100);

        val = new_val >= 0 ? new_val % 100 : 100 - Math.abs(new_val % 100);
        pd({ dir, mv, new_val, val, count });
    }

    return count;
};

if (require.main === module) {
    main();
}

export { parseInput, solvePart1, solvePart2 };
