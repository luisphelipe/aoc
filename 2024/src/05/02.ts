import * as path from 'path';
import { readFile } from '../utils/input';
import { p, pj } from '../utils/print';

const sampleFilepath = path.join(__dirname, 'sample');
const inputFilepath = path.join(__dirname, 'input');

const main = () => {
        // const rawInput = readFile(sampleFilepath);
        const rawInput = readFile(inputFilepath);
        // pj(rawInput);

        const { rules, updates } = parseInput(rawInput);
        // pj({ rules, updates });

        const result = solve(rules, updates);
        pj(result);
};

const parseInput = (rawInput: string) => {
        const rules = [];
        const updates = [];

        const parsed = rawInput.split('\n');
        let finishedRules = false;

        for (const line of parsed) {
                if (line === '') finishedRules = true;
                else if (!finishedRules) rules.push(line);
                else updates.push(line);
        }

        const parsedUpdates = updates.map((update) => update.split(',').map((v) => Number(v)));

        return { rules, updates: parsedUpdates };
};

const solve = (rules: string[], updates: number[][]) => {
        // "47|53" => 53 must be after 47 => 47 can't be after 53
        const ruleMap: { [key: number]: number[] } = {};

        for (const rule of rules) {
                const [val, key] = rule.split('|').map((n) => Number(n));
                if (!ruleMap[key]) ruleMap[key] = [];
                ruleMap[key].push(val);
        }

        const incorrects = [];

        for (const update of updates) {
                if (!solveLine(ruleMap, update)) {
                        incorrects.push(update);
                }
        }

        let total = 0;

        for (const update of incorrects) {
                total += solveIncorrect(ruleMap, update);
        }

        return total;
};

const solveIncorrect = (ruleMap: { [key: number]: number[] }, update: number[]) => {
        const correct = [update[0]];

        for (const number of update.slice(1)) {
                for (let i = correct.length - 1; i >= 0; i--) {
                        if (ruleMap[number]?.includes(correct[i])) {
                                correct.splice(i + 1, 0, number);
                                break;
                        }

                        if (i === 0) {
                                correct.splice(0, 0, number);
                        }
                }
        }

        // p({ update, correct });

        return correct[Math.floor(correct.length / 2)];
};

const solveLine = (ruleMap: { [key: number]: number[] }, update: number[]) => {
        let shouldNot: number[] = [];

        for (const item of update) {
                if (shouldNot.includes(item)) return 0;
                shouldNot = shouldNot.concat(ruleMap[item]);
        }

        return update[Math.floor(update.length / 2)];
};

main();

export {};
