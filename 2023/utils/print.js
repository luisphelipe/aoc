const COLOR_RESET = "\x1b[0m";

const FG_COLORS = {
  black: "\x1b[30m",
  red: "\x1b[31m",
  green: "\x1b[32m",
  yellow: "\x1b[33m",
  blue: "\x1b[34m",
  magenta: "\x1b[35m",
  cyan: "\x1b[36m",
  white: "\x1b[37m",
  gray: "\x1b[90m",
};

const BG_COLORS = {
  black: "\x1b[40m",
  red: "\x1b[41m",
  green: "\x1b[42m",
  yellow: "\x1b[43m",
  blue: "\x1b[44m",
  magenta: "\x1b[45m",
  cyan: "\x1b[46m",
  white: "\x1b[47m",
  gray: "\x1b[100m",
};

const colorMatch = (string, match, _options = {}) => {
  const defaultOptions = { color: "magenta", type: "BG" };
  const options = { ...defaultOptions, ..._options };
  const COLORS = options.type === "FG" ? FG_COLORS : BG_COLORS;

  const hasMatch = string.match(match);
  if (!hasMatch) return string;

  const selectedColor = COLORS[options.color] || COLORS[blue];
  const colored = string.replace(
    match,
    `${selectedColor}${hasMatch[0]}${COLOR_RESET}`
  );

  return colored;
};

const printDebug = (string, debug = true) => {
  if (debug) {
    console.log(string);
  }
};

module.exports = { printDebug, colorMatch };
