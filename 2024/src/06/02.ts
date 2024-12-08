import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pj, pm, sleep } from '../utils/print';

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

const main = async () => {
        // const rawInput = readFile(sampleFilepath);
        const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const input = parseInput(rawInput);
        // p('INPUT');
        // pm(input);

        const result = await solve(input);
        p('RESULT:', result);
        // pm(output);
};

const parseInput = (rawInput: string) => {
        const parsed = rawInput.split('\n').map((line) => line.split(''));
        return parsed;
};

const solve = async (input: string[][]): Promise<number> => {
        let currentState = [...input.map((line) => [...line])]; // get copy of input
        let currentPosition: number[] | undefined = undefined;
        let startingPosition: number[];

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
        startingPosition = [...currentPosition];

        const visited: { [a: string]: boolean } = {}; // this took me a couple of hours...
        const obstacles: { [a: string]: boolean } = {};

        while (currentPosition !== undefined) {
                const test = await runSimulation(currentState, currentPosition, visited);
                if (test) obstacles[test] = true;
                visited[currentPosition.join(',')] = true;

                const nextState = getNextState(currentState, currentPosition);
                currentState = nextState[0];
                currentPosition = nextState[1];
        }

        delete obstacles[startingPosition.join(',')];

        return Object.keys(obstacles).length;
};

const runSimulation = async (input: string[][], position: number[], visited: any) => {
        let currentState = [...input.map((line) => [...line])]; // get copy of input
        let currentPosition: number[] | undefined = [...position];

        const [_, nextPosition] = getNextState(currentState, currentPosition, false);

        // guard has no next position or there is already an obstacle ahead of him
        if (
                !nextPosition ||
                nextPosition.join(',') === position.join(',') ||
                visited[nextPosition.join(',')]
        )
                return undefined;

        // set obstacle
        currentState[nextPosition[0]][nextPosition[1]] = 'O';
        const obstaclePositionKey = nextPosition.join(',');

        const visitedPositions: { [a: string]: true } = {};
        while (currentPosition !== undefined) {
                const positionKey = getPositionKey(currentState, currentPosition);
                if (visitedPositions[positionKey]) {
                        // p(obstaclePositionKey);
                        // pm(input, '');
                        // pm(currentState, '');
                        // await sleep(1000);
                        return obstaclePositionKey;
                } // new obstacle position
                visitedPositions[positionKey] = true;

                const nextState = getNextState(currentState, currentPosition);
                currentState = nextState[0];
                currentPosition = nextState[1];
        }

        return undefined;
};

const getPositionKey = (input: string[][], position: number[]) => {
        const guard = input[position[0]][position[1]];
        return `${position.join(',')}${guard}`;
};

const getNextState = (
        input: string[][],
        currentPosition: number[],
        commit = true,
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
                return [input, undefined];
        }

        // check obstacles and change direction
        if (['O', '#'].includes(input[nextPosition[0]][nextPosition[1]])) {
                const nextGuardChar = getNextGuardChar(currentGuardChar);
                if (commit) input[currentPosition[0]][currentPosition[1]] = nextGuardChar;
                return [input, currentPosition];
        }

        // otherwise, just move to next position
        if (commit) input[nextPosition[0]][nextPosition[1]] = currentGuardChar;
        return [input, nextPosition];
};

const getNextGuardChar = (currentChar: GuardChar) => {
        const currentCharIndex = GUARD_CHAR.findIndex((item) => item === currentChar);
        const nextCharIndex = (currentCharIndex + 1) % 4;
        return GUARD_CHAR[nextCharIndex];
};

main();

export {};
