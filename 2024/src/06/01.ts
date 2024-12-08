import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pj, pm } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

type GuardChar = '^' | '>' | 'v' | '<';
const DIRECTION_MAP = {
        '^': [-1, 0],
        '>': [0, +1],
        v: [1, 0],
        '<': [0, -1],
};
const GUARD_CHAR = Object.keys(DIRECTION_MAP);

const main = () => {
        const rawInput = readFile(sampleFilepath);
        // const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // p('INPUT');
        // pm(input);

        const [output, result] = solve(input);
        p('RESULT:', result);
        pm(output);
};

const parseInput = (rawInput: string) => {
        const parsed = rawInput.split('\n').map((line) => line.split(''));
        return parsed;
};

const solve = (input: string[][]): [string[][], number] => {
        let currentPosition: number[] | undefined = undefined;
        let currentState = [...input.map((line) => [...line])]; // get copy of input

        // find starting position
        for (let row = 0; row < input.length && currentPosition === undefined; row++) {
                for (let col = 0; col < input[row].length && currentPosition === undefined; col++) {
                        const cell = input[row][col];
                        if (GUARD_CHAR.includes(cell)) {
                                currentPosition = [row, col];
                        }
                }
        }

        if (currentPosition === undefined) throw new Error('no guard found');

        while (currentPosition !== undefined) {
                const nextState = getNextCharPosition(currentState, currentPosition);
                currentState = nextState[0];
                currentPosition = nextState[1];
        }

        let total = 0;

        for (const line of currentState) {
                for (const cell of line) {
                        if (cell === 'X') total++;
                }
        }

        return [currentState, total];
};

const getNextCharPosition = (
        input: string[][],
        currentPosition: number[],
): [string[][], number[] | undefined] => {
        const currentGuardChar = input[currentPosition[0]][currentPosition[1]] as GuardChar;
        const currentDirection = DIRECTION_MAP[currentGuardChar];

        const nextPosition = [
                currentPosition[0] + currentDirection[0],
                currentPosition[1] + currentDirection[1],
        ];

        // check if guard is out
        if (
                nextPosition[0] < 0 ||
                nextPosition[0] >= input.length ||
                nextPosition[1] < 0 ||
                nextPosition[1] >= input[0].length
        ) {
                input[currentPosition[0]][currentPosition[1]] = 'X';
                return [input, undefined];
        }

        // check obstacles and change direction
        if (input[nextPosition[0]][nextPosition[1]] === '#') {
                const nextGuardChar = getNextGuardChar(currentGuardChar);
                input[currentPosition[0]][currentPosition[1]] = nextGuardChar;
                return [input, currentPosition];
        }

        // otherwise, just leave mark and move to next position
        input[currentPosition[0]][currentPosition[1]] = 'X';
        input[nextPosition[0]][nextPosition[1]] = currentGuardChar;
        return [input, nextPosition];
};

const getNextGuardChar = (currentChar: GuardChar) => {
        const currentCharIndex = GUARD_CHAR.findIndex((item) => item === currentChar);
        const nextCharIndex = (currentCharIndex + 1) % 4;
        return GUARD_CHAR[nextCharIndex];
};

main();

export {};
