/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html","./src/**/*.{ts,tsx}"],
  theme: {
    extend: { colors: { tumbleweed: "#D2A679", sage: "#9DBF9E", dusk: "#5E6472" } },
  },
  plugins: [],
}