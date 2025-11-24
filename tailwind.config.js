/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './core/**/*.py',
    './accounts/**/*.py',
    './categories/**/*.py',
    './profiles/**/*.py',
    './transactions/**/*.py',
    './users/**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
