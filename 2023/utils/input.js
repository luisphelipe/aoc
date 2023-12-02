const fs = require("node:fs/promises");
const path = require("node:path");

const readExample = (dirname, _options = {}) => {
  return readInput(dirname, { filename: "./example", ..._options });
};

const readInput = async (dirname, _options = {}) => {
  const defaultOptions = { filename: "./input", splitLines: true };
  const options = { ...defaultOptions, ..._options };

  const data = await readFile(path.resolve(dirname, options.filename));

  if (options.splitLines) {
    return data.split("\n");
  }

  return data;
};

const readFile = async (filename) => {
  try {
    const data = await fs.readFile(filename, { encoding: "utf8" });
    return data;
  } catch (err) {
    console.log(err);
    throw err;
  }
};

module.exports = { readFile, readInput, readExample };
